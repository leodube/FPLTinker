"""Data updater job worker functionality is contained here."""

import os

import aiohttp
from flask import Flask
from fpl import FPL
from models import db

from data_updater.config import Config
from data_updater.updaters import fixtures, players, teams


def create_app():
    """Return a configured Flask App using the Factory method."""
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app


async def run(app: Flask):
    """Description"""
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        # await teams.update(fpl)
        # await fixtures.update(fpl)
        await players.update(fpl)
