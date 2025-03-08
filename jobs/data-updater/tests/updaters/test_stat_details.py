"""Test suite to ensure the stat details updater is working as expected."""

import pytest
from fpltinker.models import StatDetails

from data_updater.updaters import stat_details


@pytest.mark.usefixtures("session", "mocker", "app")
class TestStatDetailssUpdater:
    """The class pytest grouping for the stat details updater."""

    def test_validation(self, session, mocker, app):
        """Assert the api data is valid."""
        mocker.patch("data_updater.updaters.stat_details.apply_update")
        stat_details_json = stat_details.update(app=app)
        schema = StatDetails.__marshmallow__()
        for stat_detail_json in stat_details_json:
            stat_detail = schema.load(stat_detail_json, session=session)
            assert stat_detail
            assert isinstance(stat_detail, StatDetails)

    def test_update(self, app):
        """Assert the stat details data is updated."""
        assert StatDetails.count() == 0
        stat_details.update(app=app)
        assert StatDetails.count() != 0
