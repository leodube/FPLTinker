"""Add precision to player stats.

Revision ID: 628ad57a5e52
Revises: c2cfd4d8096d
Create Date: 2024-08-15 22:37:07.850781

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "628ad57a5e52"
down_revision = "c2cfd4d8096d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("player_stats", schema=None) as batch_op:
        batch_op.alter_column(
            "clean_sheets_per_90",
            existing_type=sa.INTEGER(),
            type_=sa.Numeric(8, 2),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "creativity",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="creativity::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_assists",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="expected_assists::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_assists_per_90",
            existing_type=sa.INTEGER(),
            type_=sa.Numeric(8, 2),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goal_involvements",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="expected_goal_involvements::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goal_involvements_per_90",
            existing_type=sa.INTEGER(),
            type_=sa.Numeric(8, 2),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goals",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="expected_goals::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goals_per_90",
            existing_type=sa.INTEGER(),
            type_=sa.Numeric(8, 2),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goals_conceded",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="expected_goals_conceded::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goals_conceded_per_90",
            existing_type=sa.INTEGER(),
            type_=sa.Numeric(8, 2),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "form",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="form::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "goals_conceded_per_90",
            existing_type=sa.INTEGER(),
            type_=sa.Numeric(8, 2),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "ict_index",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="ict_index::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "influence",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="influence::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "points_per_game",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="points_per_game::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "saves_per_90",
            existing_type=sa.INTEGER(),
            type_=sa.Numeric(8, 2),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "selected_by_percent",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="selected_by_percent::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "starts_per_90",
            existing_type=sa.INTEGER(),
            type_=sa.Numeric(8, 2),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "threat",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="threat::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "value_form",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="value_form::numeric",
            existing_nullable=False,
        )
        batch_op.alter_column(
            "value_season",
            existing_type=sa.VARCHAR(),
            type_=sa.Numeric(8, 2),
            postgresql_using="value_season::numeric",
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("player_stats", schema=None) as batch_op:
        batch_op.alter_column(
            "value_season",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "value_form",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "threat",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "starts_per_90",
            existing_type=sa.Numeric(8, 2),
            type_=sa.INTEGER(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "selected_by_percent",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "saves_per_90",
            existing_type=sa.Numeric(8, 2),
            type_=sa.INTEGER(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "points_per_game",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "influence",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "ict_index",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "goals_conceded_per_90",
            existing_type=sa.Numeric(8, 2),
            type_=sa.INTEGER(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "form",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goals_conceded_per_90",
            existing_type=sa.Numeric(8, 2),
            type_=sa.INTEGER(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goals_conceded",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goals_per_90",
            existing_type=sa.Numeric(8, 2),
            type_=sa.INTEGER(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goals",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goal_involvements_per_90",
            existing_type=sa.Numeric(8, 2),
            type_=sa.INTEGER(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_goal_involvements",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_assists_per_90",
            existing_type=sa.Numeric(8, 2),
            type_=sa.INTEGER(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "expected_assists",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "creativity",
            existing_type=sa.Numeric(8, 2),
            type_=sa.VARCHAR(),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "clean_sheets_per_90",
            existing_type=sa.Numeric(8, 2),
            type_=sa.INTEGER(),
            existing_nullable=False,
        )

    # ### end Alembic commands ###
