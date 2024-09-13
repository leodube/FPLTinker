"""Test suite to ensure the fixture model is working as expected."""

from copy import deepcopy

import pytest
from sqlalchemy.exc import IntegrityError

from models.models import Fixture, Gameweek, Team
from tests import factory_fixture, factory_gameweek, factory_team, fixture_data


@pytest.mark.usefixtures("session")
class TestFixture:
    """The class pytest grouping for the fixture model."""

    @pytest.fixture
    def gameweek(self) -> Gameweek:
        """Returns a class-wide gameweek instance."""
        return factory_gameweek()

    @pytest.fixture
    def away_team(self) -> Team:
        """Returns a class-wide away team instance."""
        return factory_team(code=1, name="Away Team")

    @pytest.fixture
    def home_team(self) -> Team:
        """Returns a class-wide home team instance."""
        return factory_team(code=2, name="Home Team")

    @pytest.fixture
    def data(self, gameweek: Gameweek, away_team: Team, home_team: Team) -> dict:
        """Returns a class-wide copy of the fixture data object."""
        _data = deepcopy(fixture_data)
        _data.update(
            {
                "gameweek_id": gameweek.id,
                "team_a_id": away_team.id,
                "team_h_id": home_team.id,
            }
        )
        return _data

    def test_save(self, gameweek: Gameweek, away_team: Team, home_team: Team):
        """Assert the fixture can be saved."""
        fixture = factory_fixture(
            gameweek_id=gameweek.id, team_a_id=away_team.id, team_h_id=home_team.id
        )
        assert fixture.id

    def test_save_with_conflict(
        self, gameweek: Gameweek, away_team: Team, home_team: Team
    ):
        """Assert the fixture won't be saved if constraints violated."""
        factory_fixture(
            gameweek_id=gameweek.id, team_a_id=away_team.id, team_h_id=home_team.id
        )
        with pytest.raises(IntegrityError):
            factory_fixture(
                gameweek_id=gameweek.id, team_a_id=away_team.id, team_h_id=home_team.id
            )

    def test_delete(self, gameweek: Gameweek, away_team: Team, home_team: Team):
        """Assert the fixture can be deleted."""
        fixture = factory_fixture(
            gameweek_id=gameweek.id, team_a_id=away_team.id, team_h_id=home_team.id
        )
        assert fixture.id
        fixture.delete()
        assert Fixture.count() == 0

    def test_serialize(self, gameweek: Gameweek, away_team: Team, home_team: Team):
        """Assert the fixture object can be serialized."""
        fixture = factory_fixture(
            gameweek_id=gameweek.id, team_a_id=away_team.id, team_h_id=home_team.id
        )
        assert fixture.serialize()

    def test_all(self, gameweek: Gameweek, away_team: Team, home_team: Team):
        """Assert all entries can be found for the fixture."""
        for i in range(num_fixtures := 5):
            factory_fixture(
                code=i,
                gameweek_id=gameweek.id,
                team_a_id=away_team.id,
                team_h_id=home_team.id,
            )
        assert len(Fixture.all()) == num_fixtures

    def test_count(self, gameweek: Gameweek, away_team: Team, home_team: Team):
        """Assert a count of all fixture entries can be found."""
        for i in range(num_fixtures := 5):
            factory_fixture(
                code=i,
                gameweek_id=gameweek.id,
                team_a_id=away_team.id,
                team_h_id=home_team.id,
            )
        assert Fixture.count() == num_fixtures

    def test_find(self, data):
        """Assert a matching fixture object can be found."""
        fixture = factory_fixture(**data)
        assert fixture == Fixture.find(**data)

    def test_find_instance(self, data):
        """Assert a matching fixture object can be found."""
        created = factory_fixture(**data)
        keys = Fixture.__dict__.keys()
        team = Fixture(**{key: data[key] for key in keys if key in data})
        found = Fixture.find_instance(team)
        assert created == found

    def test_find_all(self, data):
        """Assert all matching fixture object can be found."""
        for i in range(num_fixtures := 5):
            data.update({"code": i})
            factory_fixture(**data)
        del data["code"]
        results = Fixture.find_all(**data)
        assert results and len(results.all()) == num_fixtures

    def test_index_constraints(self, db, metadata):
        """Assert the index constraints are unique."""
        table = metadata.tables["fixtures"]
        table_constraint = next(
            (
                constraint
                for constraint in table.constraints
                if isinstance(constraint, db.UniqueConstraint)
            ),
            None,
        )
        assert table_constraint
        for index_constraint in Fixture.index_constraints():
            assert table_constraint.contains_column(table.c[index_constraint])
