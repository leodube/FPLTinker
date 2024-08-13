"""Weighting Model"""

from .base import Base


class Weighting(Base):
    """A class containing the user-defined stat weightings."""

    __versioned__ = {}
    __tablename__ = "weightings"
