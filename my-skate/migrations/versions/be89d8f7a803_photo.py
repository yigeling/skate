"""photo

Revision ID: be89d8f7a803
Revises: 28bc71fcc103
Create Date: 2023-09-11 13:32:47.924895

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'be89d8f7a803'
down_revision = '28bc71fcc103'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_post', schema=None) as batch_op:
        batch_op.alter_column('photo',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128),
               type_=sa.String(length=512),
               existing_nullable=True)
        batch_op.create_foreign_key(None, 'user_info', ['u_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('photo',
               existing_type=sa.String(length=512),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128),
               existing_nullable=True)

    # ### end Alembic commands ###
