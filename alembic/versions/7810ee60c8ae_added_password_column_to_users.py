"""added password column to users

Revision ID: 7810ee60c8ae
Revises: ac71f94f06e2
Create Date: 2026-09-18 22:04:21.669399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7810ee60c8ae'
down_revision: Union[str, Sequence[str], None] = 'ac71f94f06e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'users',
        sa.Column('password', sa.String(length=255), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'password')