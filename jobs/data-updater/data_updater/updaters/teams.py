"""The database updater for the team model"""

import json

from fpl import FPL
from models import Team


async def update(fpl: FPL):
    """Updates the teams fom the FPL api"""
    fpl_teams = await fpl.get_teams(return_json=True)
    for ft in fpl_teams:
        ft["fpl_id"] = ft.pop("id")
    Team.bulk_upsert(fpl_teams)
