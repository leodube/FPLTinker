"""Description."""

from flask import jsonify
from flask_restx import Namespace, Resource

API = Namespace("Gameweeks", description="FPL Gameweeks")


@API.route("/")
class Gameweek(Resource):
    """Description."""

    @staticmethod
    def get():
        """Description."""
        return jsonify("test gameweek")
