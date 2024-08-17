"""The database updater for the gameweek model"""

from flask import Flask
from fpl import FPL
from models import Configuration, Gameweek, Player
from sqlalchemy.exc import SQLAlchemyError


async def update(app: Flask, fpl: FPL):
    """Updates the gameweeks fom the FPL api"""
    app.logger.debug("Updating gameweeks.")

    api_gameweeks = await fpl.get_gameweeks(include_live=True, return_json=True)
    season = Configuration.get("season")

    # Update gameweeks
    gameweeks = []
    for g in api_gameweeks:
        # Set base attributes
        g["fpl_id"] = g["id"]
        g["season"] = season

        # Set foreign key attributes
        g["top_player_id"] = None
        if g["top_element"]:
            g["top_player_id"] = Player.find(
                fpl_id=g["top_element"], season=season
            ).id

        # Generate dict and add to list
        keys = Gameweek.__dict__.keys()
        gameweek = {key: g[key] for key in keys if key in g}
        gameweeks.append(gameweek)

    try:
        updated = Gameweek.bulk_upsert(gameweeks)
        app.logger.debug(
            f"Successfully updated {len(updated)} out of "
            f"{Gameweek.count()} total entries."
        )
    except SQLAlchemyError as err:
        Gameweek.rollback()
        app.logger.error(f"Failed to update gameweeks. See error: {err}")


# Unconsumed properties returned by FPL api
# elements: dict  # FUTURE: consider capturing the live stats
# cup_leagues_created: bool
# chip_plays: Optional[any]
# deadline_time_epoch: int
# deadline_time_game_offset: int
# h2h_ko_matches_created: bool
