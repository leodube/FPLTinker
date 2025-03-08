"""Test suite to ensure the players updater is working as expected."""

import pytest
from fpltinker.models import Player

from data_updater.updaters import players


@pytest.mark.usefixtures("session", "mocker", "app", "fpl")
class TestPlayersUpdater:
    """The class pytest grouping for the players updater."""

    @pytest.fixture
    def mock_team(self, mocker):
        """Returns a class-wide mocked team."""
        mock = mocker.MagicMock()
        mock.id = 1
        return mock

    @pytest.fixture
    def mock_position(self, mocker):
        """Returns a class-wide mocked position."""
        mock = mocker.MagicMock()
        mock.id = 1
        return mock

    @pytest.mark.asyncio
    async def test_validation(self, session, mocker, app, fpl, mock_obj):
        """Assert the api data is valid."""
        mocker.patch("data_updater.updaters.players.apply_update")
        mocker.patch.object(players.Position, "find", return_value=mock_obj)
        mocker.patch.object(players.Team, "find", return_value=mock_obj)
        players_json = await players.update(app=app, fpl=fpl)
        schema = Player.__marshmallow__()
        for player_json in players_json:
            player = schema.load(player_json, session=session)
            assert player
            assert isinstance(player, Player)

    @pytest.mark.asyncio
    async def test_update(self, mocker, app, fpl, mock_obj):
        """Assert the player data is updated."""
        mocker.patch.object(players.Position, "find", return_value=mock_obj)
        mocker.patch.object(players.Team, "find", return_value=mock_obj)
        assert Player.count() == 0
        await players.update(app=app, fpl=fpl)
        assert Player.count() != 0
