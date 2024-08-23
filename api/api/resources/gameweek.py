"""Contains Fantasy Premiere League gameweek api resource."""

from flask_restx import Namespace, Resource
from models import Configuration, Gameweek

from .marshalling import BaseMarshal, DetailedMarshal

api = Namespace("gameweeks", description="FPL Gameweeks")

base_model = api.model("GameweekBaseModel", BaseMarshal.gameweek)
detailed_model = base_model.clone("GameweekDetailedModel", DetailedMarshal.gameweek)


@api.route("/")
class GameweekListResource(Resource):
    """Gameweek list api resource."""

    @api.marshal_list_with(base_model)
    def get(self):
        """Get a list of all the gameweeks."""
        gameweeks = Gameweek.all()
        return gameweeks


@api.route("/<fpl_id>", "/current")
class GameweekResource(Resource):
    """Gameweek api resource."""

    @api.marshal_with(detailed_model)
    def get(self, fpl_id: int = None):
        """Get a gameweek by it's Fpl identifier."""
        if fpl_id:
            gameweek = Gameweek.find(fpl_id=fpl_id, season=Configuration.get("season"))
            return gameweek

        gameweek = Gameweek.find(is_current=True)
        if not gameweek:
            gameweek = Gameweek.find(is_next=True)
        return gameweek
