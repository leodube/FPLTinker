"""The database updater for the fixture model"""

from flask import Flask
from fpl import FPL
from models import Configuration, Fixture, Gameweek, Team
from sqlalchemy.exc import SQLAlchemyError


async def update(app: Flask, fpl: FPL):
    """Updates the fixtures fom the FPL api"""
    app.logger.debug("Updating fixtures.")

    # FUTURE: fdr = await fpl.FDR()
    fpl_fixtures = await fpl.get_fixtures(return_json=True)
    season = Configuration.get("season")

    # Update fixtures
    fixtures = []
    for ff in fpl_fixtures:
        # Set base attributes
        ff["fpl_id"] = ff["id"]
        ff["season"] = season

        # Set foreign key attributes
        ff["gameweek_id"] = Gameweek.find(fpl_id=ff["event"], season=season).id
        ff["team_a_id"] = Team.find(fpl_id=ff["team_a"], season=season).id
        ff["team_h_id"] = Team.find(fpl_id=ff["team_h"], season=season).id

        # Generate dict
        keys = Fixture.__dict__.keys()
        fixture = {key: ff[key] for key in keys if key in ff}

        # Delete conflicts
        del fixture["stats"]

        # Add to list
        fixtures.append(fixture)
    try:
        updated = Fixture.bulk_upsert(fixtures)
        app.logger.debug(
            f"Successfully updated {len(updated)} out of "
            f"{Fixture.count()} total entries."
        )
    except SQLAlchemyError as err:
        Fixture.rollback()
        app.logger.error(f"Failed to update fixtures. See error: {err}")
