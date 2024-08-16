"""Description"""

from flask_restx import fields


class BaseMarshal:
    """Description"""

    fixture: dict = {
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

    gameweek: dict = {
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
        "highestScoringEntry": fields.Integer(
            attribute="highest_scoring_entry"
        ),
        "mostCaptained": fields.Integer(attribute="most_captained"),
        "mostSelected": fields.Integer(attribute="most_selected"),
        "mostTransferredIn": fields.Integer(attribute="most_transferred_in"),
        "mostViceCaptained": fields.Integer(attribute="most_vice_captained"),
        "releaseTime": fields.DateTime(attribute="release_time"),
        "topElement": fields.Integer(attribute="top_element"),
        "topElementInfo": fields.String(attribute="top_element_info"),
        "season": fields.Integer,
    }

    player: dict = {
        "fplId": fields.Integer(attribute="fpl_id"),
        "firstName": fields.String(attribute="first_name"),
        "secondName": fields.String(attribute="second_name"),
        "webName": fields.String(attribute="web_name"),
        "team": {
            "fplId": fields.Integer(attribute="team_id"),
        },
        "position": {
            "fplId": fields.Integer(attribute="position_id"),
        },
        "squadNumber": fields.Integer(attribute="squad_number"),
        "status": fields.String(attribute="fpl_id"),
        "news": fields.String(attribute="fpl_id"),
        "newsSdded": fields.String(attribute="news_added"),
        "penaltiesOrder": fields.Integer(attribute="penalties_order"),
        "chanceOfPlaying": {
            "nextRound": fields.Integer(
                attribute="chance_of_playing_next_round"
            ),
            "thisRound": fields.Integer(
                attribute="chance_of_playing_this_round"
            ),
        },
        "cornersAndIndirectFreekicks": {
            "order": fields.Integer(
                attribute="corners_and_indirect_freekicks_order"
            ),
            "text": fields.String(
                attribute="corners_and_indirect_freekicks_text"
            ),
        },
        "direcFreekicks": {
            "order": fields.Integer(attribute="direct_freekicks_order"),
            "text": fields.String(attribute="direct_freekicks_text"),
        },
        "season": fields.Integer,
    }

    player_stats: dict = {
        "id": fields.Integer(),
        "playerId": fields.Integer(attribute="player_id"),
        "assists": fields.Integer(),
        "bonus": fields.Integer(),
        "bps": fields.Integer(),
        "clean_sheets": fields.Integer(attribute="clean_sheets"),
        "clean_sheets_per_90": fields.Fixed(
            decimals=2, attribute="clean_sheets_per_90"
        ),
        "cost_change_event": fields.Integer(attribute="cost_change_event"),
        "cost_change_event_fall": fields.Integer(
            attribute="cost_change_event_fall"
        ),
        "cost_change_start": fields.Integer(attribute="cost_change_start"),
        "cost_change_start_fall": fields.Integer(
            attribute="cost_change_start_fall"
        ),
        "creativity": fields.Fixed(decimals=1),
        "dreamteam_count": fields.Integer(attribute="dreamteam_count"),
        "event_points": fields.Integer(attribute="event_points"),
        "expected_assists": fields.Fixed(
            decimal=2, attribute="expected_assists"
        ),
        "expected_assists_per_90": fields.Fixed(
            decimal=2, attribute="expected_assists_per_90"
        ),
        "expected_goal_involvements": fields.Fixed(
            decimal=2, attribute="expected_goal_involvements"
        ),
        "expected_goal_involvements_per_90": fields.Fixed(
            decimal=2, attribute="expected_goal_involvements_per_90"
        ),
        "expected_goals": fields.Fixed(decimal=2, attribute="expected_goals"),
        "expected_goals_per_90": fields.Fixed(
            decimal=2, attribute="expected_goals_per_90"
        ),
        "expected_goals_conceded": fields.Fixed(
            decimal=2, attribute="expected_goals_conceded"
        ),
        "expected_goals_conceded_per_90": fields.Fixed(
            decimal=2, attribute="expected_goals_conceded_per_90"
        ),
        "goals_conceded": fields.Integer(attribute="goals_conceded"),
        "goals_conceded_per_90": fields.Fixed(
            decimal=2, attribute="goals_conceded_per_90"
        ),
        "goals_scored": fields.Integer(attribute="goals_scored"),
        "ict_index": fields.Fixed(decimal=1, attribute="ict_index"),
        "influence": fields.Fixed(decimal=1),
        "minutes": fields.Integer(),
        "now_cost": fields.Integer(attribute="now_cost"),
        "own_goals": fields.Integer(attribute="own_goals"),
        "penalties_missed": fields.Integer(attribute="penalties_missed"),
        "penalties_saved": fields.Integer(attribute="penalties_saved"),
        "points_per_game": fields.Fixed(decimal=1, attribute="points_per_game"),
        "red_cards": fields.Integer(attribute="red_cards"),
        "saves": fields.Integer(),
        "saves_per_90": fields.Integer(attribute="saves_per_90"),
        "selected_by_percent": fields.Fixed(
            decimal=1, attribute="selected_by_percent"
        ),
        "starts": fields.Integer(attribute="player_id"),
        "starts_per_90": fields.Fixed(decimal=2, attribute="starts_per_90"),
        "threat": fields.Integer(),
        "total_points": fields.Integer(attribute="total_points"),
        "transfers_in": fields.Integer(attribute="transfers_in"),
        "transfers_in_event": fields.Integer(attribute="transfers_in_event"),
        "transfers_out": fields.Integer(attribute="transfers_out"),
        "transfers_out_event": fields.Integer(attribute="transfers_out_event"),
        "value_form": fields.Integer(attribute="value_form"),
        "value_season": fields.Fixed(decimal=1, attribute="value_season"),
        "yellow_cards": fields.Integer(attribute="yellow_cards"),
        "season": fields.Integer,
    }

    position: dict = {
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

    stat_details: dict = {
        "name": fields.String(),
        "label": fields.String(),
        "description": fields.String(),
    }

    team: dict = {
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
        "strengthOverallHome": fields.Integer(
            attribute="strength_overall_home"
        ),
        "strengthOverallAway": fields.Integer(
            attribute="strength_overall_away"
        ),
        "strengthAttackHome": fields.Integer(attribute="strength_attack_home"),
        "strengthAttackAway": fields.Integer(attribute="strength_attack_away"),
        "strengthDefenceHome": fields.Integer(
            attribute="strength_defence_home"
        ),
        "strengthDefenceAway": fields.Integer(
            attribute="strength_defence_away"
        ),
        "season": fields.Integer,
    }
