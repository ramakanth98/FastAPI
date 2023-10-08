"""Add content column to post table

Revision ID: 9f31b5aa2b82
Revises: 3caeed041d9d
Create Date: 2023-10-07 14:35:19.612952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f31b5aa2b82'
down_revision: Union[str, None] = '3caeed041d9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
