"""The database updater for the stat details model"""

from models import PlayerStats, StatDetails

from .utils.date_utilities import is_today
from .utils.stat_details import get_stat_details


def update():
    """Updates the stat details"""
    # Return if updater already ran today
    if (last_updated := StatDetails.last_updated()) and is_today(last_updated):
        return

    stat_names = PlayerStats.__dict__.keys()

    # Update stat details
    stat_details = []
    for sn in stat_names:
        if details_dict := get_stat_details(sn):
            stat_details.append({"name": sn, **details_dict})
    StatDetails.bulk_upsert(stat_details)
