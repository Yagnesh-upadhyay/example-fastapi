"""add content column to posts table

Revision ID: 08d974e2b902
Revises: e57aeebead68
Create Date: 2026-07-06 20:51:20.534392

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08d974e2b902'
down_revision: Union[str, Sequence[str], None] = 'e57aeebead68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable= False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
