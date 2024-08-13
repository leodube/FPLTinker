"""StatDetails model"""

from sqlalchemy.orm import Mapped

from .base import Base


class StatDetails(Base):
    """A class representing stat details."""

    __versioned__ = {}
    __tablename__ = "stat_details"

    # Properties
    name: Mapped[str]
    label: Mapped[str]
    description: Mapped[str]
