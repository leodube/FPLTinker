"""The database updater for the fixture model"""

import json

from fpl import FPL
from models import Fixture, Gameweek, Team

from .utils.date_utilities import is_today


async def update(fpl: FPL):
    """Updates the fixtures fom the FPL api"""
    # Return if updater already ran today
    if (last_updated := Fixture.last_updated()) and is_today(last_updated):
        return

    # FUTURE: fdr = await fpl.FDR()
    fpl_fixtures = await fpl.get_fixtures(return_json=True)

    # Update fixtures
    fixtures = []
    for ff in fpl_fixtures:
        ff["fpl_id"] = ff["id"]
        ff["stats"] = json.dumps(ff["stats"]) if ff["stats"] else "[]"
        ff["gameweek"] = Gameweek.find_by_fpl_id(ff["event"]).id
        ff["team_a"] = Team.find_by_fpl_id(ff["team_a"]).id
        ff["team_h"] = Team.find_by_fpl_id(ff["team_h"]).id
        fixture = {key: ff[key] for key in Fixture.__dict__.keys() if key in ff}
        fixtures.append(fixture)
    Fixture.bulk_upsert(fixtures)


# Unconsumed properties returned by FPL api
# stats: list  # FUTURE: create fixture_stats model to store these stats
