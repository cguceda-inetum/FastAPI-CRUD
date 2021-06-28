"""default date time

Revision ID: d115f9a0d897
Revises: a8624baa512b
Create Date: 2021-06-18 15:23:46.007799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.

revision = 'd115f9a0d897'
down_revision = 'a8624baa512b'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('posts', 'created', server_default=sa.text("CURRENT_TIMESTAMP"))
    op.alter_column('posts', 'modified', server_default=sa.text("CURRENT_TIMESTAMP"))


def downgrade():
    op.alter_column('posts', 'created', server_default=None)
    op.alter_column('posts', 'modified', server_default=None)
