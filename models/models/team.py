"""Description"""

from dataclasses import field
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db

DEFAULT_SEASON = 20232024


class Team(Base):
    """Description"""

    __versioned__ = {}
    __tablename__ = "teams"

    # FPL api properties
    fpl_id: Mapped[int]
    code: Mapped[int]
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

    # Unused properties returned by FPL api
    pulse_id: int

    # Additional properties
    season: Mapped[int] = mapped_column(init=False, default=DEFAULT_SEASON)

    # Methods
    @classmethod
    def index_constraints(cls):
        """Description"""
        return ["code"]

    @classmethod
    def find_by_fpl_id(cls, fpl_id: int = None, season: int = DEFAULT_SEASON):
        """Return the team matching the fpl_id and season"""
        return (
            db.session.query(Team)
            .filter(Team.fpl_id == fpl_id)
            .filter(Team.season == season)
            .one_or_none()
        )
