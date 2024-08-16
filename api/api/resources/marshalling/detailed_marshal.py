"""Description"""

from flask_restx import fields
from models import Configuration, Team

from . import BaseMarshal


class TeamField(fields.Raw):
    def format(self, value):
        team = Team.find(fpl_id=value, season=Configuration.get("season"))
        return {
            "fplId": team.fpl_id,
            "name": team.name,
            "shortName": team.short_name,
            "position": team.position,
            "points": team.points,
            "played": team.played,
            "win": team.win,
            "draw": team.draw,
            "loss": team.loss,
            "form": team.form,
        }


class DetailedMarshal:
    """Description"""

    fixture: dict = {
        "teams": {
            "away": TeamField(attribute="team_a_id"),
            "home": TeamField(attribute="team_h_id"),
        },
        "gameweek": fields.Nested(BaseMarshal.fixture),
    }

    gameweek: dict = {
        "fixtures": fields.List(fields.Nested(BaseMarshal.gameweek))
    }

    player: dict = {
        "team": fields.Nested(BaseMarshal.team),
        "position": fields.Nested(BaseMarshal.position),
    }

    position: dict = {
        "players": fields.List(fields.Nested(BaseMarshal.position))
    }

    team: dict = {"players": fields.List(fields.Nested(BaseMarshal.team))}
