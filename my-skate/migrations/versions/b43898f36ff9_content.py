"""content

Revision ID: b43898f36ff9
Revises: be89d8f7a803
Create Date: 2023-09-11 14:14:15.024828

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b43898f36ff9'
down_revision = 'be89d8f7a803'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128),
               type_=sa.String(length=512),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=sa.String(length=512),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128),
               existing_nullable=True)

    # ### end Alembic commands ###