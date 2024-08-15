"""The database updater for the player model"""

from fpl import FPL
from models import Configuration, Player, Position, Team

from .utils.date_utilities import is_today


async def update(fpl: FPL):
    """Updates the players fom the FPL api"""
    # Return if updater already ran today
    if (last_updated := Player.last_updated()) and is_today(last_updated):
        return

    fpl_players = await fpl.get_players(return_json=True)

    # Update players
    players = []
    for fp in fpl_players:
        fp["fpl_id"] = fp["id"]
        fp["season"] = Configuration.get_value_for(name="season")
        fp["position"] = Position.find_by_fpl_id(
            fp["element_type"], fp["season"]
        ).id
        fp["team"] = Team.find_by_fpl_id(fp["team"], fp["season"]).id
        player = {key: fp[key] for key in Player.__dict__.keys() if key in fp}
        players.append(player)
    Player.bulk_upsert(players)


# Unconsumed properties returned by FPL api
# penalties_text: str
