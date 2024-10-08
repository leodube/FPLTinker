"""Test suite to ensure the fixture stat  model is working as expected."""

from copy import deepcopy

import pytest
from sqlalchemy.exc import IntegrityError

from models.models import Fixture, FixtureStat, Player, Position, StatDetails, Team
from tests import (
    factory_fixture,
    factory_fixture_stat,
    factory_gameweek,
    factory_player,
    factory_position,
    factory_stat_details,
    factory_team,
    fixture_stat_data,
)


@pytest.mark.usefixtures("session")
class TestFixtureStat:
    """The class pytest grouping for the fixture stat model."""

    team_code_offset = 3  # used to prevent duplicate key on unique constraint

    @pytest.fixture
    def team(self) -> Team:
        """Returns a class-wide team instance."""
        return factory_team()

    @pytest.fixture
    def stat_details(self) -> StatDetails:
        """Returns a class-wide stat details instance."""
        return factory_stat_details()

    @pytest.fixture
    def position(self) -> Position:
        """Returns a class-wide position instance."""
        return factory_position()

    @pytest.fixture
    def player(self, team: Team, position: Position) -> Player:
        """Returns a class-wide player instance."""
        return factory_player(team_id=team.id, position_id=position.id)

    @pytest.fixture
    def fixture(self, team: Team) -> Fixture:
        """Returns a class-wide fixture instance."""
        away_team = factory_team(code=self.team_code_offset - 1)
        gameweek = factory_gameweek()
        return factory_fixture(
            team_a_id=away_team.id, team_h_id=team.id, gameweek_id=gameweek.id
        )

    @pytest.fixture
    def data(
        self, fixture: Fixture, team: Team, player: Player, stat_details: StatDetails
    ) -> dict:
        """Returns a class-wide copy of the fixture stat data object."""
        _data = deepcopy(fixture_stat_data)
        _data.update(
            {
                "fixture_id": fixture.id,
                "team_id": team.id,
                "player_id": player.id,
                "stat_details_id": stat_details.id,
            }
        )
        return _data

    def test_save(
        self, fixture: Fixture, team: Team, player: Player, stat_details: StatDetails
    ):
        """Assert the fixture stats can be saved."""
        fixture_stats = factory_fixture_stat(
            fixture_id=fixture.id,
            team_id=team.id,
            player_id=player.id,
            stat_details_id=stat_details.id,
        )
        assert fixture_stats.id

    def test_save_with_conflict(
        self, fixture: Fixture, team: Team, player: Player, stat_details: StatDetails
    ):
        """Assert the fixture stats won't be saved if constraints violated."""
        factory_fixture_stat(
            fixture_id=fixture.id,
            team_id=team.id,
            player_id=player.id,
            stat_details_id=stat_details.id,
        )
        with pytest.raises(IntegrityError):
            factory_fixture_stat(
                fixture_id=fixture.id,
                team_id=team.id,
                player_id=player.id,
                stat_details_id=stat_details.id,
            )

    def test_delete(
        self, fixture: Fixture, team: Team, player: Player, stat_details: StatDetails
    ):
        """Assert the fixture stats can be deleted."""
        fixture_stats = factory_fixture_stat(
            fixture_id=fixture.id,
            team_id=team.id,
            player_id=player.id,
            stat_details_id=stat_details.id,
        )
        assert fixture_stats.id
        fixture_stats.delete()
        assert FixtureStat.count() == 0

    def test_serialize(
        self, fixture: Fixture, team: Team, player: Player, stat_details: StatDetails
    ):
        """Assert the fixture stats object can be serialized."""
        fixture_stats = factory_fixture_stat(
            fixture_id=fixture.id,
            team_id=team.id,
            player_id=player.id,
            stat_details_id=stat_details.id,
        )
        assert fixture_stats.serialize()

    def test_all(
        self,
        fixture: Fixture,
        player: Player,
        stat_details: StatDetails,
    ):
        """Assert all entries can be found for the fixture stats."""
        for i in range(num_fixture_stats := 5):
            factory_fixture_stat(
                fixture_id=fixture.id,
                team_id=factory_team(code=i + self.team_code_offset).id,
                player_id=player.id,
                stat_details_id=stat_details.id,
                value=i,
            )
        assert len(FixtureStat.all()) == num_fixture_stats

    def test_count(
        self,
        fixture: Fixture,
        player: Player,
        stat_details: StatDetails,
    ):
        """Assert a count of all fixture stats entries can be found."""
        for i in range(num_fixture_stats := 5):
            factory_fixture_stat(
                fixture_id=fixture.id,
                team_id=factory_team(code=i + self.team_code_offset).id,
                player_id=player.id,
                stat_details_id=stat_details.id,
                value=i,
            )
        assert FixtureStat.count() == num_fixture_stats

    def test_find(self, data):
        """Assert a matching fixture stats object can be found."""
        fixture_stats = factory_fixture_stat(**data)
        assert fixture_stats == FixtureStat.find(**data)

    def test_find_instance(self, data):
        """Assert a matching fixture stats object can be found."""
        created = factory_fixture_stat(**data)
        keys = FixtureStat.__dict__.keys()
        team = FixtureStat(**{key: data[key] for key in keys if key in data})
        found = FixtureStat.find_instance(team)
        assert created == found

    def test_find_all(self, data):
        """Assert all matching fixture stats object can be found."""
        for i in range(num_fixture_stats := 5):
            data.update(
                {"team_id": factory_team(code=i + self.team_code_offset).id, "value": i}
            )
            factory_fixture_stat(**data)
        del data["team_id"]
        del data["value"]
        results = FixtureStat.find_all(**data)
        assert results and len(results.all()) == num_fixture_stats

    def test_index_constraints(self, db, metadata):
        """Assert the index constraints are unique."""
        table = metadata.tables["fixture_stats"]
        table_constraint = next(
            (
                constraint
                for constraint in table.constraints
                if isinstance(constraint, db.UniqueConstraint)
            ),
            None,
        )
        assert table_constraint
        for index_constraint in FixtureStat.index_constraints():
            assert table_constraint.contains_column(table.c[index_constraint])
