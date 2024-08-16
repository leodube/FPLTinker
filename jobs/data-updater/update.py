"""Data importer job"""

import asyncio
import logging.config
import sys
from os import path

from flask import Flask
from models import db

from data_updater.config import Config
from data_updater.worker import run


def create_app():
    """Return a configured Flask App using the Factory method."""
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app


def setup_logging():
    """Create the services logger."""
    conf = path.join(path.abspath(path.dirname(__file__)), "logging.conf")
    if conf and path.isfile(conf):
        logging.config.fileConfig(conf)
        print("Configure logging, from conf:{}".format(conf), file=sys.stdout)
    else:
        print(
            "Unable to configure logging, attempted conf:{}".format(conf),
            file=sys.stderr,
        )


if __name__ == "__main__":
    setup_logging()
    app = create_app()
    with app.app_context():
        asyncio.run(run(app))
