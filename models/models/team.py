"""Team model"""

from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db


class Team(Base):
    """A class representing a team in Fantasy Premier League."""

    __versioned__ = {}
    __tablename__ = "teams"

    # FPL api properties
    fpl_id: Mapped[int] = mapped_column(unique=True, sort_order=-1)
    code: Mapped[int] = mapped_column(unique=True, sort_order=-1)
    name: Mapped[str]
    short_name: Mapped[str]
    position: Mapped[int]
    points: Mapped[int]
    played: Mapped[int]
    win: Mapped[int]
    draw: Mapped[int]
    loss: Mapped[int]
    form: Mapped[Optional[int]]
    strength: Mapped[int]
    team_division: Mapped[Optional[int]]
    unavailable: Mapped[bool]
    strength_overall_home: Mapped[int]
    strength_overall_away: Mapped[int]
    strength_attack_home: Mapped[int]
    strength_attack_away: Mapped[int]
    strength_defence_home: Mapped[int]
    strength_defence_away: Mapped[int]

    # Relationships
    players: Mapped[List["Player"]] = db.relationship(
        back_populates="team"
    )  # noqa: F821

    # Additional properties
    season: Mapped[Optional[int]]

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Return the constraints that the upsert will use to identify
        conflicts"""
        return ["code"]
