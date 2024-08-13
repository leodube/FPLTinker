"""Description"""

import json

from fpl import FPL
from models import Team


async def update(fpl: FPL):
    """Description"""
    fpl_teams = await fpl.get_teams(return_json=True)
    for ft in fpl_teams:
        ft["fpl_id"] = ft.pop("id")
    Team.bulk_upsert(fpl_teams)
