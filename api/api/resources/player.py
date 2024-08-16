"""Description."""

from flask import jsonify
from flask_restx import Namespace, Resource

api = Namespace("Players", description="FPL Players")


@api.route("/")
class Player(Resource):
    """Description."""

    @staticmethod
    def get():
        """Description."""
        return jsonify("test player")
