"""empty message

Revision ID: c00714c5984f
Revises: 
Create Date: 2023-08-15 22:21:22.881904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c00714c5984f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('user_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('sex', sa.String(length=128), nullable=True),
    sa.Column('photo', sa.String(length=128), nullable=True),
    sa.Column('signature', sa.String(length=128), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['name'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user_post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('head', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(length=128), nullable=True),
    sa.Column('photo', sa.String(length=128), nullable=True),
    sa.Column('user_like', sa.Integer(), nullable=False),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['u_id'], ['user_info.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_post')
    op.drop_table('user_info')
    op.drop_table('user')
    # ### end Alembic commands ###
