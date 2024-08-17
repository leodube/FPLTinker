"""Contains Fantasy Premiere League fixture api resource."""

from flask_restx import Namespace, Resource
from models import Configuration, Fixture

from .marshalling import BaseMarshal, DetailedMarshal

api = Namespace("Fixtures", description="FPL Fixtures")

base_model = api.model("FixtureBaseModel", BaseMarshal.fixture)
detailed_model = base_model.clone("FixtureDetailedModel", DetailedMarshal.fixture)


@api.route("/")
class FixtureListResource(Resource):
    """Fixture list api resource."""

    @api.marshal_with(base_model)
    def get(self):
        """Get a list of all the fixtures."""
        fixtures = Fixture.all()
        return fixtures


@api.route("/<fpl_id>")
@api.param("fpl_id", "The FPL identifier")
class FixtureResource(Resource):
    """Fixture api resource."""

    @api.marshal_with(detailed_model)
    def get(self, fpl_id):
        """Get a fixture by it's Fpl identifier."""
        fixture = Fixture.find(fpl_id=fpl_id, season=Configuration.get("season"))
        return fixture
