"""Description"""

from dataclasses import field
from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db

DEFAULT_SEASON: int = 20232024
STATUS_DETAILS: dict = {
    "a": "available",
    "d": "doubtful",
    "i": "injured",
    "s": "suspended",
    "u": "unavailable",
}


class Player(Base):
    """Description"""

    __versioned__ = {}
    __tablename__ = "players"

    # FPL api properties
    fpl_id: Mapped[int]
    code: Mapped[int]
    first_name: Mapped[str]
    second_name: Mapped[str]
    web_name: Mapped[str]
    squad_number: Mapped[int]
    team: Mapped[int]
    team_code: Mapped[int]
    element_type: Mapped[int]  # player position
    status: Mapped[str]  # whether available (a), not (u), injured (d)
    news: Mapped[str]
    news_added: Mapped[Optional[bool]]
    penalties_order: Mapped[int]
    chance_of_playing_next_round: Mapped[Optional[int]]
    chance_of_playing_this_round: Mapped[Optional[int]]
    corners_and_indirect_freekicks_order: Mapped[Optional[int]]
    corners_and_indirect_freekicks_text: Mapped[Optional[str]]
    direct_freekicks_order: Mapped[int]
    direct_freekicks_text: Mapped[str]

    # Unused properties returned by FPL api
    penalties_text: str

    # Additional properties
    season: Mapped[int] = mapped_column(init=False, default=DEFAULT_SEASON)

    # Relationships
    stats: Mapped[List["Stats"]] = db.relationship()

    # Methods
    @classmethod
    def index_constraints(cls):
        """Description"""
        return ["code"]

    @classmethod
    def find_by_fpl_id(cls, fpl_id: int = None, season: int = DEFAULT_SEASON):
        """Return the player matching the fpl_id and season"""
        return (
            db.session.query(Player)
            .filter(Player.fpl_id == fpl_id)
            .filter(Player.season == season)
            .one_or_none()
        )