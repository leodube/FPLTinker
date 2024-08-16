"""The database updater for the player model"""

from flask import Flask
from fpl import FPL
from models import Configuration, Player, Position, Team
from sqlalchemy.exc import SQLAlchemyError


async def update(app: Flask, fpl: FPL):
    """Updates the players fom the FPL api"""
    app.logger.debug("Updating players.")

    fpl_players = await fpl.get_players(return_json=True)

    # Update players
    players = []
    for fp in fpl_players:
        fp["fpl_id"] = fp["id"]
        fp["season"] = Configuration.get("season")
        fp["position_id"] = Position.find(
            fpl_id=fp["element_type"], season=fp["season"]
        ).id
        fp["team_id"] = Team.find(fpl_id=fp["team"], season=fp["season"]).id
        player = {key: fp[key] for key in Player.__dict__.keys() if key in fp}
        del player["team"]
        players.append(player)

    try:
        updated = Player.bulk_upsert(players)
        app.logger.debug(
            f"Successfully updated {len(updated)} out of {Player.count()} total entries."
        )
    except SQLAlchemyError as err:
        app.logger.error(f"Failed to update players. See error: {err}")


# Unconsumed properties returned by FPL api
# penalties_text: str
