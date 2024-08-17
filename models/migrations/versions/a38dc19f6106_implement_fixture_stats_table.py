"""Implement fixture stats table.

Revision ID: a38dc19f6106
Revises: c99e5c4a209a
Create Date: 2024-08-16 15:42:46.936207

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a38dc19f6106"
down_revision = "c99e5c4a209a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(
        "fixture_stats", schema=None, recreate="always"
    ) as batch_op:
        batch_op.add_column(
            sa.Column("fixture_id", sa.Integer(), nullable=False),
            insert_after="id",
        )
        batch_op.add_column(
            sa.Column("team_id", sa.Integer(), nullable=False),
            insert_before="created_at",
        )
        batch_op.add_column(
            sa.Column("stat_details_id", sa.Integer(), nullable=False),
            insert_before="created_at",
        )
        batch_op.add_column(
            sa.Column("player_id", sa.Integer(), nullable=False),
            insert_before="created_at",
        )
        batch_op.add_column(
            sa.Column("value", sa.Integer(), nullable=False),
            insert_before="created_at",
        )
        batch_op.create_foreign_key(
            "fixture_stats_stat_details_id_fkey",
            "stat_details",
            ["stat_details_id"],
            ["id"],
        )
        batch_op.create_foreign_key(
            "fixture_stats_player_id_fkey", "players", ["player_id"], ["id"]
        )
        batch_op.create_foreign_key(
            "fixture_stats_fixture_id_fkey", "fixtures", ["fixture_id"], ["id"]
        )
        batch_op.create_foreign_key(
            "fixture_stats_team_id_fkey", "teams", ["team_id"], ["id"]
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("fixture_stats", schema=None) as batch_op:
        batch_op.drop_constraint(
            "fixture_stats_stat_details_id_fkey", type_="foreignkey"
        )
        batch_op.drop_constraint("fixture_stats_player_id_fkey", type_="foreignkey")
        batch_op.drop_constraint("fixture_stats_fixture_id_fkey", type_="foreignkey")
        batch_op.drop_constraint("fixture_stats_team_id_fkey", type_="foreignkey")
        batch_op.drop_column("value")
        batch_op.drop_column("player_id")
        batch_op.drop_column("stat_details_id")
        batch_op.drop_column("team_id")
        batch_op.drop_column("fixture_id")

    # ### end Alembic commands ###
