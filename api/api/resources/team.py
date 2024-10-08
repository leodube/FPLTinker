"""Contains Fantasy Premiere League team api resource."""

from flask_restx import Namespace, Resource
from models import Configuration, Team

from .marshalling import BaseMarshal, DetailedMarshal

api = Namespace("teams", description="FPL Teams")

base_model = api.model("TeamBaseModel", BaseMarshal.team)
detailed_model = base_model.clone("TeamDetailedModel", DetailedMarshal.team)


@api.route("/")
class TeamListResource(Resource):
    """Team list api resource."""

    @api.marshal_list_with(base_model)
    def get(self):
        """Get a list of all the teams."""
        teams = Team.all()
        return teams


@api.route("/<fpl_id>")
class TeamResource(Resource):
    """Team api resource."""

    @api.marshal_with(detailed_model)
    def get(self, fpl_id):
        """Get a team by it's Fpl identifier."""
        team = Team.find(fpl_id=fpl_id, season=Configuration.get("season"))
        return team
