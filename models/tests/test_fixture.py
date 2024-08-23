"""Test suite to ensure the fixture model is working as expected."""

from copy import deepcopy

import pytest

from models.models import Fixture, Team, Gameweek
from tests import factory_fixture, fixture_data, factory_team, factory_gameweek


@pytest.mark.usefixtures("session")
class TestFixture:
    @pytest.fixture
    def data(self) -> dict:
        return deepcopy(fixture_data)

    @pytest.fixture
    def gameweek(self) -> Gameweek:
        return factory_gameweek()

    @pytest.fixture
    def away_team(self) -> Team:
        return factory_team(code=1, name="Away Team")

    @pytest.fixture
    def home_team(self) -> Team:
        return factory_team(code=2, name="Home Team")

    def test_save(self, gameweek: Gameweek, away_team: Team, home_team: Team):
        """Assert the fixture can be saved."""
        fixture = factory_fixture(
            gameweek_id=gameweek.id, team_a_id=away_team.id, team_h_id=home_team.id
        )
        assert fixture.id

    def test_delete(self, gameweek: Gameweek, away_team: Team, home_team: Team):
        """Assert the fixture can be deleted."""
        fixture = factory_fixture(
            gameweek_id=gameweek.id, team_a_id=away_team.id, team_h_id=home_team.id
        )
        assert fixture.id
        fixture.delete()
        assert Fixture.count() == 0

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

    def test_find(self, data, gameweek: Gameweek, away_team: Team, home_team: Team):
        """Assert a matching fixture object can be found."""
        data.update(
            {
                "gameweek_id": gameweek.id,
                "team_a_id": away_team.id,
                "team_h_id": home_team.id,
            }
        )
        fixture = factory_fixture(**data)
        assert fixture == Fixture.find(**data)

    def test_find_all(self, data, gameweek: Gameweek, away_team: Team, home_team: Team):
        """Assert all matching fixture object can be found."""
        data.update(
            {
                "gameweek_id": gameweek.id,
                "team_a_id": away_team.id,
                "team_h_id": home_team.id,
            }
        )
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

    def test_bulk_upsert(
        self, data, gameweek: Gameweek, away_team: Team, home_team: Team
    ):
        """Assert entries can be inserted and updated."""
        data.update(
            {
                "gameweek_id": gameweek.id,
                "team_a_id": away_team.id,
                "team_h_id": home_team.id,
            }
        )

        # Test inserting entries
        fixtures = []
        for i in range(num_fixtures_inserted := 5):
            data.update({"code": i})
            fixtures.append(deepcopy(data))
        Fixture.bulk_upsert(fixtures)
        assert Fixture.count() == num_fixtures_inserted

        # Test updating entries
        fixtures = []
        for i in range(3):
            data.update({"code": i, "team_a_score": i})
            fixtures.append(deepcopy(data))
        Fixture.bulk_upsert(fixtures)
        assert Fixture.count() == num_fixtures_inserted
