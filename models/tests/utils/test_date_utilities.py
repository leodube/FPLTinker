"""Test suite to ensure the date utilities are working as expected."""

import pytest

from models.models.utils.date_utilities import add_to_season


@pytest.mark.parametrize(
    "season,to_add,result",
    [
        (20242025, 0, 20242025),
        (20242025, 1, 20252026),
        (20242025, 3, 20272028),
        (20242025, -1, 20232024),
        (20242025, -3, 20212022),
    ],
)
def test_add_to_season(season, to_add, result):
    """Assert the adding and subtracting to a season is done correctly."""
    assert add_to_season(season=season, to_add=to_add) == result
