"""Test suite to ensure the fixture stat  model is working as expected."""

from copy import deepcopy

import pytest

from models.models import FixtureStat, Fixture, Team, Player, StatDetails, Position
from tests import (
    factory_fixture_stat,
    fixture_stat_data,
    factory_fixture,
    factory_team,
    factory_stat_details,
    factory_player,
    factory_gameweek,
    factory_position,
)


@pytest.mark.usefixtures("session")
class TestFixtureStat:

    team_code_offset = 3  # used to prevent duplicate key on unique constraint

    @pytest.fixture
    def data(self) -> dict:
        return deepcopy(fixture_stat_data)

    @pytest.fixture
    def team(self) -> Team:
        return factory_team()

    @pytest.fixture
    def stat_details(self) -> StatDetails:
        return factory_stat_details()

    @pytest.fixture
    def position(self) -> Position:
        return factory_position()

    @pytest.fixture
    def player(self, team: Team, position: Position) -> Player:
        return factory_player(team_id=team.id, position_id=position.id)

    @pytest.fixture
    def fixture(self, team: Team) -> Fixture:
        away_team = factory_team(code=self.team_code_offset - 1)
        gameweek = factory_gameweek()
        return factory_fixture(
            team_a_id=away_team.id, team_h_id=team.id, gameweek_id=gameweek.id
        )

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
        position: Position,
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

    def test_find(
        self,
        data,
        fixture: Fixture,
        team: Team,
        player: Player,
        stat_details: StatDetails,
    ):
        """Assert a matching fixture stats object can be found."""
        data.update(
            {
                "fixture_id": fixture.id,
                "team_id": team.id,
                "player_id": player.id,
                "stat_details_id": stat_details.id,
            }
        )
        fixture_stats = factory_fixture_stat(**data)
        assert fixture_stats == FixtureStat.find(**data)

    def test_find_all(
        self,
        data,
        fixture: Fixture,
        player: Player,
        stat_details: StatDetails,
    ):
        """Assert all matching fixture stats object can be found."""
        data.update(
            {
                "fixture_id": fixture.id,
                "player_id": player.id,
                "stat_details_id": stat_details.id,
            }
        )

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

    def test_bulk_upsert(
        self,
        data,
        fixture: Fixture,
        player: Player,
        stat_details: StatDetails,
    ):
        """Assert entries can be inserted and updated."""
        data.update(
            {
                "fixture_id": fixture.id,
                "player_id": player.id,
                "stat_details_id": stat_details.id,
            }
        )

        # Test inserting entries
        fixture_stats = []
        for i in range(num_fixture_stats_inserted := 5):
            data.update(
                {"team_id": factory_team(code=i + self.team_code_offset).id, "value": i}
            )
            fixture_stats.append(deepcopy(data))
        FixtureStat.bulk_upsert(fixture_stats)
        assert FixtureStat.count() == num_fixture_stats_inserted

        # Test updating entries
        fixture_stats = []
        for i in range(3):
            data.update(
                {
                    "team_id": Team.find(code=i + self.team_code_offset).id,
                    "value": i + 1,
                }
            )
            fixture_stats.append(deepcopy(data))
        FixtureStat.bulk_upsert(fixture_stats)
        assert FixtureStat.count() == num_fixture_stats_inserted
