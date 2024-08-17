"""The database updater for the player model"""

from flask import Flask
from fpl import FPL
from models import Configuration, Player, Position, Team

from .utils.db_utilities import apply_update


async def update(app: Flask, fpl: FPL):
    """Updates the players fom the FPL api"""
    app.logger.debug("Updating players.")

    api_players = await fpl.get_players(return_json=True)
    season = Configuration.get("season")

    # Update players
    players = []
    for p in api_players:
        # Set base attributes
        p["fpl_id"] = p["id"]
        p["season"] = season

        # Set foreign key attributes
        p["position_id"] = Position.find(fpl_id=p["element_type"], season=season).id
        p["team_id"] = Team.find(fpl_id=p["team"], season=season).id

        # Delete conflicts
        del p["team"]

        # Generate dict and add to list
        keys = Player.__dict__.keys()
        player = {key: p[key] for key in keys if key in p}
        players.append(player)

    # Apply updates to db
    apply_update(app, Player, players)


# Unconsumed properties returned by FPL api
# penalties_text: str
