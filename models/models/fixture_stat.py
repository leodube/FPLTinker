"""FixtureStat model"""

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db


class FixtureStat(Base):
    """A class representing a fixtures stat in Fantasy Premier League."""

    __tablename__ = "fixture_stats"
    __table_args__ = (
        db.UniqueConstraint("fixture_id", "team_id", "stat_details_id", "player_id"),
    )

    # Foreign Keys
    fixture_id: Mapped[int] = mapped_column(db.ForeignKey("fixtures.id"))
    team_id: Mapped[int] = mapped_column(db.ForeignKey("teams.id"))
    stat_details_id: Mapped[int] = mapped_column(db.ForeignKey("stat_details.id"))
    player_id: Mapped[int] = mapped_column(db.ForeignKey("players.id"))

    # FPL api properties
    value: Mapped[int]

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Returns the constraints that the upsert will use to identify
        conflicts"""
        return ["fixture_id", "team_id", "stat_details_id", "player_id"]
