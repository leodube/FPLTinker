"""Description."""

from flask import jsonify
from flask_restx import Namespace, Resource

API = Namespace("Players", description="FPL Players")


@API.route("/")
class Player(Resource):
    """Description."""

    @staticmethod
    def get():
        """Description."""
        return jsonify("test player")
