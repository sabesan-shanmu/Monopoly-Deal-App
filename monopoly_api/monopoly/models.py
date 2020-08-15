from monopoly import db
import monopoly.common.enums as Enum
import uuid
from datetime import datetime
from sqlalchemy import UniqueConstraint


class PropertiesCard(db.Model):
    propertiesCardId = db.Column(db.Integer, primary_key=True,nullable=False)
    name = db.Column(db.String,nullable=False)
    primaryColourId = db.Column(db.Integer,db.Enum(Enum.Colours),nullable=False)
    secondaryColourId = db.Column(db.Integer,db.Enum(Enum.Colours),nullable=True)
    price= db.Column(db.Integer,nullable=False)


class PropertiesColor(db.Model):
    colorId = db.Column(db.Integer,db.Enum(Enum.Colours),nullable=False,primary_key=True)
    onePairRentPrice = db.Column(db.Integer,nullable=False)
    twoPairRentPrice = db.Column(db.Integer,nullable=False)
    threePairRentPrice = db.Column(db.Integer,nullable=False)
    fourPairRentPrice = db.Column(db.Integer,nullable=False)
    numberNeededToCompleteSet = db.Column(db.Integer,nullable=False)

class CashCard(db.Model):
    cashCardId = db.Column(db.Integer,primary_key=True,nullable=False)
    price = db.Column(db.Integer,nullable=False)


class RentCard(db.Model):
    rentCardId = db.Column(db.Integer,primary_key=True,nullable=False)
    primaryColourId = db.Column(db.Integer,db.Enum(Enum.Colours),nullable=False)
    secondaryColourId = db.Column(db.Integer,db.Enum(Enum.Colours),nullable=True)
    payee = db.Column(db.Integer,db.Enum(Enum.Payee),nullable=False)


class ActionCard(db.Model):
    actionCardId = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String,nullable=False)
    price= db.Column(db.Integer,nullable=False)
    actionType = db.Column(db.Integer,db.Enum(Enum.ActionType),nullable=False)


class Player(db.Model):
    __table_args__ = (
        db.UniqueConstraint('gameId', 'playerName',name='unique_player'),
    )
    playerId = db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    playerPassCode = db.Column(db.String,nullable=False)
    gameId = db.Column(db.Integer,db.ForeignKey("game.gameId"),nullable=False)
    playerName = db.Column(db.String)
    playerGameOrder = db.Column(db.Integer)

   
class Cards(db.Model):
    cardId = db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    cardType =  db.Column(db.Enum(Enum.CardTypes))
    propertiesCardId = db.Column(db.Integer,db.ForeignKey("properties_card.propertiesCardId"))
    cashCardId = db.Column(db.Integer,db.ForeignKey("cash_card.cashCardId"))
    rentId = db.Column(db.Integer,db.ForeignKey("rent_card.rentCardId"))
    actionId = db.Column(db.Integer,db.ForeignKey("action_card.actionCardId"))
    properties = db.relationship(PropertiesCard)  
    cash = db.relationship(CashCard,primaryjoin=cashCardId==CashCard.cashCardId)  
    rent = db.relationship(RentCard,primaryjoin=rentId==RentCard.rentCardId)
    action = db.relationship(ActionCard,primaryjoin=actionId==ActionCard.actionCardId)




class GameCards(db.Model):
    __table_args__ = (
        db.PrimaryKeyConstraint('gameId', 'cardId'),
    )
    gameId = db.Column(db.Integer,db.ForeignKey("game.gameId"),nullable=True)
    cardId = db.Column(db.Integer,db.ForeignKey("cards.cardId"),nullable=True)
    playerId = db.Column(db.Integer,db.ForeignKey("player.playerId"),nullable=True)
    cardStatus = db.Column(db.Enum(Enum.GameCardStatus),nullable=False, default=Enum.GameCardStatus.IsNotDrawn)





class Game(db.Model):
    gameId = db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    gamePassCode = db.Column(db.String, unique=True,nullable=False,default=uuid.uuid4)
    numberOfPlayers = db.Column(db.Integer,nullable=False,default=0)
    name = db.Column(db.String,nullable=False)
    currentPlayerId = db.Column(db.Integer,db.ForeignKey("player.playerId",use_alter=True, name='fk_game_current_player_id',ondelete='CASCADE'))
    numberOfTurnsPlayed = db.Column(db.Integer,nullable=False,default=0)
    gameStatus = db.Column(db.Enum(Enum.GameStatus),nullable=False, default=Enum.GameStatus.WaitingToStart)
    createdUtcDate = db.Column(db.DateTime,default=datetime.utcnow())
    currentInPlayCardId = db.Column(db.Integer,db.ForeignKey("cards.cardId",use_alter=True,name="fk_game_card_id"),nullable=True)
    isPlayerTurnComplete = db.Column(db.Boolean,nullable=False,default=False)
    players =  db.relationship(Player,primaryjoin=gameId==Player.gameId,passive_deletes=True)
    def __str__(self):
        return self.name