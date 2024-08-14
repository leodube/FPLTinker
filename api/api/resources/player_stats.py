"""Description."""

from flask import jsonify
from flask_restx import Namespace, Resource

API = Namespace("PlayerStats", description="FPL Player Statistics")


@API.route("/")
class PlayerStats(Resource):
    """Description."""

    @staticmethod
    def get():
        """Description."""
        return jsonify("test player stats")
