"""Base model"""

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Mapped, mapped_column

from .db import db, intpk, timestamp


class Base(db.Model):
    """The base model adds general properties and methods that all subclasses will use"""

    __abstract__ = True

    # Base properties
    id: Mapped[intpk] = mapped_column(init=False)
    created_date: Mapped[timestamp] = mapped_column(init=False)
    last_modified: Mapped[timestamp] = mapped_column(init=False)

    def save(self):
        """Save the object to the database."""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete the object from the database."""
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def index_constraints(cls):
        """Return the constraints that the upsert will use to identify conflicts"""
        return ["id"]

    @classmethod
    def bulk_upsert(cls, rows):
        """Insert multiple rows in the database from an array of dictionaries.
        If a conflicting entry is found, update that entry instead."""
        stmt = insert(cls).values(rows)
        stmt = stmt.on_conflict_do_update(
            index_elements=cls.index_constraints(), set_=dict(**stmt.excluded)
        ).returning(cls)
        # return db.session.scalars(stmt)
