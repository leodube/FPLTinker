"""The database updater for the stat details model"""

from flask import Flask
from models import PlayerStats, StatDetails
from sqlalchemy.exc import SQLAlchemyError

from .utils.stat_details import get_stat_details


def update(app: Flask):
    """Updates the stat details"""
    app.logger.debug("Updating stat details.")

    stat_names = PlayerStats.__dict__.keys()

    # Update stat details
    stat_details = []
    for sn in stat_names:
        if details_dict := get_stat_details(sn):
            stat_details.append({"name": sn, **details_dict})

    try:
        updated = StatDetails.bulk_upsert(stat_details)
        app.logger.debug(
            f"Successfully updated {len(updated)} out of "
            f"{StatDetails.count()} total entries."
        )
    except SQLAlchemyError as err:
        StatDetails.rollback()
        app.logger.error(f"Failed to update stat details. See error: {err}")
