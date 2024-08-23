"""PlayerStats model"""

from decimal import Decimal
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, WithTimestamps
from .db import db


class PlayerStats(Base, WithTimestamps):
    """A class representing a player's stats in Fantasy Premier League."""

    __tablename__ = "player_stats"
    __table_args__ = (db.UniqueConstraint("player_id", "season"),)

    # FPL api properties
    assists: Mapped[int]
    bonus: Mapped[int]
    bps: Mapped[int]
    clean_sheets: Mapped[int]
    clean_sheets_per_90: Mapped[Decimal]
    cost_change_event: Mapped[int]
    cost_change_event_fall: Mapped[int]
    cost_change_start: Mapped[int]
    cost_change_start_fall: Mapped[int]
    creativity: Mapped[Decimal]
    dreamteam_count: Mapped[int]
    event_points: Mapped[int]
    expected_assists: Mapped[Decimal]
    expected_assists_per_90: Mapped[Decimal]
    expected_goal_involvements: Mapped[Decimal]
    expected_goal_involvements_per_90: Mapped[Decimal]
    expected_goals: Mapped[Decimal]
    expected_goals_per_90: Mapped[Decimal]
    expected_goals_conceded: Mapped[Decimal]
    expected_goals_conceded_per_90: Mapped[Decimal]
    form: Mapped[Decimal]
    goals_conceded: Mapped[int]
    goals_conceded_per_90: Mapped[Decimal]
    goals_scored: Mapped[int]
    ict_index: Mapped[Decimal]
    influence: Mapped[Decimal]
    minutes: Mapped[int]
    now_cost: Mapped[int]
    own_goals: Mapped[int]
    penalties_missed: Mapped[int]
    penalties_saved: Mapped[int]
    points_per_game: Mapped[Decimal]
    red_cards: Mapped[int]
    saves: Mapped[int]
    saves_per_90: Mapped[Decimal]
    selected_by_percent: Mapped[Decimal]
    starts: Mapped[int]
    starts_per_90: Mapped[Decimal]
    threat: Mapped[Decimal]
    total_points: Mapped[int]
    transfers_in: Mapped[int]
    transfers_in_event: Mapped[int]
    transfers_out: Mapped[int]
    transfers_out_event: Mapped[int]
    value_form: Mapped[Decimal]
    value_season: Mapped[Decimal]
    yellow_cards: Mapped[int]

    # Additional properties
    season: Mapped[Optional[int]]

    # Foreign keys
    player_id: Mapped[int] = mapped_column(db.ForeignKey("players.id"), sort_order=-1)

    # Relationships
    player: Mapped["Player"] = db.relationship(
        back_populates="stats", viewonly=True, init=False
    )

    # Methods
    @classmethod
    def index_constraints(cls) -> list:
        """Return the constraints that the upsert will use to identify
        conflicts"""
        return ["player_id", "season"]
