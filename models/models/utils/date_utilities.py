"""Contains date helper methods"""


def add_to_season(season: int, to_add: int) -> int:
    """Add or subtract from a season."""
    return season + (to_add * 10001)
