"""The database updater for the player stats model"""

from fpl import FPL
from models import Configuration, Player, PlayerStats

from .utils.date_utilities import is_today


async def update(fpl: FPL):
    """Updates the player stats fom the FPL api"""
    # Return if updater already ran today
    if (last_updated := PlayerStats.last_updated()) and is_today(last_updated):
        return

    fpl_players = await fpl.get_players(return_json=True)

    # Update player stats
    player_stats = []
    for fp in fpl_players:
        fp["season"] = Configuration.get("season")
        stat = {
            key: fp[key] for key in PlayerStats.__dict__.keys() if key in fp
        }
        stat["player_id"] = Player.find(fpl_id=fp["id"], season=fp["season"]).id
        player_stats.append(stat)
    PlayerStats.bulk_upsert(player_stats)


# Unconsumed properties returned by FPL api
# creativity_rank: int  # FUTURE: create own ranking script
# creativity_rank_type: int  # ranking by player type (position)
# ep_next: str
# ep_this: Optional[str]
# form_rank: int
# form_rank_type: int
# ict_index_rank: int
# ict_index_rank_type: int
# in_dreamteam: bool
# influence_rank: int
# influence_rank_type: int
# now_cost_rank: int
# now_cost_rank_type: int
# points_per_game_rank: int
# points_per_game_rank_type: int
# selected_rank: int
# selected_rank_type: int
# special: int  # for shirt mode, generally unused
# threat_rank: int
# threat_rank_type: int
