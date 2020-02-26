"""create user table

Revision ID: 325060948345
Revises:
Create Date: 2020-02-25 23:29:32.793389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '325060948345'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String),
        sa.Column('last_name', sa.String),
        sa.Column('email', sa.String),
        sa.Column('balance', sa.Integer, default=500)
    )

def downgrade():
    op.drop_table('users')
