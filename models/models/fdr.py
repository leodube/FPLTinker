"""FDR model"""

from __future__ import annotations

from enum import Enum, auto
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, WithTimestamps
from .db import db, stat


class FDR(Base, WithTimestamps):
    """A class representing a Fixture Difficulty Ranking in Fantasy Premier League."""

    __tablename__ = "fdr"
    __table_args__ = (db.UniqueConstraint("team_id", "type"),)

    class FDRTypes(Enum):
        """Enum of the FDR types."""

        ALL = auto()
        GOALKEEPER = auto()
        DEFENDER = auto()
        MIDFIELDER = auto()
        FORWARD = auto()

        @classmethod
        def list(cls):
            """Returns the enum as a list"""
            return list(map(lambda c: c, cls))

    # FPL api properties
    team_name: Mapped[str]
    _type: Mapped[FDRTypes] = mapped_column("type")
    home: Mapped[stat]
    away: Mapped[stat]

    # Foreign Keys
    team_id: Mapped[int] = mapped_column(db.ForeignKey("teams.id"), sort_order=-1)

    # Additional properties
    season: Mapped[Optional[int]]

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Returns the constraints that the upsert will use to identify
        conflicts"""
        return ["team_id", "_type"]
