"""The database updater for the position model."""

from flask import Flask
from fpl import FPL
from models import Configuration, Position

from data_updater.utils.date_utilities import is_today
from data_updater.utils.db_utilities import apply_update


async def update(app: Flask, fpl: FPL):
    """Updates the positions fom the FPL api."""
    app.logger.debug("Updating positions.")

    # Return if updater already ran today
    if (last_updated := Position.last_updated()) and is_today(last_updated):
        app.logger.debug("Already updated positions today. Skipping.")
        return

    api_positions = await fpl.get_positions(return_json=True)
    season = Configuration.get("season")

    # Update positions
    positions = []
    for p in api_positions:
        # Set base attributes
        p["fpl_id"] = p["id"]
        p["season"] = season

        # Generate dict and add to list
        keys = Position.__dict__.keys()
        position = {key: p[key] for key in keys if key in p}
        positions.append(position)

    apply_update(app, Position, positions)


# Unconsumed properties returned by FPL api
# squad_min_select: bool
# squad_max_select: bool
# sub_positions_locked: list
