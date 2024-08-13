"""PlayerStats model"""

from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .db import db


class PlayerStats(Base):
    """A class representing a player's stats in Fantasy Premier League."""

    __versioned__ = {}
    __tablename__ = "player_stats"

    # FPL api properties
    assists: Mapped[int]
    bonus: Mapped[int]
    bps: Mapped[int]
    clean_sheets: Mapped[int]
    clean_sheets_per_90: Mapped[int]
    cost_change_event: Mapped[int]
    cost_change_event_fall: Mapped[int]
    cost_change_start: Mapped[int]
    cost_change_start_fall: Mapped[int]
    creativity: Mapped[str]
    dreamteam_count: Mapped[int]
    event_points: Mapped[int]
    expected_assists: Mapped[str]
    expected_assists_per_90: Mapped[int]
    expected_goal_involvements: Mapped[str]
    expected_goal_involvements_per_90: Mapped[int]
    expected_goals: Mapped[str]
    expected_goals_per_90: Mapped[int]
    expected_goals_conceded: Mapped[str]
    expected_goals_conceded_per_90: Mapped[int]
    form: Mapped[str]
    goals_conceded: Mapped[int]
    goals_conceded_per_90: Mapped[int]
    goals_scored: Mapped[int]
    ict_index: Mapped[str]
    influence: Mapped[str]
    minutes: Mapped[int]
    now_cost: Mapped[int]
    own_goals: Mapped[int]
    penalties_missed: Mapped[int]
    penalties_saved: Mapped[int]
    points_per_game: Mapped[str]
    red_cards: Mapped[int]
    saves: Mapped[int]
    saves_per_90: Mapped[int]
    selected_by_percent: Mapped[str]
    starts: Mapped[int]
    starts_per_90: Mapped[int]
    threat: Mapped[str]
    total_points: Mapped[int]
    transfers_in: Mapped[int]
    transfers_in_event: Mapped[int]
    transfers_out: Mapped[int]
    transfers_out_event: Mapped[int]
    value_form: Mapped[str]
    value_season: Mapped[str]
    yellow_cards: Mapped[int]

    # Foreign keys
    player_id: Mapped[int] = mapped_column(
        db.ForeignKey("players.id"), sort_order=-1
    )
