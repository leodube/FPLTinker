"""Contains database helper methods"""

from typing import TypeVar

from flask import Flask
from models import Base
from sqlalchemy.exc import SQLAlchemyError

FplModelClass = TypeVar("FplModelClass", bound=Base)


def apply_update(app: Flask, model: FplModelClass, items: dict):
    """Apply the items to the database table."""
    try:
        entries_before_count = model.count()

        upserted = model.bulk_upsert(items)

        num_added = model.count() - entries_before_count
        num_updated = len(upserted) - num_added

        app.logger.debug(
            f"Successfully added {num_added} entries and "
            f"updated {num_updated}/{model.count()} entries."
        )
    except SQLAlchemyError as err:
        model.rollback()
        app.logger.error(f"Failed to update table. See error: {err}")
