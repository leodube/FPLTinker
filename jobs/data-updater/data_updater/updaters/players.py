"""The database updater for the player model"""

from fpl import FPL
from models import Configuration, Player, Position, Team

from .utils.date_utilities import is_today
from pprint import pprint


async def update(fpl: FPL):
    """Updates the players fom the FPL api"""
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
    Player.bulk_upsert(players)


# Unconsumed properties returned by FPL api
# penalties_text: str
