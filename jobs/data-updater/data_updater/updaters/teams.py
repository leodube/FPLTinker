"""The database updater for the team model."""

from flask import Flask
from fpl import FPL
from models import Configuration, Team

from data_updater.utils.db_utilities import apply_update


async def update(app: Flask, fpl: FPL):
    """Updates the teams fom the FPL api."""
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

    apply_update(app, Team, teams)


# Unconsumed properties returned by FPL api
# pulse_id: int
