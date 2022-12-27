"""Renaming name to fun

Revision ID: 42a5493fd518
Revises: 483842aa3d28
Create Date: 2022-12-27 08:29:51.248436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42a5493fd518'
down_revision = '483842aa3d28'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'name', new_column_name='fun')


def downgrade() -> None:
    pass
