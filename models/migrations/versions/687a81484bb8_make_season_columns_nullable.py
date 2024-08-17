"""Make season columns nullable.

Revision ID: 687a81484bb8
Revises: edd961afb15c
Create Date: 2024-08-14 22:18:49.046029

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "687a81484bb8"
down_revision = "edd961afb15c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("fixtures", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=True)

    with op.batch_alter_table("gameweeks", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=True)

    with op.batch_alter_table("player_stats", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=True)

    with op.batch_alter_table("players", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=True)

    with op.batch_alter_table("positions", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=True)

    with op.batch_alter_table("teams", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("teams", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=False)

    with op.batch_alter_table("positions", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=False)

    with op.batch_alter_table("players", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=False)

    with op.batch_alter_table("player_stats", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=False)

    with op.batch_alter_table("gameweeks", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=False)

    with op.batch_alter_table("fixtures", schema=None) as batch_op:
        batch_op.alter_column("season", existing_type=sa.INTEGER(), nullable=False)

    # ### end Alembic commands ###
