"""Add FDR table.

Revision ID: 891580dfdb26
Revises: e5c85bd667cb
Create Date: 2024-09-06 09:02:44.573192

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "891580dfdb26"
down_revision = "e5c85bd667cb"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "fdr",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("team_id", sa.Integer(), nullable=False),
        sa.Column("team_name", sa.String(), nullable=False),
        sa.Column(
            "type",
            sa.Enum(
                "ALL",
                "GOALKEEPER",
                "DEFENDER",
                "MIDFIELDER",
                "FORWARD",
                name="fdrtypes",
            ),
            nullable=False,
        ),
        sa.Column("home", sa.Numeric(8, 2), nullable=False),
        sa.Column("away", sa.Numeric(8, 2), nullable=False),
        sa.Column("season", sa.Integer(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["team_id"], ["teams.id"], name="fdr_team_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="fdr_pkey"),
        sa.UniqueConstraint("team_id", "type", name="fdr_team_id_type_key"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("fdr", schema=None) as batch_op:
        batch_op.drop_constraint("fdr_team_id_fkey", type_="foreignkey")

    op.drop_table("fdr")
    op.execute("DROP TYPE fdrtypes")
    # ### end Alembic commands ###
