"""Contains database helper methods"""

from pprint import pprint
from typing import List, TypeVar

from flask import Flask
from models import Base
from sqlalchemy.exc import SQLAlchemyError

BaseModelType = TypeVar("BaseModelType", bound=Base)


def apply_update(app: Flask, model: BaseModelType, entries_data: List[dict]):
    """Apply the entries to the database table."""
    try:
        db_count_before = model.count()
        num_updated = 0

        for data in entries_data:
            data.pop("id", None)
            entry = model(**data)
            if found := model.find_instance(entry):
                if found.diff(
                    entry, exclude=("id", "created_at", "updated_at")
                ):  # has updates
                    found.update(model.index_constraints(), **data)
                    found.save()
                    num_updated += 1
            else:
                entry.save()

        num_added = model.count() - db_count_before

        app.logger.debug(
            f"Successfully added {num_added} entries and "
            f"updated {num_updated}/{model.count()} entries."
        )
    except SQLAlchemyError as err:
        model.rollback()
        app.logger.error(f"Failed to update table. See error: {err}")
