"""Test suite to ensure the player stats model is working as expected."""

from copy import deepcopy

import pytest
from sqlalchemy.exc import IntegrityError

from models.models import Player, PlayerStats
from tests import (
    factory_player,
    factory_player_stats,
    factory_position,
    factory_team,
    player_stats_data,
)

from ..models.utils import date_utilities


@pytest.mark.usefixtures("session")
class TestPlayerStats:
    """The class pytest grouping for the player stats model."""

    @pytest.fixture
    def player(self) -> Player:
        """Returns a class-wide player instance."""
        position = factory_position()
        team = factory_team()
        return factory_player(position_id=position.id, team_id=team.id)

    @pytest.fixture
    def data(self, player) -> dict:
        """Returns a class-wide copy of the player stats data object."""
        _data = deepcopy(player_stats_data)
        _data.update({"player_id": player.id})
        return _data

    def test_save(self, player: Player):
        """Assert the player stats can be saved."""
        player_stats = factory_player_stats(player_id=player.id)
        assert player_stats.id

    def test_save_with_conflict(self, player: Player):
        """Assert the player stats won't be saved if constraints violated."""
        factory_player_stats(player_id=player.id)
        with pytest.raises(IntegrityError):
            factory_player_stats(player_id=player.id)

    def test_delete(self, player: Player):
        """Assert the player stats can be deleted."""
        player_stats = factory_player_stats(player_id=player.id)
        assert player_stats.id
        player_stats.delete()
        assert PlayerStats.count() == 0

    def test_all(self, player: Player):
        """Assert all entries can be found for the player stats."""
        for i in range(num_player_stats := 5):
            factory_player_stats(
                player_id=player.id, season=date_utilities.add_to_season(20242025, -i)
            )
        assert len(PlayerStats.all()) == num_player_stats

    def test_count(self, player: Player):
        """Assert a count of all player stats entries can be found."""
        for i in range(num_player_stats := 5):
            factory_player_stats(
                player_id=player.id, season=date_utilities.add_to_season(20242025, -i)
            )
        assert PlayerStats.count() == num_player_stats

    def test_find(self, data):
        """Assert a matching player stats object can be found."""
        player_stats = factory_player_stats(**data)
        assert player_stats == PlayerStats.find(**data)

    def test_find_instance(self, data):
        """Assert a matching player stats object can be found."""
        created = factory_player_stats(**data)
        keys = PlayerStats.__dict__.keys()
        team = PlayerStats(**{key: data[key] for key in keys if key in data})
        found = PlayerStats.find_instance(team)
        assert created == found

    def test_find_all(self, data):
        """Assert all matching player stats object can be found."""
        for i in range(num_player_stats := 5):
            data.update(
                {
                    "season": date_utilities.add_to_season(20242025, -i),
                }
            )
            factory_player_stats(**data)
        del data["player_id"]
        del data["season"]
        results = PlayerStats.find_all(**data)
        assert results and len(results.all()) == num_player_stats

    def test_index_constraints(self, db, metadata):
        """Assert the index constraints are unique."""
        table = metadata.tables["player_stats"]
        table_constraint = next(
            (
                constraint
                for constraint in table.constraints
                if isinstance(constraint, db.UniqueConstraint)
            ),
            None,
        )
        assert table_constraint
        for index_constraint in PlayerStats.index_constraints():
            assert table_constraint.contains_column(table.c[index_constraint])
