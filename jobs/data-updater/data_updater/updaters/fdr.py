"""The database updater for the FDR model."""

from flask import Flask
from fpl import FPL
from fpltinker.models import FDR, Configuration, Team

from data_updater.utils.db_utilities import apply_update


async def update(app: Flask, fpl: FPL) -> dict:
    """Updates the fixture difficulty rankings fom the FPL api."""
    if not (app.config.get("FLAGS", {}).get("fdr")):
        return

    app.logger.debug("Updating FDRs.")

    api_fdr = await fpl.FDR()
    season = Configuration.get("season")

    # Update fdr
    fdr = []
    for team_name, rankings in api_fdr.items():
        team = Team.find(name=team_name, season=season)
        for _type, ranking in rankings.items():
            fdr.append(
                {
                    "team_id": team.id,
                    "team_name": team_name,
                    "_type": FDR.FDRTypes[_type.upper()],
                    "home": ranking["H"],
                    "away": ranking["A"],
                    "season": season,
                }
            )

    # Apply updates to db
    apply_update(app, FDR, fdr)
    return fdr
