"""Player model"""

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, WithTimestamps
from .db import db


class Player(Base, WithTimestamps):
    """A class representing a player in Fantasy Premier League."""

    __tablename__ = "players"

    class PlayerStatuses(Enum):
        """Enum of the player statuses."""

        AVAILABLE = "a"
        DOUBTFUL = "d"
        INJURED = "i"
        NOT_ELIGIBLE = "n"
        SUSPENDED = "s"
        UNAVAILABLE = "u"

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
    team_id: Mapped[int] = mapped_column(db.ForeignKey("teams.id"), sort_order=-1)
    position_id: Mapped[int] = mapped_column(
        db.ForeignKey("positions.id"), sort_order=-1
    )

    # Relationships
    stats: Mapped[List["PlayerStats"]] = db.relationship(
        back_populates="player", init=False
    )
    position: Mapped["Position"] = db.relationship(
        back_populates="players", viewonly=True, init=False
    )
    team: Mapped["Team"] = db.relationship(
        back_populates="players", viewonly=True, init=False
    )

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Return the constraints that the upsert will use to identify
        conflicts"""
        return ["code"]
