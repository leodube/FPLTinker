"""Remove timestamps from some stat tables.

Revision ID: 6cec9828deda
Revises: a38dc19f6106
Create Date: 2024-08-16 17:27:05.562579

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "6cec9828deda"
down_revision = "a38dc19f6106"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("fixture_stats", schema=None) as batch_op:
        batch_op.create_unique_constraint(
            "fixture_stats_fixture_id_team_id_stat_details_id_player_id_key",
            ["fixture_id", "team_id", "stat_details_id", "player_id"],
        )
        batch_op.drop_column("updated_at")
        batch_op.drop_column("created_at")

    with op.batch_alter_table("stat_details", schema=None) as batch_op:
        batch_op.drop_column("updated_at")
        batch_op.drop_column("created_at")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("stat_details", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "created_at",
                postgresql.TIMESTAMP(),
                server_default=sa.text("CURRENT_TIMESTAMP"),
                autoincrement=False,
                nullable=False,
            )
        )
        batch_op.add_column(
            sa.Column(
                "updated_at",
                postgresql.TIMESTAMP(),
                server_default=sa.text("CURRENT_TIMESTAMP"),
                autoincrement=False,
                nullable=False,
            )
        )

    with op.batch_alter_table("fixture_stats", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "created_at",
                postgresql.TIMESTAMP(),
                server_default=sa.text("CURRENT_TIMESTAMP"),
                autoincrement=False,
                nullable=False,
            )
        )
        batch_op.add_column(
            sa.Column(
                "updated_at",
                postgresql.TIMESTAMP(),
                server_default=sa.text("CURRENT_TIMESTAMP"),
                autoincrement=False,
                nullable=False,
            )
        )
        batch_op.drop_constraint(
            "fixture_stats_fixture_id_team_id_stat_details_id_player_id_key",
            type_="unique",
        )

    # ### end Alembic commands ###
