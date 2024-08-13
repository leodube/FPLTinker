"""Description"""

from fpl import FPL
from models import Player, Stats
from pprint import pprint

async def update(fpl: FPL):
    """Description"""
    fpl_players = await fpl.get_players(return_json=True)

    # Update players
    players = []
    for fp in fpl_players:
        player = {key:fp[key] for key in Player.__dict__.keys() if key in fp}
        player["fpl_id"] = player.pop("id")
        players.append(player)
    Player.bulk_upsert(players)
    
    # Update stats
    stats = []
    for fp in fpl_players:
        stat = {key:fp[key] for key in Stats.__dict__.keys() if key in fp}
        player = Player.find_by_fpl_id(fp["id"])
        stat["player_id"] = player.id
        stats.append(stat)
    Stats.bulk_upsert(stats)
