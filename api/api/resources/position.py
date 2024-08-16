"""Description."""

from flask_restx import Namespace, Resource
from models import Configuration, Position
from .marshalling.models import position_dict, position_details_dict

api = Namespace("Positions", description="FPL Player Positions")

position_model = api.model("PositionModel", position_dict)
position_details_model = position_model.clone(
    "PositionDetailsModel", position_details_dict
)


@api.route("/")
class PositionListResource(Resource):
    """Position list api resource."""

    @api.marshal_with(position_model)
    def get(self):
        """Get a list of all the positions."""
        positions = Position.all()
        return positions


@api.route("/<fpl_id>")
@api.param("fpl_id", "The FPL identifier")
class PositionResource(Resource):
    """Position api resource."""

    @api.marshal_with(position_details_model)
    def get(self, fpl_id):
        """Get a position by it's Fpl identifier."""
        position = Position.find(
            fpl_id=fpl_id, season=Configuration.get("season")
        )
        return position
