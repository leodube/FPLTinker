"""Contains date helper methods"""

from datetime import datetime


def is_today(datetime_obj: datetime):
    """Checks if a given date is today."""
    date = datetime_obj.date()
    today = datetime.now().date()
    return date == today
