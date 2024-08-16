"""Exposes all of the resource endpoints mounted in Flask-Blueprint style.

Uses restplus namespaces to mount individual api endpoints into the service.
"""

from flask import Blueprint
from flask_restx import Api

from .fixture import api as fixture_api
from .gameweek import api as gameweek_api
from .player import api as player_api
from .position import api as position_api
from .stat_details import api as stat_details_api
from .team import api as team_api

__all__ = ("api", "blueprint")


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(
    blueprint,
    title="FPL TINKER API",
    version="1.0",
    description="The api for the FPL Tinker app",
)

api.add_namespace(fixture_api, path="/fixtures")
api.add_namespace(gameweek_api, path="/gameweeks")
api.add_namespace(player_api, path="/players")
api.add_namespace(position_api, path="/positions")
api.add_namespace(stat_details_api, path="/stats/details")
api.add_namespace(team_api, path="/teams")
