"""Contains Flask-RestX custom marshalling fields."""

from flask_restx import fields
from models import Configuration, Team


class TeamField(fields.Raw):
    """Custom FPL team marshalling field."""

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
