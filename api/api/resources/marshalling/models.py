"""Description"""

from flask_restx import fields
from .fields import TeamField

gameweek_dict: dict = {
    "fplId": fields.Integer(attribute="fpl_id"),
    "name": fields.String,
    "averageEntryScore": fields.Integer(attribute="average_entry_score"),
    "dataChecked": fields.Boolean(attribute="data_checked"),
    "deadlineTime": fields.DateTime(attribute="deadline_time"),
    "finished": fields.Boolean,
    "isCurrent": fields.Boolean(attribute="is_current"),
    "isNext": fields.Boolean(attribute="is_next"),
    "isPrevious": fields.Boolean(attribute="is_previous"),
    "rankedCount": fields.Integer(attribute="ranked_count"),
    "transfersMade": fields.Integer(attribute="transfers_made"),
    "highestScore": fields.Integer(attribute="highest_score"),
    "highestScoringEntry": fields.Integer(attribute="highest_scoring_entry"),
    "mostCaptained": fields.Integer(attribute="most_captained"),
    "mostSelected": fields.Integer(attribute="most_selected"),
    "mostTransferredIn": fields.Integer(attribute="most_transferred_in"),
    "mostViceCaptained": fields.Integer(attribute="most_vice_captained"),
    "releaseTime": fields.DateTime(attribute="release_time"),
    "topElement": fields.Integer(attribute="top_element"),
    "topElementInfo": fields.String(attribute="top_element_info"),
    "season": fields.Integer,
}

fixture_dict: dict = {
    "fplId": fields.Integer(attribute="fpl_id"),
    "finished": fields.Boolean,
    "kickoffTime": fields.DateTime(attribute="kickoff_time"),
    "minutes": fields.Integer,
    "started": fields.Boolean,
    "season": fields.Integer,
    "difficulty": {
        "away": fields.Integer(attribute="team_a_difficulty"),
        "home": fields.Integer(attribute="team_h_difficulty"),
    },
    "score": {
        "away": fields.Integer(attribute="team_a_score"),
        "home": fields.Integer(attribute="team_h_score"),
    },
    "teams": {
        "away": {
            "fplId": fields.Integer(attribute="team_a_id"),
        },
        "home": {
            "fplId": fields.Integer(attribute="team_h_id"),
        },
    },
    "gameweek": {"fplId": fields.Integer(attribute="gameweek_id")},
}

player_dict: dict = {
    "fplId": fields.Integer(attribute="fpl_id"),
    "firstName": fields.String(attribute="first_name"),
    "secondName": fields.String(attribute="second_name"),
    "webName": fields.String(attribute="web_name"),
    "teamId": fields.Integer(attribute="team_id"),
    "positionId": fields.Integer(attribute="position_id"),
    "squadNumber": fields.Integer(attribute="squad_number"),
    "status": fields.String(attribute="fpl_id"),
    "news": fields.String(attribute="fpl_id"),
    "newsSdded": fields.String(attribute="news_added"),
    "penaltiesOrder": fields.Integer(attribute="penalties_order"),
    "chanceOfPlaying": {
        "nextRound": fields.Integer(attribute="chance_of_playing_next_round"),
        "thisRound": fields.Integer(attribute="chance_of_playing_this_round"),
    },
    "cornersAndIndirectFreekicks": {
        "order": fields.Integer(
            attribute="corners_and_indirect_freekicks_order"
        ),
        "text": fields.String(attribute="corners_and_indirect_freekicks_text"),
    },
    "direcFreekicks": {
        "order": fields.Integer(attribute="direct_freekicks_order"),
        "text": fields.String(attribute="direct_freekicks_text"),
    },
    "season": fields.Integer,
}

position_dict: dict = {
    "fplId": fields.Integer(attribute="fpl_id"),
    "pluralName": fields.String(attribute="plural_name"),
    "pluralNameShort": fields.String(attribute="plural_name_short"),
    "singularName": fields.String(attribute="singular_name"),
    "singularNameShort": fields.String(attribute="singular_name_short"),
    "squadSelect": fields.Integer(attribute="squad_select"),
    "squadMinPlay": fields.Integer(attribute="squad_min_play"),
    "squadMaxPlay": fields.Integer(attribute="squad_max_play"),
    "uiShirtSpecific": fields.Boolean(attribute="ui_shirt_specific"),
    "elementCount": fields.Integer(attribute="element_count"),
    "season": fields.Integer,
}

team_dict: dict = {
    "fplId": fields.Integer(attribute="fpl_id"),
    "name": fields.String(),
    "shortName": fields.String(attribute="short_name"),
    "position": fields.Integer,
    "points": fields.Integer,
    "played": fields.Integer,
    "win": fields.Integer,
    "draw": fields.Integer,
    "loss": fields.Integer,
    "form": fields.Integer,
    "strength": fields.Integer,
    "teamDivision": fields.Integer(attribute="team_division"),
    "strengthOverallHome": fields.Integer(attribute="strength_overall_home"),
    "strengthOverallAway": fields.Integer(attribute="strength_overall_away"),
    "strengthAttackHome": fields.Integer(attribute="strength_attack_home"),
    "strengthAttackAway": fields.Integer(attribute="strength_attack_away"),
    "strengthDefenceHome": fields.Integer(attribute="strength_defence_home"),
    "strengthDefenceAway": fields.Integer(attribute="strength_defence_away"),
    "season": fields.Integer,
}

fixture_details_dict: dict = {
    "teams": {
        "away": TeamField(attribute="team_a"),
        "home": TeamField(attribute="team_h"),
    },
    "gameweek": fields.Nested(gameweek_dict),
}

gameweek_details_dict: dict = {
    "fixtures": fields.List(fields.Nested(fixture_dict))
}

position_details_dict: dict = {
    "players": fields.List(fields.Nested(player_dict))
}

team_details_dict: dict = {"players": fields.List(fields.Nested(player_dict))}
