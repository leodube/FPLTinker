"""Tinker model"""

from .base import Base, WithTimestamps


class Tinker(Base, WithTimestamps):
    """A class representing a team tinker."""

    __versioned__ = {}
    __tablename__ = "tinkers"
