"""The database updater for the fixture stats model."""

from flask import Flask
from fpl import FPL
from fpltinker.models import Configuration, Fixture, FixtureStat, Player, StatDetails

from data_updater.utils.db_utilities import apply_update


async def update(app: Flask, fpl: FPL) -> dict:
    """Updates the fixtures stats fom the FPL api."""
    if not (app.config.get("FLAGS", {}).get("fixtureStats")):
        return

    app.logger.debug("Updating fixtures stats.")

    api_fixtures = await fpl.get_fixtures(return_json=True)
    season = Configuration.get("season")

    # Update fixture stats
    fixture_stats = []
    for af in api_fixtures:
        # Return if no fixture stats
        f = af.copy()
        if not f["stats"]:
            import pprint

            if f["event"] == 3:
                pprint.pprint(f)
            continue

        fixture = Fixture.find(fpl_id=f["id"], season=season)

        import pprint

        for stat in f["stats"]:
            pprint.pprint(stat)
            stat_details_id = StatDetails.find(name=stat["identifier"]).id

            # Get away stats
            if away_stats := stat["a"]:
                for away_stat in away_stats:
                    away_stat = {
                        "fixture_id": fixture.id,
                        "team_id": fixture.team_h_id,
                        "player_id": Player.find(
                            fpl_id=away_stat["element"], season=season
                        ).id,
                        "stat_details_id": stat_details_id,
                        "value": away_stat["value"],
                    }
                    fixture_stats.append(away_stat)

            # Get home stats
            if home_stats := stat["h"]:
                for home_stat in home_stats:
                    home_stat = {
                        "fixture_id": fixture.id,
                        "team_id": fixture.team_h_id,
                        "player_id": Player.find(
                            fpl_id=home_stat["element"], season=season
                        ).id,
                        "stat_details_id": stat_details_id,
                        "value": home_stat["value"],
                    }
                    fixture_stats.append(home_stat)

    # Apply updates to db
    apply_update(app, FixtureStat, fixture_stats)
    return fixture_stats
