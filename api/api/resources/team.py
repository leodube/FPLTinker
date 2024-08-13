"""Description."""

from flask import jsonify
from flask_restx import Namespace, Resource

API = Namespace("teams", description="FPL Teams")


@API.route("/")
class Team(Resource):
    """Description."""

    @staticmethod
    def get():
        """Description."""
        return jsonify("test team")
