"""The database updater for the team model"""

from flask import Flask
from fpl import FPL
from models import Configuration, Team
from sqlalchemy.exc import SQLAlchemyError


async def update(app: Flask, fpl: FPL):
    """Updates the teams fom the FPL api"""
    app.logger.debug("Updating teams.")

    fpl_teams = await fpl.get_teams(return_json=True)

    # Update teams
    teams = []
    for ft in fpl_teams:
        ft["fpl_id"] = ft["id"]
        ft["season"] = Configuration.get("season")
        team = {key: ft[key] for key in Team.__dict__.keys() if key in ft}
        teams.append(team)

    try:
        updated = Team.bulk_upsert(teams)
        app.logger.debug(
            f"Successfully updated {len(updated)} out of {Team.count()} total entries."
        )
    except SQLAlchemyError as err:
        app.logger.error(f"Failed to update teams. See error: {err}")


# Unconsumed properties returned by FPL api
# pulse_id: int
