"""Data updater job worker functionality is contained here."""

import aiohttp
from flask import Flask
from fpl import FPL
from models import db

from data_updater.config import Config
from data_updater.updaters import (
    configurations,
    fixtures,
    gameweeks,
    player_stats,
    players,
    positions,
    stat_details,
    teams,
)


def create_app():
    """Return a configured Flask App using the Factory method."""
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app


async def run():
    """Run the data updater worker"""
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        await configurations.update(fpl)
        await teams.update(fpl)
        await gameweeks.update(fpl)
        await fixtures.update(fpl)
        await positions.update(fpl)
        await players.update(fpl)
        await player_stats.update(fpl)
        stat_details.update()
