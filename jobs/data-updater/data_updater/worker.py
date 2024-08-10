"""Data updater job worker functionality is contained here."""
import os

from flask import Flask

from data_updater.config import Config
from models import db


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