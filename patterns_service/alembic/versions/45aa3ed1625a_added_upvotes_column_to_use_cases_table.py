"""Added upvotes column to use cases table

Revision ID: 45aa3ed1625a
Revises: 55c84de7ef84
Create Date: 2023-08-04 21:00:16.274562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45aa3ed1625a'
down_revision = '55c84de7ef84'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('use_cases', sa.Column('upvotes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('use_cases', 'upvotes')
    # ### end Alembic commands ###
