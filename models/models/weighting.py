"""Weighting Model"""

from .base import Base, WithTimestamps


class Weighting(Base, WithTimestamps):
    """A class containing the user-defined stat weightings."""

    __versioned__ = {}
    __tablename__ = "weightings"
