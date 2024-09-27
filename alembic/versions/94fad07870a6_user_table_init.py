"""user table init

Revision ID: 94fad07870a6
Revises: 
Create Date: 2024-09-26 17:11:01.754959

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '94fad07870a6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('telegram_id', sa.String(length=20), nullable=False),
                    sa.Column('username', sa.String(length=32), nullable=True),
                    sa.Column('full_name', sa.String(length=64), nullable=True),
                    sa.Column('is_active', sa.Boolean(), server_default='1', nullable=False),
                    sa.Column('is_admin', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('id', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
                    sa.UniqueConstraint('telegram_id', name=op.f('uq_users_telegram_id'))
                    )


def downgrade() -> None:
    op.drop_table('users')
