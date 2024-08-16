"""Description."""

from flask import jsonify
from flask_restx import Namespace, Resource

api = Namespace("StatDetails", description="Statistic Details")


@api.route("/")
class StatDetail(Resource):
    """Description."""

    @staticmethod
    def get():
        """Description."""
        return jsonify("test stat detail")
