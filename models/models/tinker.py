"""Tinker model"""

from .base import Base
from .db import db


class Tinker(Base):
    """Description"""

    __versioned__ = {}
    __tablename__ = "tinkers"
