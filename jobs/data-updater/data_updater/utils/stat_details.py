"""Holds the stat details."""

# pylint: skip-file;
# flake8: noqa


stat_details: dict = {
    "total_points": {
        "description": "Total points earned this season.",
        "label": "Total points",
    },
    "event_points": {
        "description": "Total points earned in the latest Gameweek.",
        "label": "Round points",
    },
    "now_cost": {
        "description": "Current buying price in the transfer market.",
        "label": "Price",
    },
    "selected_by_percent": {
        "description": "The percentage of overall Fantasy managers who currently own the player.",
        "label": "Team selected by %",
    },
    "minutes": {
        "description": "Total minutes played this season.",
        "label": "Minutes played",
    },
    "goals_scored": {
        "description": "Total goals scored this season.",
        "label": "Goals scored",
    },
    "assists": {
        "description": "Total goal assists - awarded to the player from the goalscoring team who makes the final pass before a goal is scored, including own goals.",
        "label": "Assists",
    },
    "clean_sheets": {
        "description": "Total clean sheets - awarded to players who do not concede a goal and have played at least 60 minutes.",
        "label": "Clean sheets",
    },
    "goals_conceded": {
        "description": "Total number of goals conceded by a team while the player has been on the pitch.",
        "label": "Goals conceded",
    },
    "own_goals": {
        "description": "Awarded to a player who puts the ball into his own team's goal.",
        "label": "Own goals",
    },
    "penalties_saved": {
        "description": "Awarded to a goalkeeper who touches the ball when saving a penalty.",
        "label": "Penalties saved",
    },
    "penalties_missed": {
        "description": "Awarded to a player who takes a penalty but does not score from the penalty spot.",
        "label": "Penalties missed",
    },
    "yellow_cards": {
        "description": "Total yellow cards this season.",
        "label": "Yellow cards",
    },
    "red_cards": {
        "description": "Total red cards this season.",
        "label": "Red cards",
    },
    "saves": {
        "description": "Total times a goalkeeper has saved a shot on goal.",
        "label": "Saves",
    },
    "bonus": {
        "description": "The three best performing players in each match according to the BPS will receive additional bonus points - 3 points will be awarded to the highest scoring player, 2 to the second best and 1 to the third.",
        "label": "Bonus",
    },
    "bps": {
        "description": "The Bonus Points System (BPS) uses a range of stats to create a BPS score for each player. The three best performing players in each match will be awarded bonus points.",
        "label": "Bonus Points System",
    },
    "influence": {
        "description": "Influence evaluates a player's impact on a match, taking into account actions that could directly or indirectly affect the match outcome. Part of the ICT index.",
        "label": "Influence",
    },
    "creativity": {
        "description": "Creativity assesses player performance in terms of producing goalscoring opportunities for other players. Part of the ICT index.",
        "label": "Creativity",
    },
    "threat": {
        "description": "Threat gauges players who are most likely to score goals. Part of the ICT index.",
        "label": "Threat",
    },
    "ict_index": {
        "description": "Statistical index developed specifically to assess a player as an FPL asset, combining Influence, Creativity and Threat scores.",
        "label": "ICT Index",
    },
    "form": {
        "description": "Form is a player's average score per match, calculated from all matches played by his club in the last 30 days.",
        "label": "Form",
    },
    "dreamteam_count": {
        "description": "The number of times a player has been selected in a Gameweek Dream Team. Players with the most points in a Gameweek in a valid formation earn a place in the Dream Team.",
        "label": "Times in Dream Team",
    },
    "value_form": {
        "description": "Player's form divided by player's value.",
        "label": "Value (form)",
    },
    "value_season": {
        "description": "Player's total points divided by player's value.",
        "label": "Value (season)",
    },
    "points_per_game": {
        "description": "Player's total points divided by player's number of matches.",
        "label": "Points per match",
    },
    "transfers_in": {
        "description": "Total number of times a player has been transferred in to a team this season.",
        "label": "Transfers in",
    },
    "transfers_out": {
        "description": "Total number of times a player has been transferred out of a team this season.",
        "label": "Transfers out",
    },
    "transfers_in_event": {
        "description": "Total number of times a player has been transferred in to a team this Gameweek.",
        "label": "Transfers in (round)",
    },
    "transfers_out_event": {
        "description": "Total number of times a player has been transferred out of a team this Gameweek.",
        "label": "Transfers out (round)",
    },
    "cost_change_start": {
        "description": "How much a player's price has increased since the start of the season.",
        "label": "Price rise",
    },
    "cost_change_start_fall": {
        "description": "How much a player price has fallen since the start of the season.",
        "label": "Price fall",
    },
    "cost_change_event": {
        "description": "How much a player's price has increased this Gameweek.",
        "label": "Price rise (round)",
    },
    "cost_change_event_fall": {
        "description": "How much a player's price has fallen this Gameweek.",
        "label": "Price fall (round)",
    },
    "expected_assists": {
        "description": "Expected assists since the start of the season",
        "label": "xA (Total)",
    },
    "expected_goals": {
        "description": "Expected goals since the start of the season",
        "label": "xG (Total)",
    },
    "expected_goal_involvements": {
        "description": "Expected goal involvements since the start of the season",
        "label": "xGI (Total)",
    },
    "expected_goals_conceded": {
        "description": "Expected goals conceded since the start of the season",
        "label": "xGC (Total)",
    },
    "starts": {
        "description": "Total games started this season",
        "label": "Starts",
    },
}


def get_stat_details(name: str):
    return stat_details.get(name, None)
