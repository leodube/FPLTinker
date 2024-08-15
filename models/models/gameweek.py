"""Gameweek model"""

# pylint: disable=unsubscriptable-object

from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db


class Gameweek(Base):
    """A class representing a gameweek in Fantasy Premier League."""

    __versioned__ = {}
    __tablename__ = "gameweeks"
    __table_args__ = (db.UniqueConstraint("fpl_id", "season"),)

    # FPL api properties
    fpl_id: Mapped[int] = mapped_column(sort_order=-1)
    name: Mapped[str]
    average_entry_score: Mapped[int]
    data_checked: Mapped[bool]
    deadline_time: Mapped[str]
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
    release_time: Mapped[Optional[str]]
    top_element: Mapped[Optional[int]]
    top_element_info: Mapped[Optional[str]]

    # Additional properties
    season: Mapped[Optional[int]]

    # Relationships
    fixtures: Mapped[List["Fixture"]] = db.relationship()  # noqa: F821

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Return the constraints that the upsert will use to identify
        conflicts"""
        return ["fpl_id", "season"]

    @classmethod
    def find_by_fpl_id(cls, fpl_id: int, season: int) -> Gameweek:
        """Return the gameweek matching the fpl_id and season"""
        return (
            db.session.query(Gameweek)
            .filter(Gameweek.fpl_id == fpl_id)
            .filter(Gameweek.season == season)
            .one_or_none()
        )
