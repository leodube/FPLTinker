"""The database updater for the gameweek model"""

from fpl import FPL
from models import Gameweek


async def update(fpl: FPL):
    """Updates the gameweeks fom the FPL api"""
    fpl_gameweeks = await fpl.get_gameweeks(include_live=True, return_json=True)
    for fg in fpl_gameweeks:
        fg["fpl_id"] = fg.pop("id")
    Gameweek.bulk_upsert(fpl_gameweeks)
