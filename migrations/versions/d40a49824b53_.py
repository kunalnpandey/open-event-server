"""empty message

Revision ID: d40a49824b53
Revises: aa4b21539f5b
Create Date: 2016-06-16 13:31:57.438513

"""

# revision identifiers, used by Alembic.
revision = 'd40a49824b53'
down_revision = 'aa4b21539f5b'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_detail', sa.Column('avatar_uploaded', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_detail', 'avatar_uploaded')
    ### end Alembic commands ###
