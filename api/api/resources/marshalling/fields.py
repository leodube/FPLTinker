"""Contains Flask-RestX custom marshalling fields."""

from flask_restx import fields
import simplejson as json
from models import Configuration, FDR, Team


class FDRField(fields.Raw):
    """Custom FPL FDR marshalling field."""

    def format(self, value):
        fdrs = FDR.find_all(team_id=value, season=Configuration.get("season"))
        return {
            fdr._type.name.lower(): {
                "home": json.dumps(fdr.home, use_decimal=True),
                "away": json.dumps(fdr.away, use_decimal=True),
            }
            for fdr in fdrs
        }


class TeamField(fields.Raw):
    """Custom FPL team marshalling field."""

    def format(self, value):
        team = Team.find(fpl_id=value, season=Configuration.get("season"))
        fdrs = FDR.find_all(team_id=value, season=Configuration.get("season"))
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
            "fdr": {
                fdr._type.name.lower(): {
                    "home": json.dumps(fdr.home, use_decimal=True),
                    "away": json.dumps(fdr.away, use_decimal=True),
                }
                for fdr in fdrs
            },
        }
