"""Description."""

from flask import jsonify
from flask_restx import Namespace, Resource

API = Namespace("StatDetails", description="Statistic Details")


@API.route("/")
class StatDetail(Resource):
    """Description."""

    @staticmethod
    def get():
        """Description."""
        return jsonify("test stat detail")
