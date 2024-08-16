"""The database updater for the gameweek model"""

from flask import Flask
from fpl import FPL
from models import Configuration, Gameweek
from sqlalchemy.exc import SQLAlchemyError


async def update(app: Flask, fpl: FPL):
    """Updates the gameweeks fom the FPL api"""
    app.logger.debug("Updating gameweeks.")

    fpl_gameweeks = await fpl.get_gameweeks(include_live=True, return_json=True)

    # Update gameweeks
    gameweeks = []
    for fg in fpl_gameweeks:
        fg["fpl_id"] = fg["id"]
        fg["season"] = Configuration.get("season")
        gameweek = {
            key: fg[key] for key in Gameweek.__dict__.keys() if key in fg
        }
        gameweeks.append(gameweek)
    try:
        updated = Gameweek.bulk_upsert(gameweeks)
        app.logger.debug(
            f"Successfully updated {len(updated)} out of {Gameweek.count()} total entries."
        )
    except SQLAlchemyError as err:
        app.logger.error(f"Failed to update gameweeks. See error: {err}")


# Unconsumed properties returned by FPL api
# elements: dict  # FUTURE: consider capturing the live stats
# cup_leagues_created: bool
# chip_plays: Optional[any]
# deadline_time_epoch: int
# deadline_time_game_offset: int
# h2h_ko_matches_created: bool
