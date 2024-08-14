"""Description."""

from flask import jsonify
from flask_restx import Namespace, Resource

API = Namespace("Positions", description="FPL Player Positions")


@API.route("/")
class Position(Resource):
    """Description."""

    @staticmethod
    def get():
        """Description."""
        return jsonify("test position")
