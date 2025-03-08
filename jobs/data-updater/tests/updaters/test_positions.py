"""Test suite to ensure the positions updater is working as expected."""

import pytest
from fpltinker.models import Position

from data_updater.updaters import positions


@pytest.mark.usefixtures("session", "mocker", "app", "fpl")
class TestPositionsUpdater:
    """The class pytest grouping for the positions updater."""

    @pytest.mark.asyncio
    async def test_validation(self, session, mocker, app, fpl):
        """Assert the api data is valid."""
        mocker.patch("data_updater.updaters.positions.apply_update")
        positions_json = await positions.update(app=app, fpl=fpl)
        schema = Position.__marshmallow__()
        for position_json in positions_json:
            position = schema.load(position_json, session=session)
            assert position
            assert isinstance(position, Position)

    @pytest.mark.asyncio
    async def test_update(self, app, fpl):
        """Assert the position data is updated."""
        assert Position.count() == 0
        await positions.update(app=app, fpl=fpl)
        assert Position.count() != 0
