import os

from flask import Flask
from flask_migrate import Migrate

from config import CONFIGURATION

from .models import db


def create_app(run_mode=os.getenv("FLASK_ENV", "production")):
    app = Flask(__name__)
    app.config.from_object(CONFIGURATION[run_mode])
    db.init_app(app)

    Migrate(app, db)
    return app
