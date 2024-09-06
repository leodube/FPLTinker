"""The database updater for the fixture model."""

from flask import Flask
from fpl import FPL
from models import Configuration, Fixture, Gameweek, Team

from data_updater.utils.db_utilities import apply_update


async def update(app: Flask, fpl: FPL):
    """Updates the fixtures fom the FPL api."""
    app.logger.debug("Updating fixtures.")

    # FUTURE: fdr = await fpl.FDR()
    api_fixtures = await fpl.get_fixtures(return_json=True)
    season = Configuration.get("season")

    # Update fixtures
    fixtures = []
    for f in api_fixtures:
        # Set base attributes
        f["fpl_id"] = f["id"]
        f["season"] = season

        # Set foreign key attributes
        f["gameweek_id"] = Gameweek.find(fpl_id=f["event"], season=season).id
        f["team_a_id"] = Team.find(fpl_id=f["team_a"], season=season).id
        f["team_h_id"] = Team.find(fpl_id=f["team_h"], season=season).id

        # Generate dict
        keys = Fixture.__dict__.keys()
        fixture = {key: f[key] for key in keys if key in f}

        # Delete conflicts
        del fixture["stats"]

        # Add to list
        fixtures.append(fixture)

    # Apply updates to db
    apply_update(app, Fixture, fixtures)
