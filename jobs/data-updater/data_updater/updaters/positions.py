"""The database updater for the position model"""

from fpl import FPL
from models import Position
from .utils.date_utilities import is_today


async def update(fpl: FPL):
    """Updates the positions fom the FPL api"""
    # Return if updater already ran today
    if((last_updated := Position.last_updated()) and is_today(last_updated)):
        return

    fpl_positions = await fpl.get_positions(return_json=True)

    # Update positions
    positions = []
    for fp in fpl_positions:
        fp["fpl_id"] = fp["id"]
        position = {
            key: fp[key] for key in Position.__dict__.keys() if key in fp
        }
        positions.append(position)
    Position.bulk_upsert(positions)


# Unconsumed properties returned by FPL api
# squad_min_select: bool
# squad_max_select: bool
# sub_positions_locked: list
