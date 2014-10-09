"""Initial alembic migration

Revision ID: 3e52765e7151
Revises: None
Create Date: 2014-10-09 13:51:43.204915

"""

# revision identifiers, used by Alembic.
revision = '3e52765e7151'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('given_name', sa.String(length=128), nullable=True),
    sa.Column('family_name', sa.String(length=128), nullable=True),
    sa.Column('picture', sa.String(length=256), nullable=True),
    sa.Column('role', sa.String(length=32), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('base_path', sa.String(length=1024), nullable=True),
    sa.Column('git_address', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('host',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('params', sa.Text(), nullable=True),
    sa.Column('provider', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teams_users',
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('vagrant_instance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=256), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('environment', sa.String(length=128), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('host_id', sa.Integer(), nullable=True),
    sa.Column('git_reference', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['host_id'], ['host.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_permissions_grids',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('objectId', sa.Integer(), nullable=True),
    sa.Column('objectType', sa.String(length=64), nullable=True),
    sa.Column('action', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team_permissions_grids',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('objectId', sa.Integer(), nullable=True),
    sa.Column('objectType', sa.String(length=64), nullable=True),
    sa.Column('action', sa.String(length=64), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team_permissions_grids')
    op.drop_table('user_permissions_grids')
    op.drop_table('vagrant_instance')
    op.drop_table('teams_users')
    op.drop_table('host')
    op.drop_table('project')
    op.drop_table('team')
    op.drop_table('user')
    ### end Alembic commands ###