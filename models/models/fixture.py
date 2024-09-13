"""Fixture model"""

from __future__ import annotations

from typing import List, Optional

from dateutil.parser import parse
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, WithTimestamps
from .db import db, timestamp


class Fixture(Base, WithTimestamps):
    """A class representing a fixture in Fantasy Premier League."""

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
    gameweek_id: Mapped[int] = mapped_column(
        db.ForeignKey("gameweeks.id"), sort_order=-1
    )
    team_a_id: Mapped[int] = mapped_column(db.ForeignKey("teams.id"), sort_order=-1)
    team_h_id: Mapped[int] = mapped_column(db.ForeignKey("teams.id"), sort_order=-1)

    # Relationships
    gameweek: Mapped["Gameweek"] = db.relationship(
        back_populates="fixtures", viewonly=True, init=False
    )
    stats: Mapped[List["FixtureStat"]] = db.relationship(init=False)

    # Post initialization
    def __post_init__(self):
        self.kickoff_time = parse(self.kickoff_time, ignoretz=True)

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Returns the constraints that the upsert will use to identify
        conflicts"""
        return ["code"]
