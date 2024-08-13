"""The database updater for the position model"""

from fpl import FPL
from models import Position


async def update(fpl: FPL):
    """Updates the positions fom the FPL api"""
    fpl_positions = await fpl.get_positions(return_json=True)
    for fp in fpl_positions:
        fp["fpl_id"] = fp.pop("id")
    Position.bulk_upsert(fpl_positions)
