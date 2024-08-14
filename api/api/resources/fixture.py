"""Description."""

from flask import jsonify
from flask_restx import Namespace, Resource

API = Namespace("Fixtures", description="FPL Fixtures")


@API.route("/")
class Fixture(Resource):
    """Description."""

    @staticmethod
    def get():
        """Description."""
        return jsonify("test fixture")
