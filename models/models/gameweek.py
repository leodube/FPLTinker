"""Gameweek model"""

# pylint: disable=unsubscriptable-object

from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, WithTimestamps
from .db import db, optional_timestamp, timestamp


class Gameweek(Base, WithTimestamps):
    """A class representing a gameweek in Fantasy Premier League."""

    __tablename__ = "gameweeks"
    __table_args__ = (db.UniqueConstraint("fpl_id", "season"),)

    # FPL api properties
    fpl_id: Mapped[int] = mapped_column(sort_order=-1)
    name: Mapped[str]
    average_entry_score: Mapped[int]
    data_checked: Mapped[bool]
    deadline_time: Mapped[timestamp]
    finished: Mapped[bool]
    is_current: Mapped[bool]
    is_next: Mapped[bool]
    is_previous: Mapped[bool]
    ranked_count: Mapped[int]
    transfers_made: Mapped[int]
    highest_score: Mapped[Optional[int]]
    highest_scoring_entry: Mapped[Optional[int]]
    most_captained: Mapped[Optional[int]]
    most_selected: Mapped[Optional[int]]
    most_transferred_in: Mapped[Optional[int]]
    most_vice_captained: Mapped[Optional[int]]
    release_time: Mapped[optional_timestamp]

    # Foreign Keys
    top_player_id: Mapped[Optional[int]] = mapped_column(db.ForeignKey("players.id"))

    # Additional properties
    season: Mapped[Optional[int]]

    # Relationships
    fixtures: Mapped[List["Fixture"]] = db.relationship(
        back_populates="gameweek", init=False
    )
    top_player: Mapped["Player"] = db.relationship(viewonly=True, init=False)

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Returns the constraints that the upsert will use to identify
        conflicts"""
        return ["fpl_id", "season"]
