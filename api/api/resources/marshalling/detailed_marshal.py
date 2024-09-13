"""Contains Flask-RestX detailed response marshalling."""

from flask_restx import fields

from .base_marshal import BaseMarshal
from .fields import TeamField


class DetailedMarshal:  # pylint: disable=too-few-public-methods
    """The marshalling object that contains the input layouts."""

    fixture: dict = {
        "teams": {
            "away": TeamField(attribute="team_a_id"),
            "home": TeamField(attribute="team_h_id"),
        },
        "gameweek": fields.Nested(BaseMarshal.gameweek),
    }

    gameweek: dict = {
        "topPlayer": fields.Nested(
            BaseMarshal.player, attribute="top_player", allow_null=True
        ),
        "fixtures": fields.List(fields.Nested(BaseMarshal.fixture)),
    }

    player: dict = {
        "team": fields.Nested(BaseMarshal.team),
        "position": fields.Nested(BaseMarshal.position),
        "stats": fields.Nested(BaseMarshal.player_stats),
    }

    position: dict = {"players": fields.List(fields.Nested(BaseMarshal.player))}

    team: dict = {
        "players": fields.List(fields.Nested(BaseMarshal.player)),
    }
