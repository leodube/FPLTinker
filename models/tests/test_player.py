"""Test suite to ensure the player model is working as expected."""

from copy import deepcopy

import pytest
from sqlalchemy.exc import IntegrityError

from models.models import Player, Position, Team
from tests import factory_player, factory_position, factory_team, player_data


@pytest.mark.usefixtures("session")
class TestPlayer:
    """The class pytest grouping for the player model."""

    @pytest.fixture
    def position(self) -> Position:
        """Returns a class-wide position instance."""
        return factory_position()

    @pytest.fixture
    def team(self) -> Team:
        """Returns a class-wide team instance."""
        return factory_team()

    @pytest.fixture
    def data(self, position, team) -> dict:
        """Returns a class-wide copy of the player data object."""
        _data = deepcopy(player_data)
        _data.update({"position_id": position.id, "team_id": team.id})
        return _data

    def test_save(self, position: Position, team: Team):
        """Assert the player can be saved."""
        player = factory_player(position_id=position.id, team_id=team.id)
        assert player.id

    def test_save_with_conflict(self, position: Position, team: Team):
        """Assert the player won't be saved if constraints violated."""
        factory_player(position_id=position.id, team_id=team.id)
        with pytest.raises(IntegrityError):
            factory_player(position_id=position.id, team_id=team.id)

    def test_delete(self, position: Position, team: Team):
        """Assert the player can be deleted."""
        player = factory_player(position_id=position.id, team_id=team.id)
        assert player.id
        player.delete()
        assert Player.count() == 0

    def test_serialize(self, position: Position, team: Team):
        """Assert the player object can be serialized."""
        player = factory_player(position_id=position.id, team_id=team.id)
        assert player.serialize()

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

    def test_find(self, data):
        """Assert a matching player object can be found."""
        player = factory_player(**data)
        assert player == Player.find(**data)

    def test_find_instance(self, data):
        """Assert a matching player object can be found."""
        created = factory_player(**data)
        keys = Player.__dict__.keys()
        team = Player(**{key: data[key] for key in keys if key in data})
        found = Player.find_instance(team)
        assert created == found

    def test_find_all(self, data):
        """Assert all matching player object can be found."""
        for i in range(num_players := 5):
            data.update(
                {
                    "code": i,
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
