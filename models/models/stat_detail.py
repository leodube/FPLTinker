"""Description"""

from sqlalchemy.orm import Mapped

from .base import Base
from .db import db


class StatDetails(Base):
    """Description"""

    __versioned__ = {}
    __tablename__ = "stat_details"

    # Properties
    name: Mapped[str]
    label: Mapped[str]
    description: Mapped[str]
