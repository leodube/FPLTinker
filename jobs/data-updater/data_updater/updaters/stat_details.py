"""The database updater for the stat details model"""

from flask import Flask
from models import PlayerStats, StatDetails

from .utils.date_utilities import is_today
from .utils.stat_details import get_stat_details


def update(app: Flask):
    """Updates the stat details"""
    app.logger.debug("Updating stat details.")

    # Return if updater already ran today
    if (last_updated := StatDetails.last_updated()) and is_today(last_updated):
        app.logger.debug("Already updated stat details today. Skipping.")
        return

    stat_names = PlayerStats.__dict__.keys()

    # Update stat details
    stat_details = []
    for sn in stat_names:
        if details_dict := get_stat_details(sn):
            stat_details.append({"name": sn, **details_dict})
    updated = StatDetails.bulk_upsert(stat_details)
    app.logger.debug(
        f"Successfully updated {len(updated)} out of {StatDetails.count()} total entries."
    )
