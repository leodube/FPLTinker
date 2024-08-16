"""Description."""

from flask_restx import Namespace, Resource
from models import Configuration, Fixture
from .marshalling.models import fixture_dict, fixture_details_dict

api = Namespace("Fixtures", description="FPL Fixtures")

fixture_model = api.model("FixtureModel", fixture_dict)
fixture_details_model = fixture_model.clone(
    "FixtureDetailsModel", fixture_details_dict
)


@api.route("/")
class FixtureListResource(Resource):
    """Fixture list api resource."""

    @api.marshal_with(fixture_model)
    def get(self):
        """Get a list of all the fixtures."""
        fixtures = Fixture.all()
        return fixtures


@api.route("/<fpl_id>")
@api.param("fpl_id", "The FPL identifier")
class FixtureResource(Resource):
    """Fixture api resource."""

    @api.marshal_with(fixture_details_model)
    def get(self, fpl_id):
        """Get a fixture by it's Fpl identifier."""
        fixture = Fixture.find(
            fpl_id=fpl_id, season=Configuration.get("season")
        )
        return fixture
