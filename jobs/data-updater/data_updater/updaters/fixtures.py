"""Description"""

import json

from fpl import FPL
from models import Fixture, Team


async def update(fpl: FPL):
    """Description"""
    # FUTURE: fdr = await fpl.FDR()
    fpl_fixtures = await fpl.get_fixtures(return_json=True)
    for ff in fpl_fixtures:
        ff["fpl_id"] = ff.pop("id")
        ff["gameweek"] = ff.pop("event")
        ff["stats"] = (
            json.dump(ff["stats"]) if ff["stats"] else "[]"
        )
        ff["team_a"] = Team.find_by_fpl_id(ff["team_a"])
        ff["team_h"] = Team.find_by_fpl_id(ff["team_h"])
    Fixture.bulk_upsert(fpl_fixtures)
