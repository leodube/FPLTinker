"""Configuration model"""

from __future__ import annotations

from enum import Enum, auto
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, WithTimestamps
from .db import db


class Configuration(Base, WithTimestamps):
    """A class representing a configuration for the application."""

    __versioned__ = {}
    __tablename__ = "configurations"

    class ConfigurationTypes(Enum):
        """Enum of the configuration types."""

        BOOLEAN = auto()
        STRING = auto()
        INTEGER = auto()

    name: Mapped[str] = mapped_column(unique=True)
    value: Mapped[str]
    _type: Mapped[ConfigurationTypes] = mapped_column("type")
    description: Mapped[Optional[str]]

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Return the constraints that the upsert will use to identify
        conflicts"""
        return ["name"]

    @classmethod
    def get(cls, name: str) -> any:
        """Return the value in the correct type for the configuration matching
        the name."""
        if not (config := cls.find_by_name(name)):
            return None
        return cls.cast_value(
            config.value, config._type  # pylint: disable=protected-access
        )

    @classmethod
    def find_by_name(cls, name: str) -> Configuration:
        """Return the configuration matching the name"""
        return (
            db.session.query(Configuration)
            .filter(Configuration.name == name)
            .one_or_none()
        )

    @classmethod
    def cast_value(cls, value: str, _type: ConfigurationTypes) -> any:
        """Cast the value to the correct type."""
        match _type:
            case cls.ConfigurationTypes.BOOLEAN:
                return bool(value)
            case cls.ConfigurationTypes.INTEGER:
                return int(value)
            case cls.ConfigurationTypes.STRING:
                return value
            case _:
                raise ValueError(
                    (
                        f"Cannot cast type {_type}. Make sure the type exists "
                        "in the ConfigurationTypes enum."
                    )
                )
