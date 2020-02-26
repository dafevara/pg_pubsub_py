"""create other basic tables

Revision ID: 97ca8f0a862d
Revises: 325060948345
Create Date: 2020-02-26 00:03:58.703702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97ca8f0a862d'
down_revision = '325060948345'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('price', sa.Integer),
        sa.Column('stock', sa.Integer),
        sa.Column('discount', sa.Integer)
    )

    op.create_table(
        'payments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('product_id', sa.Integer),
        sa.Column('user_id', sa.Integer),
        sa.Column('ammount', sa.Integer)
    )

    op.create_table(
        'payment_tasks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('payment_id', sa.Integer),
        sa.Column('tries_left', sa.Integer),
        sa.Column('next_try_at', sa.DateTime),
        sa.Column('priority', sa.Integer),
        sa.Column('error', sa.String),
        sa.Column('processing', sa.Boolean),
        sa.Column('context', sa.JSON)
    )


def downgrade():
    op.drop_table('products')
    op.drop_table('payments')
    op.drop_table('payment_tasks')
