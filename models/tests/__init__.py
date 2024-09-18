"""Factory methods for the models test suites."""

from copy import deepcopy

from models.data import (
    configuration_sample,
    fdr_sample,
    fixture_sample,
    fixture_stat_sample,
    gameweek_sample,
    player_sample,
    player_stats_sample,
    player_sample,
    position_sample,
    stat_details_sample,
    team_sample,
)
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


def factory_configuration(**kwargs):
    """Create a configuration entity."""
    data = deepcopy(configuration_sample)
    data.update({**kwargs})
    configuration = Configuration(**data)
    configuration.save()
    return configuration


def factory_fdr(**kwargs):
    """Create a fdr entity."""
    data = deepcopy(fdr_sample)
    data.update({**kwargs})
    fdr = FDR(**data)
    fdr.save()
    return fdr


def factory_fixture_stat(**kwargs):
    """Create a fixture stat entity."""
    data = deepcopy(fixture_stat_sample)
    data.update({**kwargs})
    fixture_stat = FixtureStat(**data)
    fixture_stat.save()
    return fixture_stat


def factory_fixture(**kwargs):
    """Create a fixture entity."""
    data = deepcopy(fixture_sample)
    data.update({**kwargs})
    fixture = Fixture(**data)
    fixture.save()
    return fixture


def factory_gameweek(**kwargs):
    """Create a gameweek entity."""
    data = deepcopy(gameweek_sample)
    data.update({**kwargs})
    gameweek = Gameweek(**data)
    gameweek.save()
    return gameweek


def factory_player_stats(**kwargs):
    """Create a player stats entity."""
    data = deepcopy(player_stats_sample)
    data.update({**kwargs})
    player_stats = PlayerStats(**data)
    player_stats.save()
    return player_stats


def factory_player(**kwargs):
    """Create a player entity."""
    data = deepcopy(player_sample)
    data.update({**kwargs})
    player = Player(**data)
    player.save()
    return player


def factory_position(**kwargs):
    """Create a position entity."""
    data = deepcopy(position_sample)
    data.update({**kwargs})
    position = Position(**data)
    position.save()
    return position


def factory_stat_details(**kwargs):
    """Create a stat details entity."""
    data = deepcopy(stat_details_sample)
    data.update({**kwargs})
    stat_details = StatDetails(**data)
    stat_details.save()
    return stat_details


def factory_team(**kwargs):
    """Create a team entity."""
    data = deepcopy(team_sample)
    data.update({**kwargs})
    team = Team(**data)
    team.save()
    return team
