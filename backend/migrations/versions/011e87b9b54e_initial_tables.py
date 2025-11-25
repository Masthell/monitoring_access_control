"""Initial tables

Revision ID: 011e87b9b54e
Revises: 752d97d25782
Create Date: 2025-11-25 17:46:13.957136

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '011e87b9b54e'
down_revision: Union[str, Sequence[str], None] = '752d97d25782'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
