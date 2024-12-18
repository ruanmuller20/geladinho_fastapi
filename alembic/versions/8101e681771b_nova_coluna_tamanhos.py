"""Nova coluna tamanhos

Revision ID: 8101e681771b
Revises: 8b8ef6da6126
Create Date: 2024-12-10 23:47:57.975913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8101e681771b'
down_revision: Union[str, None] = '8b8ef6da6126'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('tamanhos', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('produto', 'tamanhos')
    # ### end Alembic commands ###