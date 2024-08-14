"""The database updater for the gameweek model"""

from fpl import FPL
from models import Gameweek

from .utils.date_utilities import is_today


async def update(fpl: FPL):
    """Updates the gameweeks fom the FPL api"""
    # Return if updater already ran today
    if (last_updated := Gameweek.last_updated()) and is_today(last_updated):
        return

    fpl_gameweeks = await fpl.get_gameweeks(include_live=True, return_json=True)

    # Update gameweeks
    gameweeks = []
    for fg in fpl_gameweeks:
        fg["fpl_id"] = fg["id"]
        gameweek = {
            key: fg[key] for key in Gameweek.__dict__.keys() if key in fg
        }
        gameweeks.append(gameweek)
    Gameweek.bulk_upsert(gameweeks)


# Unconsumed properties returned by FPL api
# elements: dict  # FUTURE: consider capturing the live stats
# cup_leagues_created: bool
# chip_plays: Optional[any]
# deadline_time_epoch: int
# deadline_time_game_offset: int
# h2h_ko_matches_created: bool
