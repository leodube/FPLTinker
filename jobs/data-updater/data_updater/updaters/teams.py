"""The database updater for the team model"""

from flask import Flask
from fpl import FPL
from models import Configuration, Team
from sqlalchemy.exc import SQLAlchemyError


async def update(app: Flask, fpl: FPL):
    """Updates the teams fom the FPL api"""
    app.logger.debug("Updating teams.")

    api_teams = await fpl.get_teams(return_json=True)
    season = Configuration.get("season")

    # Update teams
    teams = []
    for t in api_teams:
        # Set base attributes
        t["fpl_id"] = t["id"]
        t["season"] = season

        # Generate dict and add to list
        keys = Team.__dict__.keys()
        team = {key: t[key] for key in keys if key in t}
        teams.append(team)

    try:
        updated = Team.bulk_upsert(teams)
        app.logger.debug(
            f"Successfully updated {len(updated)} out of {Team.count()} total entries."
        )
    except SQLAlchemyError as err:
        Team.rollback()
        app.logger.error(f"Failed to update teams. See error: {err}")


# Unconsumed properties returned by FPL api
# pulse_id: int
