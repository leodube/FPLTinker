"""The database updater for the player model"""

from fpl import FPL
from models import Player


async def update(fpl: FPL):
    """Updates the players fom the FPL api"""
    fpl_players = await fpl.get_players(return_json=True)

    # Update players
    players = []
    for fp in fpl_players:
        fp["fpl_id"] = fp.pop("id")
        fp["position"] = fp.pop("element_type")
        player = {key: fp[key] for key in Player.__dict__.keys() if key in fp}
        players.append(player)
    Player.bulk_upsert(players)
