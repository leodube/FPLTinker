"""Factory methods for the models test suites."""

from copy import deepcopy

from models.models import (
    FDR,
    Configuration,
    Fixture,
    FixtureStat,
    Gameweek,
    Player,
    PlayerStats,
    Position,
    StatDetails,
    Team,
)

configuration_data = {
    "name": "config name",
    "value": "12345",
    "_type": Configuration.ConfigurationTypes.INTEGER,
    "description": "config description",
}

fdr_data = {
    "team_id": 1,
    "team_name": "Arsenal",
    "_type": FDR.FDRTypes.ALL,
    "home": 1,
    "away": 0.5,
    "season": 20242025,
}

fixture_stat_data = {
    "fixture_id": 1,
    "team_id": 1,
    "stat_details_id": 1,
    "player_id": 1,
    "value": 1,
}

fixture_data = {
    "fpl_id": 1,
    "code": 1,
    "finished": True,
    "finished_provisional": True,
    "kickoff_time": "2024-08-16 19:00:00",
    "minutes": 90,
    "provisional_start_time": False,
    "started": True,
    "team_a_difficulty": 2,
    "team_a_score": 1,
    "team_h_difficulty": 3,
    "team_h_score": 1,
    "gameweek_id": 1,
    "team_a_id": 1,
    "team_h_id": 2,
    "season": 20242025,
}

gameweek_data = {
    "fpl_id": 1,
    "name": "Gameweek 1",
    "average_entry_score": 57,
    "data_checked": True,
    "deadline_time": "2024-08-16 17:30:00",
    "finished": True,
    "is_current": True,
    "is_next": False,
    "is_previous": False,
    "ranked_count": 8597356,
    "transfers_made": 0,
    "highest_score": 127,
    "highest_scoring_entry": None,
    "most_captained": None,
    "most_selected": None,
    "most_transferred_in": None,
    "most_vice_captained": None,
    "release_time": None,
    "top_player_id": None,
    "season": 20242025,
}

player_stats_data = {
    "player_id": 1,
    "assists": 12,
    "bonus": 29,
    "bps": 776,
    "clean_sheets": 16,
    "clean_sheets_per_90": 0.49,
    "cost_change_event": 0,
    "cost_change_event_fall": 0,
    "cost_change_start": 0,
    "cost_change_start_fall": 0,
    "creativity": 1319.8,
    "dreamteam_count": 0,
    "event_points": 0,
    "expected_assists": 10.9,
    "expected_assists_per_90": 0.34,
    "expected_goal_involvements": 26.29,
    "expected_goal_involvements_per_90": 0.81,
    "expected_goals": 15.4,
    "expected_goals_per_90": 0.47,
    "expected_goals_conceded": 25.66,
    "expected_goals_conceded_per_90": 0.79,
    "form": 0,
    "goals_conceded": 27,
    "goals_conceded_per_90": 0.83,
    "goals_scored": 16,
    "ict_index": 375.7,
    "influence": 1093.8,
    "minutes": 2922,
    "now_cost": 100,
    "own_goals": 0,
    "penalties_missed": 0,
    "penalties_saved": 0,
    "points_per_game": 6.5,
    "red_cards": 0,
    "saves": 0,
    "saves_per_90": 0,
    "selected_by_percent": 31.9,
    "starts": 35,
    "starts_per_90": 1.08,
    "threat": 1342,
    "total_points": 226,
    "transfers_in": 0,
    "transfers_in_event": 0,
    "transfers_out": 0,
    "transfers_out_event": 0,
    "value_form": 0,
    "value_season": 22.6,
    "yellow_cards": 4,
    "season": 20242025,
}

player_data = {
    "fpl_id": 17,
    "code": 223340,
    "team_id": 1,
    "position_id": 1,
    "first_name": "Bukayo",
    "second_name": "Saka",
    "web_name": "Saka",
    "squad_number": None,
    "team_code": 3,
    "status": Player.PlayerStatuses.AVAILABLE.value,
    "news": "",
    "news_added": None,
    "penalties_order": 1,
    "chance_of_playing_next_round": None,
    "chance_of_playing_this_round": None,
    "corners_and_indirect_freekicks_order": 1,
    "corners_and_indirect_freekicks_text": None,
    "direct_freekicks_order": None,
    "direct_freekicks_text": None,
    "season": 20242025,
}

position_data = {
    "fpl_id": 1,
    "plural_name": "Midfielders",
    "plural_name_short": "MID",
    "singular_name": "Midfielder",
    "singular_name_short": "MID",
    "squad_select": 5,
    "squad_min_play": 2,
    "squad_max_play": 5,
    "ui_shirt_specific": False,
    "element_count": 276,
    "season": 20242025,
}

stat_details_data = {
    "name": "total_points",
    "label": "Total points",
    "description": "Total points earned this season.",
}

team_data = {
    "fpl_id": 1,
    "code": 1,
    "name": "Arsenal",
    "short_name": "ARS",
    "position": 0,
    "points": 0,
    "played": 0,
    "win": 0,
    "draw": 0,
    "loss": 0,
    "form": None,
    "strength": 5,
    "team_division": None,
    "unavailable": False,
    "strength_overall_home": 1350,
    "strength_overall_away": 1380,
    "strength_attack_home": 1370,
    "strength_attack_away": 1370,
    "strength_defence_home": 1330,
    "strength_defence_away": 1390,
    "season": 20242025,
}


def factory_configuration(**kwargs):
    """Create a configuration entity."""
    data = deepcopy(configuration_data)
    data.update({**kwargs})
    configuration = Configuration(**data)
    configuration.save()
    return configuration


def factory_fdr(**kwargs):
    """Create a fdr entity."""
    data = deepcopy(fdr_data)
    data.update({**kwargs})
    fdr = FDR(**data)
    fdr.save()
    return fdr


def factory_fixture_stat(**kwargs):
    """Create a fixture stat entity."""
    data = deepcopy(fixture_stat_data)
    data.update({**kwargs})
    fixture_stat = FixtureStat(**data)
    fixture_stat.save()
    return fixture_stat


def factory_fixture(**kwargs):
    """Create a fixture entity."""
    data = deepcopy(fixture_data)
    data.update({**kwargs})
    fixture = Fixture(**data)
    fixture.save()
    return fixture


def factory_gameweek(**kwargs):
    """Create a gameweek entity."""
    data = deepcopy(gameweek_data)
    data.update({**kwargs})
    gameweek = Gameweek(**data)
    gameweek.save()
    return gameweek


def factory_player_stats(**kwargs):
    """Create a player stats entity."""
    data = deepcopy(player_stats_data)
    data.update({**kwargs})
    player_stats = PlayerStats(**data)
    player_stats.save()
    return player_stats


def factory_player(**kwargs):
    """Create a player entity."""
    data = deepcopy(player_data)
    data.update({**kwargs})
    player = Player(**data)
    player.save()
    return player


def factory_position(**kwargs):
    """Create a position entity."""
    data = deepcopy(position_data)
    data.update({**kwargs})
    position = Position(**data)
    position.save()
    return position


def factory_stat_details(**kwargs):
    """Create a stat details entity."""
    data = deepcopy(stat_details_data)
    data.update({**kwargs})
    stat_details = StatDetails(**data)
    stat_details.save()
    return stat_details


def factory_team(**kwargs):
    """Create a team entity."""
    data = deepcopy(team_data)
    data.update({**kwargs})
    team = Team(**data)
    team.save()
    return team
