"""Renaming students to scholars

Revision ID: 483842aa3d28
Revises: 791279dd0760
Create Date: 2022-12-27 08:20:27.640161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '483842aa3d28'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')

