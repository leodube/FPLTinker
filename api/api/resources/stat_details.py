"""Contains Fantasy Premiere League stat details api resource."""

from flask_restx import Namespace, Resource
from models import StatDetails

from .marshalling import BaseMarshal

api = Namespace("stats", description="Statistic Details")

base_model = api.model("StatDetailsBaseModel", BaseMarshal.stat_details)


@api.route("/")
class StatDetailsListResource(Resource):
    """Stat details list api resource."""

    @api.marshal_list_with(base_model)
    def get(self):
        """Get a list of all the stat details."""
        stat_details = StatDetails.all()
        return stat_details


@api.route("/<name>")
class StatDetailsResource(Resource):
    """Stat details api resource."""

    @api.marshal_with(base_model)
    def get(self, name):
        """Get a stat's details by it's name."""
        stat_details = StatDetails.find(name=name)
        return stat_details
