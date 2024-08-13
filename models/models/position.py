"""Position model"""

from typing import List

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db

DEFAULT_SEASON = 20232024


class Position(Base):
    """A class representing a player's position in Fantasy Premier League."""

    __versioned__ = {}
    __tablename__ = "positions"

    # FPL api properties
    fpl_id: Mapped[int]
    plural_name: Mapped[str]
    plural_name_short: Mapped[str]
    singular_name: Mapped[str]
    singular_name_short: Mapped[str]
    squad_select: Mapped[int]
    squad_min_play: Mapped[int]
    squad_max_play: Mapped[int]
    ui_shirt_specific: Mapped[bool]
    element_count: Mapped[int]

    # Unused properties returned by FPL api
    squad_min_select: bool
    squad_max_select: bool
    sub_positions_locked: list

    # Additional properties
    season: Mapped[int] = mapped_column(init=False, default=DEFAULT_SEASON)

    # Relationships
    players: Mapped[List["Player"]] = db.relationship()

    @classmethod
    def find_by_fpl_id(cls, fpl_id: int, season: int = DEFAULT_SEASON):
        """Return the team matching the fpl_id and season"""
        return (
            db.session.query(Position)
            .filter(Position.fpl_id == fpl_id)
            .filter(Position.season == season)
            .one_or_none()
        )
