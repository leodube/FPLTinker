"""FixtureStats model"""

from .base import Base
from .db import db


class FixtureStats(Base):
    """A class representing a fixtures's stats in Fantasy Premier League."""

    __versioned__ = {}
    __tablename__ = "fixture_stats"
