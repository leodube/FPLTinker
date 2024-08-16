"""The database updater for the fixture model"""

import json

from fpl import FPL
from models import Configuration, Fixture, Gameweek, Team

from .utils.date_utilities import is_today


async def update(fpl: FPL):
    """Updates the fixtures fom the FPL api"""
    # FUTURE: fdr = await fpl.FDR()
    fpl_fixtures = await fpl.get_fixtures(return_json=True)

    # Update fixtures
    fixtures = []
    for ff in fpl_fixtures:
        ff["fpl_id"] = ff["id"]
        ff["stats"] = json.dumps(ff["stats"]) if ff["stats"] else "[]"
        ff["season"] = Configuration.get("season")
        ff["gameweek_id"] = Gameweek.find(
            fpl_id=ff["event"], season=ff["season"]
        ).id
        ff["team_a_id"] = Team.find(fpl_id=ff["team_a"], season=ff["season"]).id
        ff["team_h_id"] = Team.find(fpl_id=ff["team_h"], season=ff["season"]).id
        fixture = {key: ff[key] for key in Fixture.__dict__.keys() if key in ff}
        fixtures.append(fixture)
    Fixture.bulk_upsert(fixtures)


# Unconsumed properties returned by FPL api
# stats: list  # FUTURE: create fixture_stats model to store these stats
