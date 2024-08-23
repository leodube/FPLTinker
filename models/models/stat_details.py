"""StatDetails model"""

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class StatDetails(Base):
    """A class representing stat details."""

    __tablename__ = "stat_details"

    # Properties
    name: Mapped[str] = mapped_column(unique=True)
    label: Mapped[str]
    description: Mapped[str]

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Return the constraints that the upsert will use to identify
        conflicts"""
        return ["name"]
