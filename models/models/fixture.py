"""Fixture model"""

from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db, timestamp


class Fixture(Base):
    """A class representing a fixture in Fantasy Premier League."""

    __versioned__ = {}
    __tablename__ = "fixtures"

    # FPL api properties
    fpl_id: Mapped[int] = mapped_column(sort_order=-1)
    code: Mapped[int] = mapped_column(unique=True, sort_order=-1)
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

    # Additional properties
    season: Mapped[Optional[int]]

    # Foreign keys
    gameweek: Mapped[int] = mapped_column(
        db.ForeignKey("gameweeks.id"), sort_order=-1
    )
    team_a: Mapped[int] = mapped_column(
        db.ForeignKey("teams.id"), sort_order=-1
    )
    team_h: Mapped[int] = mapped_column(
        db.ForeignKey("teams.id"), sort_order=-1
    )

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Return the constraints that the upsert will use to identify
        conflicts"""
        return ["code"]
