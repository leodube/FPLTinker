"""Base model"""

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
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

    def save(self):
        """Save the object to the database."""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete the object from the database."""
        db.session.delete(self)
        db.session.commit()

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

    @classmethod
    def on_conflict_set(cls, vals: dict) -> dict:
        """Determines what values to update during the upsert operation.
        Generally we want to keep the id and created_at date from the
        original insert."""
        vals.pop("id", None)
        vals.pop("created_at", None)
        return vals

    @classmethod
    def bulk_upsert(cls, rows) -> list:
        """Insert multiple rows in the database from an array of dictionaries.
        If a conflicting entry is found, update that entry instead."""
        stmt = insert(cls).values(rows)
        stmt = stmt.on_conflict_do_update(
            index_elements=cls.index_constraints(),
            set_=cls.on_conflict_set({**stmt.excluded}),
        ).returning(cls)
        objs = db.session.scalars(stmt)
        db.session.commit()
        return objs.all()
