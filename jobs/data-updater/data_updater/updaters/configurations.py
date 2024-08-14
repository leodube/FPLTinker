"""The database updater for the configuration model"""

from datetime import datetime

from fpl import FPL
from models import Configuration

from .utils.date_utilities import is_today
from .utils.config_details import get_config_details


async def update(fpl: FPL):
    """Updates the configurations"""
    # Return if updater already ran today
    if (last_updated := Configuration.last_updated()) and is_today(
        last_updated
    ):
        return

    configurations = []

    # Update current season. The FPL api will update sometime between seasons.
    # When this happens, the first gameweek will be listed as not finished.
    # This will be used as our indicator for the new season to begin.
    fpl_gameweeks = await fpl.get_gameweeks(include_live=True, return_json=True)
    if not fpl_gameweeks[0].get("finished", True):
        current_year = datetime.now().date().year
        details = get_config_details("season")
        season_config = {"name": "season", **details}
        season_config["value"] = str(current_year) + str(current_year + 1)
        configurations.append(season_config)

    Configuration.bulk_upsert(configurations)
