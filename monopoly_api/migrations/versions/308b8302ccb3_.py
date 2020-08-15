"""empty message

Revision ID: 308b8302ccb3
Revises: ab47be0a9ec4
Create Date: 2020-08-14 23:16:07.083063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '308b8302ccb3'
down_revision = 'ab47be0a9ec4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_game_current_player_id', 'game', type_='foreignkey')
    op.create_foreign_key('fk_game_current_player_id', 'game', 'player', ['currentPlayerId'], ['playerId'], ondelete='CASCADE', use_alter=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_game_current_player_id', 'game', type_='foreignkey')
    op.create_foreign_key('fk_game_current_player_id', 'game', 'player', ['currentPlayerId'], ['playerId'])
    # ### end Alembic commands ###
