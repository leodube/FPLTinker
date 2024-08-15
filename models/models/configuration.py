"""Configuration model"""

from enum import Enum, auto
from typing import Optional

from sqlalchemy import event
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db


class Configuration(Base):
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
    def index_constraints(cls):
        """Return the constraints that the upsert will use to identify
        conflicts"""
        return ["name"]

    @classmethod
    def find_by_name(cls, name: str):
        """Return the configuration matching the name"""
        return (
            db.session.query(Configuration)
            .filter(Configuration.name == name)
            .one_or_none()
        )

    @classmethod
    def get_value_for(cls, name: str):
        """Return the value in the correct type for the configuration matching
        the name."""
        if not (
            config := (
                db.session.query(Configuration)
                .filter(Configuration.name == name)
                .one_or_none()
            )
        ):
            return None
        return cls.cast_value(config.value, config._type)

    # TODO: validate value and type before insert/update
    def validate_value(self):
        """Ensure the value is the correct type before insert or update."""
        Configuration.cast_value(self.value, self._type)

    @staticmethod
    def cast_value(cls, value: str, _type: str):
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
                    f"Cannot cast _type {type}. Make sure the type exists in the ConfigurationTypes enum."
                )
