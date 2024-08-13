"""The database updater for the player stats model"""

from fpl import FPL
from models import Player, PlayerStats


async def update(fpl: FPL):
    """Updates the player stats fom the FPL api"""
    fpl_players = await fpl.get_players(return_json=True)

    # Update stats
    stats = []
    for fp in fpl_players:
        stat = {
            key: fp[key] for key in PlayerStats.__dict__.keys() if key in fp
        }
        stat["player_id"] = Player.find_by_fpl_id(fp["id"]).id
        stats.append(stat)
    PlayerStats.bulk_upsert(stats)
