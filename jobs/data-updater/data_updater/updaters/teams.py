"""The database updater for the team model."""

from flask import Flask
from fpl import FPL
from fpltinker.models import Configuration, Team

from data_updater.utils.db_utilities import apply_update


async def update(app: Flask, fpl: FPL) -> dict:
    """Updates the teams fom the FPL api."""
    if not (app.config.get("FLAGS", {}).get("teams")):
        return

    app.logger.debug("Updating teams.")

    api_teams = await fpl.get_teams(return_json=True)
    season = Configuration.get("season")

    # Update teams
    teams = []
    for at in api_teams:
        # Set base attributes
        t = at.copy()
        t["fpl_id"] = t["id"]
        t["season"] = season
        t.pop("id", None)

        # Generate dict and add to list
        keys = Team.__dict__.keys()
        team = {key: t[key] for key in keys if key in t}
        teams.append(team)

    apply_update(app, Team, teams)
    return teams


# Unconsumed properties returned by FPL api
# pulse_id: int
