"""Team model"""

from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, WithTimestamps
from .db import db


class Team(Base, WithTimestamps):
    """A class representing a team in Fantasy Premier League."""

    __tablename__ = "teams"

    # Serializer config
    serialize_rules = (
        "-id",
        "-created_at",
        "-updated_at",
        "-players",
    )

    # FPL api properties
    fpl_id: Mapped[int] = mapped_column(sort_order=-1)
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
        back_populates="team", init=False, repr=False
    )

    # Additional properties
    season: Mapped[Optional[int]]

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Returns the constraints that the upsert will use to identify
        conflicts"""
        return ["code"]
