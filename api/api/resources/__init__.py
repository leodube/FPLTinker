"""Exposes all of the resource endpoints mounted in Flask-Blueprint style.

Uses restplus namespaces to mount individual api endpoints into the service.
"""

from flask import Blueprint
from flask_restx import Api

from .fixture import API as FIXTURE_API
from .gameweek import API as GAMEWEEK_API
from .player_stats import API as PLAYER_STATS_API
from .player import API as PLAYER_API
from .position import API as POSITION_API
from .stat_details import API as STAT_DETAILS_API
from .team import API as TEAM_API

__all__ = ("API", "API_BLUEPRINT")


API_BLUEPRINT = Blueprint("API", __name__, url_prefix="/api/v1")

API = Api(
    API_BLUEPRINT,
    title="FPL TINKER API",
    version="1.0",
    description="The api for the FPL Tinker app",
)

API.add_namespace(FIXTURE_API, path="/fixtures")
API.add_namespace(GAMEWEEK_API, path="/gameweeks")
API.add_namespace(PLAYER_STATS_API, path="/players/stats")
API.add_namespace(PLAYER_API, path="/players")
API.add_namespace(POSITION_API, path="/positions")
API.add_namespace(STAT_DETAILS_API, path="/stats/details")
API.add_namespace(TEAM_API, path="/teams")
