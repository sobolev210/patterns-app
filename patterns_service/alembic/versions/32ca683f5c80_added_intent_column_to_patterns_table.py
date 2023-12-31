"""Added intent column to patterns table

Revision ID: 32ca683f5c80
Revises: 45aa3ed1625a
Create Date: 2023-08-05 16:15:47.243528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32ca683f5c80'
down_revision = '45aa3ed1625a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patterns', sa.Column('intent', sa.Text(), nullable=True))
    op.execute("UPDATE patterns SET intent = 'Not filled'")
    op.alter_column("patterns", "intent", nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patterns', 'intent')
    # ### end Alembic commands ###
