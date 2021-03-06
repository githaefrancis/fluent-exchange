"""add subscribers table

Revision ID: 915ad9fc5f76
Revises: 9e416621fa1a
Create Date: 2022-02-12 11:19:37.156319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '915ad9fc5f76'
down_revision = '9e416621fa1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscribers')
    # ### end Alembic commands ###
