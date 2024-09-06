"""Base model"""

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Mapped, mapped_column

from .db import db, intpk, timestamp


class WithTimestamps(db.Model):  # pylint: disable=too-few-public-methods
    """Adds timestamps to any subclass that inherits it."""

    __abstract__ = True

    # Timestamp properties
    created_at: Mapped[timestamp] = mapped_column(init=False, sort_order=99)
    updated_at: Mapped[timestamp] = mapped_column(init=False, sort_order=99)

    @classmethod
    def last_updated(cls) -> datetime:
        """Get the datestamp of the most recently updated entry."""
        stmt = select(cls.updated_at).order_by(cls.updated_at.desc())
        return db.session.scalar(stmt)


class Base(db.Model):
    """The base model adds general properties and methods."""

    __abstract__ = True

    # Base properties
    id: Mapped[intpk] = mapped_column(init=False, sort_order=-2)

    # Base methods
    def save(self):
        """Save the object to the database."""
        db.session.add(self)
        db.session.commit()

    def update(self, index_constraints, **kwargs):
        """Update the object attributes."""
        for key, value in kwargs.items():
            if key not in index_constraints:
                setattr(self, key, value)

    def delete(self):
        """Delete the object from the database."""
        db.session.delete(self)
        db.session.commit()

    # Base class methods
    @classmethod
    def all(cls):
        """Get all entries for the object."""
        return db.session.scalars(select(cls)).all()

    @classmethod
    def count(cls, **kwargs):
        """Count the number of entries that match the passed args."""
        return len(cls.find_all(**kwargs).all())

    @classmethod
    def find(cls, **kwargs):
        """Find a single entry that matches the passed args."""
        return cls.find_all(**kwargs).first()

    @classmethod
    def find_instance(cls, obj):
        """Find a single entry if the object passed already exists in the db."""
        stmt = select(cls)
        for constraint in cls.index_constraints():
            stmt = stmt.where(getattr(cls, constraint) == getattr(obj, constraint))
        return db.session.scalar(stmt)

    @classmethod
    def find_all(cls, **kwargs):
        """Find all entries that match the passed args."""
        stmt = select(cls)
        for key, value in kwargs.items():
            stmt = stmt.where(getattr(cls, key) == value)
        return db.session.scalars(stmt)

    @classmethod
    def index_constraints(cls) -> list:
        """Returns the constraints that the upsert will use to identify
        conflicts"""
        return ["id"]

    @classmethod
    def rollback(cls):
        """Rollback any pending changes."""
        db.session.rollback()
