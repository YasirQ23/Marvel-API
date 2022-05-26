"""empty message

Revision ID: 3324aebf4062
Revises: e00003de211d
Create Date: 2022-05-26 12:05:47.021969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3324aebf4062'
down_revision = 'e00003de211d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('api_token', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'api_token')
    # ### end Alembic commands ###