"""The database updater for the fixture model"""

import json

from fpl import FPL
from models import Fixture, Gameweek, Team


async def update(fpl: FPL):
    """Updates the fixtures fom the FPL api"""
    # FUTURE: fdr = await fpl.FDR()
    fpl_fixtures = await fpl.get_fixtures(return_json=True)
    for ff in fpl_fixtures:
        ff["fpl_id"] = ff.pop("id")
        ff["stats"] = json.dump(ff["stats"]) if ff["stats"] else "[]"
        ff["gameweek"] = Gameweek.find_by_fpl_id(ff["event"]).id
        ff["team_a"] = Team.find_by_fpl_id(ff["team_a"]).id
        ff["team_h"] = Team.find_by_fpl_id(ff["team_h"]).id
    Fixture.bulk_upsert(fpl_fixtures)
