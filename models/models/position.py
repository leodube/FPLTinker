"""Position model"""

from __future__ import annotations

from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db


class Position(Base):
    """A class representing a player's position in Fantasy Premier League."""

    __versioned__ = {}
    __tablename__ = "positions"

    # FPL api properties
    fpl_id: Mapped[int] = mapped_column(sort_order=-1)
    plural_name: Mapped[str]
    plural_name_short: Mapped[str]
    singular_name: Mapped[str]
    singular_name_short: Mapped[str]
    squad_select: Mapped[int]
    squad_min_play: Mapped[int]
    squad_max_play: Mapped[int]
    ui_shirt_specific: Mapped[bool]
    element_count: Mapped[int]

    # Additional properties
    season: Mapped[Optional[int]]

    # Relationships
    players: Mapped[List["Player"]] = db.relationship()  # noqa: F821
