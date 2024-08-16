"""The database updater for the team model"""

from fpl import FPL
from models import Configuration, Team

from .utils.date_utilities import is_today


async def update(fpl: FPL):
    """Updates the teams fom the FPL api"""
    # Return if updater already ran today
    if (last_updated := Team.last_updated()) and is_today(last_updated):
        return

    fpl_teams = await fpl.get_teams(return_json=True)

    # Update teams
    teams = []
    for ft in fpl_teams:
        ft["fpl_id"] = ft["id"]
        ft["season"] = Configuration.get("season")
        team = {key: ft[key] for key in Team.__dict__.keys() if key in ft}
        teams.append(team)
    Team.bulk_upsert(teams)


# Unconsumed properties returned by FPL api
# pulse_id: int
