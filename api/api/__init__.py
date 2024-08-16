"""The FPL Tinker API service."""

from flask import Flask
from models import db

from api.config import Config

from .resources import blueprint


def create_app():
    """Return a configured Flask App using the Factory method."""
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(blueprint)
    return app
