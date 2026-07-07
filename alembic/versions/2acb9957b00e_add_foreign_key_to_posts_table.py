"""add foreign-key to posts table

Revision ID: 2acb9957b00e
Revises: 0f43cee769b6
Create Date: 2026-07-06 21:07:10.248618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2acb9957b00e'
down_revision: Union[str, Sequence[str], None] = '0f43cee769b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable= False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('posts_users_fk', table_name= 'posts')
    op.drop_column('posts', 'owner_id')
    pass
