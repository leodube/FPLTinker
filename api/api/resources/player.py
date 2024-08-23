"""Contains Fantasy Premiere League player api resource."""

from flask_restx import Namespace, Resource
from models import Configuration, Player

from .marshalling import BaseMarshal, DetailedMarshal

api = Namespace("players", description="FPL Players")

base_model = api.model("PlayerBaseModel", BaseMarshal.player)
detailed_model = base_model.clone("PlayerDetailedModel", DetailedMarshal.player)


@api.route("/")
class PlayerListResource(Resource):
    """Player list api resource."""

    @api.marshal_list_with(base_model)
    def get(self):
        """Get a list of all the fixtures."""
        players = Player.all()
        return players


@api.route("/<fpl_id>")
class PlayerResource(Resource):
    """Player api resource."""

    @api.marshal_with(detailed_model)
    def get(self, fpl_id):
        """Get a player by it's Fpl identifier."""
        player = Player.find(fpl_id=fpl_id, season=Configuration.get("season"))
        return player
