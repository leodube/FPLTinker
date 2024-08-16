"""The database updater for the position model"""

from flask import Flask
from fpl import FPL
from models import Configuration, Position

from .utils.date_utilities import is_today


async def update(app: Flask, fpl: FPL):
    """Updates the positions fom the FPL api"""
    app.logger.debug("Updating positions.")

    # Return if updater already ran today
    if (last_updated := Position.last_updated()) and is_today(last_updated):
        app.logger.debug("Already updated positions today. Skipping.")
        return

    fpl_positions = await fpl.get_positions(return_json=True)

    # Update positions
    positions = []
    for fp in fpl_positions:
        fp["fpl_id"] = fp["id"]
        fp["season"] = Configuration.get("season")
        position = {
            key: fp[key] for key in Position.__dict__.keys() if key in fp
        }
        positions.append(position)
    updated = Position.bulk_upsert(positions)
    app.logger.debug(
        f"Successfully updated {len(updated)} out of {Position.count()} total entries."
    )


# Unconsumed properties returned by FPL api
# squad_min_select: bool
# squad_max_select: bool
# sub_positions_locked: list
