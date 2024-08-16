"""Description."""

from flask_restx import fields, Namespace, Resource
from models import Configuration, Gameweek
from .marshalling.models import gameweek_dict, gameweek_details_dict

api = Namespace("Gameweeks", description="FPL Gameweeks")

gameweek_model = api.model("GameweekModel", gameweek_dict)
gameweek_details_model = gameweek_model.clone(
    "GameweekDetailsModel", gameweek_details_dict
)


@api.route("/")
class GameweekListResource(Resource):
    """Gameweek list api resource."""

    @api.marshal_with(gameweek_model)
    def get(self):
        """Get a list of all the gameweeks."""
        gameweeks = Gameweek.all()
        return gameweeks


@api.route("/<fpl_id>", "/current")
@api.param("fpl_id", "The FPL identifier")
class GameweekResource(Resource):
    """Gameweek api resource."""

    @api.marshal_with(gameweek_details_model)
    def get(self, fpl_id: int = None):
        """Get a gameweek by it's Fpl identifier."""
        if fpl_id:
            gameweek = Gameweek.find(
                fpl_id=fpl_id, season=Configuration.get("season")
            )
            return gameweek

        gameweek = Gameweek.find(is_current=True)
        if not gameweek:
            gameweek = Gameweek.find(is_next=True)
        return gameweek
