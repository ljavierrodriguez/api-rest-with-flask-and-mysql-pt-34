"""empty message

Revision ID: 5c2a1972f6c5
Revises: 46b3f183df3d
Create Date: 2023-03-31 22:53:41.539247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c2a1972f6c5'
down_revision = '46b3f183df3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('biography', sa.Text(), nullable=True),
    sa.Column('github', sa.String(length=100), nullable=True),
    sa.Column('linkedin', sa.String(length=100), nullable=True),
    sa.Column('instagram', sa.String(length=100), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###
