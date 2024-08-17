"""The database updater for the player stats model"""

from flask import Flask
from fpl import FPL
from models import Configuration, Player, PlayerStats
from sqlalchemy.exc import SQLAlchemyError


async def update(app: Flask, fpl: FPL):
    """Updates the player stats fom the FPL api"""
    app.logger.debug("Updating player stats.")

    api_players = await fpl.get_players(return_json=True)
    season = Configuration.get("season")

    # Update player stats
    player_stats = []
    for p in api_players:
        # Set base attributes
        p["season"] = season

        # Set foreign key attributes
        p["player_id"] = Player.find(fpl_id=p["id"], season=season).id

        # Generate dict and add to list
        keys = PlayerStats.__dict__.keys()
        stat = {key: p[key] for key in keys if key in p}
        player_stats.append(stat)

    try:
        updated = PlayerStats.bulk_upsert(player_stats)
        app.logger.debug(
            f"Successfully updated {len(updated)} out of "
            f"{PlayerStats.count()} total entries."
        )
    except SQLAlchemyError as err:
        PlayerStats.rollback()
        app.logger.error(f"Failed to update player stats. See error: {err}")


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
