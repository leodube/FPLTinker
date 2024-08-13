"""Tinker model"""

from .base import Base


class Tinker(Base):
    """A class representing a team tinker."""

    __versioned__ = {}
    __tablename__ = "tinkers"
