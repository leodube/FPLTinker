"""Test suite to ensure the player model is working as expected."""

from copy import deepcopy

import pytest

from models.models import Player, Position, Team
from tests import factory_player, factory_position, factory_team, player_data


@pytest.mark.usefixtures("session")
class TestPlayer:
    @pytest.fixture
    def data(self) -> dict:
        return deepcopy(player_data)

    @pytest.fixture
    def position(self) -> Position:
        return factory_position()

    @pytest.fixture
    def team(self) -> Team:
        return factory_team()

    def test_save(self, position: Position, team: Team):
        """Assert the player can be saved."""
        player = factory_player(position_id=position.id, team_id=team.id)
        assert player.id

    def test_delete(self, position: Position, team: Team):
        """Assert the player can be deleted."""
        player = factory_player(position_id=position.id, team_id=team.id)
        assert player.id
        player.delete()
        assert Player.count() == 0

    def test_all(self, position: Position, team: Team):
        """Assert all entries can be found for the player."""
        for i in range(num_players := 5):
            factory_player(
                code=i,
                position_id=position.id,
                team_id=team.id,
                web_name=f"player {i}",
            )
        assert len(Player.all()) == num_players

    def test_count(self, position: Position, team: Team):
        """Assert a count of all player entries can be found."""
        for i in range(num_players := 5):
            factory_player(
                code=i,
                position_id=position.id,
                team_id=team.id,
                web_name=f"player {i}",
            )
        assert Player.count() == num_players

    def test_find(self, data, position: Position, team: Team):
        """Assert a matching player object can be found."""
        data.update({"position_id": position.id, "team_id": team.id})
        player = factory_player(**data)
        assert player == Player.find(**data)

    def test_find_all(self, data, position: Position, team: Team):
        """Assert all matching player object can be found."""
        for i in range(num_players := 5):
            data.update(
                {
                    "code": i,
                    "position_id": position.id,
                    "team_id": team.id,
                    "web_name": f"player {i}",
                }
            )
            factory_player(**data)
        del data["code"]
        del data["web_name"]
        results = Player.find_all(**data)
        assert results and len(results.all()) == num_players

    def test_index_constraints(self, db, metadata):
        """Assert the index constraints are unique."""
        table = metadata.tables["players"]
        table_constraint = next(
            (
                constraint
                for constraint in table.constraints
                if isinstance(constraint, db.UniqueConstraint)
            ),
            None,
        )
        assert table_constraint
        for index_constraint in Player.index_constraints():
            assert table_constraint.contains_column(table.c[index_constraint])

    def test_bulk_upsert(self, data, position: Position, team: Team):
        """Assert entries can be inserted and updated."""
        # Test inserting entries
        players = []
        for i in range(num_players_inserted := 5):
            data.update(
                {
                    "code": i,
                    "position_id": position.id,
                    "team_id": team.id,
                    "web_name": f"player {i}",
                }
            )
            players.append(deepcopy(data))
        Player.bulk_upsert(players)
        assert Player.count() == num_players_inserted

        # Test updating entries
        players = []
        for i in range(3):
            data.update({"code": i, "web_name": f"new name {i}"})
            players.append(deepcopy(data))
        Player.bulk_upsert(players)
        assert Player.count() == num_players_inserted
