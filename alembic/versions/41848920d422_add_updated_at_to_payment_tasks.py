"""add updated_at to payment_tasks

Revision ID: 41848920d422
Revises: 97ca8f0a862d
Create Date: 2020-02-26 23:27:11.475072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41848920d422'
down_revision = '97ca8f0a862d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'payment_tasks',
        sa.Column('updated_at', sa.DateTime)
    )


def downgrade():
    op.drop_column('payment_tasks', 'updated_at')
