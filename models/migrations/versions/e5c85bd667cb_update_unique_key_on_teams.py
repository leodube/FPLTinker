"""Update unique key on teams.

Revision ID: e5c85bd667cb
Revises: 441b4b9fc5e8
Create Date: 2024-08-20 09:46:04.223991

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e5c85bd667cb"
down_revision = "441b4b9fc5e8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("teams", schema=None) as batch_op:
        batch_op.drop_constraint("teams_fpl_id_key", type_="unique")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("teams", schema=None) as batch_op:
        batch_op.create_unique_constraint("teams_fpl_id_key", ["fpl_id"])

    # ### end Alembic commands ###
