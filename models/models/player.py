"""Player model"""

from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db


class Player(Base):
    """A class representing a player in Fantasy Premier League."""

    __versioned__ = {}
    __tablename__ = "players"

    # FPL api properties
    fpl_id: Mapped[int] = mapped_column(sort_order=-1)
    code: Mapped[int] = mapped_column(unique=True, sort_order=-1)
    first_name: Mapped[str]
    second_name: Mapped[str]
    web_name: Mapped[str]
    squad_number: Mapped[Optional[int]]
    team_code: Mapped[int]
    status: Mapped[str]
    news: Mapped[str]
    news_added: Mapped[Optional[str]]
    penalties_order: Mapped[Optional[int]]
    chance_of_playing_next_round: Mapped[Optional[int]]
    chance_of_playing_this_round: Mapped[Optional[int]]
    corners_and_indirect_freekicks_order: Mapped[Optional[int]]
    corners_and_indirect_freekicks_text: Mapped[Optional[str]]
    direct_freekicks_order: Mapped[Optional[int]]
    direct_freekicks_text: Mapped[Optional[str]]

    # Additional properties
    season: Mapped[Optional[int]]

    # Foreign keys
    team: Mapped[int] = mapped_column(db.ForeignKey("teams.id"), sort_order=-1)
    position: Mapped[int] = mapped_column(
        db.ForeignKey("positions.id"), sort_order=-1
    )

    # Relationships
    stats: Mapped[List["PlayerStats"]] = db.relationship()  # noqa: F821

    # Methods
    @classmethod
    def index_constraints(cls):
        """Return the constraints that the upsert will use to identify
        conflicts"""
        return ["code"]

    @classmethod
    def find_by_fpl_id(cls, fpl_id: int, season: int):
        """Return the player matching the fpl_id and season"""
        return (
            db.session.query(Player)
            .filter(Player.fpl_id == fpl_id)
            .filter(Player.season == season)
            .one_or_none()
        )
