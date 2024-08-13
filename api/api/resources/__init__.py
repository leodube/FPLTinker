"""Exposes all of the resource endpoints mounted in Flask-Blueprint style.

Uses restplus namespaces to mount individual api endpoints into the service.
"""

from flask import Blueprint
from flask_restx import Api

from .team import API as TEAM_API

__all__ = ("API", "API_BLUEPRINT")


API_BLUEPRINT = Blueprint("API", __name__, url_prefix="/api/v1")

API = Api(
    API_BLUEPRINT,
    title="FPL TINKER API",
    version="1.0",
    description="The api for the FPL Tinker app",
)

API.add_namespace(TEAM_API, path="/teams")
