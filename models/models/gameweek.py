"""Gameweek model"""

from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db

DEFAULT_SEASON = 20232024


class Gameweek(Base):
    """A class representing a gameweek in Fantasy Premier League."""

    __versioned__ = {}
    __tablename__ = "gameweeks"

    # FPL api properties
    fpl_id: Mapped[int]
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

    # Unused properties returned by FPL api
    cup_leagues_created: bool
    chip_plays: Optional[any]
    deadline_time_epoch: int
    deadline_time_game_offset: int
    h2h_ko_matches_created: bool

    # Additional properties
    season: Mapped[int] = mapped_column(init=False, default=DEFAULT_SEASON)

    # Relationships
    fixtures: Mapped[List["Fixture"]] = db.relationship()

    # Methods
    @classmethod
    def index_constraints(cls):
        """Description"""
        return ["fpl_id", "season"]

    @classmethod
    def find_by_fpl_id(cls, fpl_id: int, season: int = DEFAULT_SEASON):
        """Return the gameweek matching the fpl_id and season"""
        return (
            db.session.query(Gameweek)
            .filter(Gameweek.fpl_id == fpl_id)
            .filter(Gameweek.season == season)
            .one_or_none()
        )
