"""Fixture model"""

from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db, timestamp

DEFAULT_SEASON = 20232024


class Fixture(Base):
    """A class representing a fixture in Fantasy Premier League."""

    __versioned__ = {}
    __tablename__ = "fixtures"

    # FPL api properties
    fpl_id: Mapped[int]
    code: Mapped[int]
    finished: Mapped[bool]
    finished_provisional: Mapped[bool]
    kickoff_time: Mapped[timestamp]
    minutes: Mapped[int]
    provisional_start_time: Mapped[bool]
    started: Mapped[bool]
    team_a_difficulty: Mapped[int]
    team_a_score: Mapped[Optional[int]]
    team_h_difficulty: Mapped[int]
    team_h_score: Mapped[Optional[int]]

    # Unused properties returned by FPL api
    stats: list  # FUTURE: create fixture_stats model to store these stats

    # Additional properties
    season: Mapped[int] = mapped_column(init=False, default=DEFAULT_SEASON)

    # Foreign keys
    gameweek: Mapped[int] = mapped_column(db.ForeignKey("gameweeks.id"))
    team_a: Mapped[int] = mapped_column(db.ForeignKey("teams.id"))
    team_h: Mapped[int] = mapped_column(db.ForeignKey("teams.id"))

    # Methods
    @classmethod
    def index_constraints(cls):
        """Description"""
        return ["code"]
