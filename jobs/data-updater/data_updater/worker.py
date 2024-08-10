"""Data updater job worker functionality is contained here."""
import os

from data_update.updaters import fixtures, player_stats, players, teams
from flask import Flask
from models import db

from data_updater.config import Config


def create_app():
    """Return a configured Flask App using the Factory method."""
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app


async def run(app: Flask):
    """Description"""
    with app.app_context():
        print('run')