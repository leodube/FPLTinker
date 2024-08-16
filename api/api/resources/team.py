"""Description."""

from flask_restx import Namespace, Resource
from models import Configuration, Team
from .marshalling.models import team_dict, team_details_dict

api = Namespace("Teams", description="FPL Teams")

team_model = api.model("TeamModel", team_dict)
team_details_model = team_model.clone("TeamDetailsModel", team_details_dict)


@api.route("/")
class TeamListResource(Resource):
    """Team list api resource."""

    @api.marshal_with(team_model)
    def get(self):
        """Get a list of all the teams."""
        teams = Team.all()
        return teams


@api.route("/<fpl_id>")
@api.param("fpl_id", "The FPL identifier")
class TeamResource(Resource):
    """Team api resource."""

    @api.marshal_with(team_details_model)
    def get(self, fpl_id):
        """Get a team by it's Fpl identifier."""
        team = Team.find(fpl_id=fpl_id, season=Configuration.get("season"))
        return team
