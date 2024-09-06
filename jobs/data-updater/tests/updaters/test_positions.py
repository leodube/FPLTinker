"""Test suite to ensure the positions updater is working as expected."""

import pytest
from models import Position

from data_updater.updaters import positions


@pytest.mark.usefixtures("app", "fpl", "session")
class TestPositionsUpdater:
    """The class pytest grouping for the positions updater."""

    @pytest.mark.asyncio
    async def test_update(self, app, fpl):
        """Assert the position data is updated."""
        assert Position.count() == 0
        await positions.update(app=app, fpl=fpl)
        assert Position.count() != 0

    @pytest.mark.asyncio
    async def test_only_run_daily(self, app, fpl):
        """Confirm the updater only runs once per day."""
        assert Position.count() == 0
        await positions.update(app=app, fpl=fpl)
        assert (count := Position.count()) != 0
        await positions.update(app=app, fpl=fpl)
        assert count == Position.count()
