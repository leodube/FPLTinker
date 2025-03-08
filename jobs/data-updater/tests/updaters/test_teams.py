"""Test suite to ensure the teams updater is working as expected."""

import pytest
from fpltinker.models import Team

from data_updater.updaters import teams


@pytest.mark.usefixtures("session", "mocker", "app", "fpl")
class TestTeamsUpdater:
    """The class pytest grouping for the teams updater."""

    @pytest.mark.asyncio
    async def test_validation(self, session, mocker, app, fpl):
        """Assert the api data is valid."""
        mocker.patch("data_updater.updaters.teams.apply_update")
        teams_json = await teams.update(app=app, fpl=fpl)
        schema = Team.__marshmallow__()
        for team_json in teams_json:
            team = schema.load(team_json, session=session)
            assert team
            assert isinstance(team, Team)

    @pytest.mark.asyncio
    async def test_update(self, app, fpl):
        """Assert the team data is updated."""
        assert Team.count() == 0
        await teams.update(app=app, fpl=fpl)
        assert Team.count() != 0
