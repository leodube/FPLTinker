"""Description."""

from flask_restx import Namespace, Resource
from models import Configuration, Position

from .marshalling import BaseMarshal, DetailedMarshal

api = Namespace("Positions", description="FPL Player Positions")

base_model = api.model("BaseModel", BaseMarshal.position)
detailed_model = base_model.clone("DetailedModel", DetailedMarshal.position)


@api.route("/")
class PositionListResource(Resource):
    """Position list api resource."""

    @api.marshal_with(base_model)
    def get(self):
        """Get a list of all the positions."""
        positions = Position.all()
        return positions


@api.route("/<fpl_id>")
@api.param("fpl_id", "The FPL identifier")
class PositionResource(Resource):
    """Position api resource."""

    @api.marshal_with(detailed_model)
    def get(self, fpl_id):
        """Get a position by it's Fpl identifier."""
        position = Position.find(
            fpl_id=fpl_id, season=Configuration.get("season")
        )
        return position
