"""Data updater job worker functionality is contained here."""

import aiohttp
from flask import Flask
from fpl import FPL

from data_updater.updaters import (
    configurations,
    fixture_stats,
    fixtures,
    gameweeks,
    player_stats,
    players,
    positions,
    stat_details,
    teams,
)


async def run(app: Flask):
    """Run the data updater worker"""
    async with aiohttp.ClientSession() as session:
        app.logger.debug("Running data updater.")
        fpl = FPL(session)
        await configurations.update(app, fpl)
        stat_details.update(app)
        await teams.update(app, fpl)
        await positions.update(app, fpl)
        await players.update(app, fpl)
        await player_stats.update(app, fpl)
        await gameweeks.update(app, fpl)
        await fixtures.update(app, fpl)
        await fixture_stats.update(app, fpl)
        app.logger.debug("Finished running data updater.")
