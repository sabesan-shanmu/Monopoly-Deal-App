
from flask_restx import Resource,Namespace
from flask import request,jsonify
from marshmallow import ValidationError
from .services import get_game_cards_in_play
from monopoly.api.games.services import get_game_by_gamepasscode
from .schema import GameCardSchema
from monopoly.auth import validate_gamepassCode,validate_player
from monopoly.exceptions import ResourceNotFoundException,ResourceValidationException,FieldValidationException
from marshmallow import ValidationError



game_cards_namespace = Namespace('GameCards', description='Game cards that are in play on the board')


@game_cards_namespace.route('/')
class ManyGameCardsResource(Resource):
    @validate_gamepassCode
    def get(self,gamePassCode):
        try:
            game = get_game_by_gamepasscode(gamePassCode)
            if game is None:
                raise ResourceNotFoundException(message="Game Not Found")    
            gameCards = get_game_cards_in_play(game.gamePassCode)
            result = GameCardSchema(many=True).dump(gameCards)
            return jsonify(result)
        except ValidationError as e:
            raise ResourceValidationException(e)
    
@game_cards_namespace.route('/<int:gameCardId>/')
class SingleGameCardsResource(Resource):
    @validate_gamepassCode
    @validate_player
    def put(self,gamePassCode,gameCardId):
        pass