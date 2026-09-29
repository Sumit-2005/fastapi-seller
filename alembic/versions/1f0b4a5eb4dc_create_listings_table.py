"""create listings table

Revision ID: 1f0b4a5eb4dc
Revises: 
Create Date: 2026-09-28 11:17:08.361553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f0b4a5eb4dc'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('listings',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('description', sa.String(), nullable=False),
                    sa.Column('category', sa.String(), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=False),
                    sa.Column('stock', sa.Integer(), nullable=False),
                    sa.Column('shipping_info', sa.String(), nullable=False),
                    sa.Column('image', sa.String(), nullable=True))
    pass

def downgrade() -> None:

    op.drop_table('listings')
    pass
