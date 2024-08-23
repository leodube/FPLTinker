# Details

Date : 2024-08-21 20:53:35

Directory /Users/leodube/repos/FPLTinker

Total : 112 files,  12611 codes, 253 comments, 1250 blanks, all 14114 lines

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)

## Files
| filename | language | code | comment | blank | total |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [.github/ISSUE_TEMPLATE/bug_report.md](/.github/ISSUE_TEMPLATE/bug_report.md) | Markdown | 21 | 0 | 7 | 28 |
| [.github/ISSUE_TEMPLATE/feature_request.md](/.github/ISSUE_TEMPLATE/feature_request.md) | Markdown | 13 | 0 | 5 | 18 |
| [README.md](/README.md) | Markdown | 1 | 0 | 0 | 1 |
| [api/Makefile](/api/Makefile) | Makefile | 24 | 6 | 11 | 41 |
| [api/README.md](/api/README.md) | Markdown | 0 | 0 | 1 | 1 |
| [api/api/__init__.py](/api/api/__init__.py) | Python | 12 | 0 | 6 | 18 |
| [api/api/config.py](/api/api/config.py) | Python | 16 | 1 | 8 | 25 |
| [api/api/resources/__init__.py](/api/api/resources/__init__.py) | Python | 25 | 0 | 8 | 33 |
| [api/api/resources/fixture.py](/api/api/resources/fixture.py) | Python | 23 | 0 | 11 | 34 |
| [api/api/resources/gameweek.py](/api/api/resources/gameweek.py) | Python | 28 | 0 | 12 | 40 |
| [api/api/resources/marshalling/__init__.py](/api/api/resources/marshalling/__init__.py) | Python | 7 | 0 | 3 | 10 |
| [api/api/resources/marshalling/base_marshal.py](/api/api/resources/marshalling/base_marshal.py) | Python | 187 | 0 | 11 | 198 |
| [api/api/resources/marshalling/detailed_marshal.py](/api/api/resources/marshalling/detailed_marshal.py) | Python | 26 | 0 | 10 | 36 |
| [api/api/resources/marshalling/fields.py](/api/api/resources/marshalling/fields.py) | Python | 19 | 0 | 5 | 24 |
| [api/api/resources/player.py](/api/api/resources/player.py) | Python | 23 | 0 | 11 | 34 |
| [api/api/resources/position.py](/api/api/resources/position.py) | Python | 23 | 0 | 11 | 34 |
| [api/api/resources/stat_details.py](/api/api/resources/stat_details.py) | Python | 22 | 0 | 11 | 33 |
| [api/api/resources/team.py](/api/api/resources/team.py) | Python | 23 | 0 | 11 | 34 |
| [api/poetry.lock](/api/poetry.lock) | TOML | 916 | 1 | 88 | 1,005 |
| [api/pyproject.toml](/api/pyproject.toml) | TOML | 22 | 0 | 5 | 27 |
| [api/setup.cfg](/api/setup.cfg) | Properties | 8 | 0 | 2 | 10 |
| [api/tests/__init__.py](/api/tests/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [api/wsgi.py](/api/wsgi.py) | Python | 8 | 0 | 3 | 11 |
| [jobs/data-updater/Makefile](/jobs/data-updater/Makefile) | Makefile | 24 | 6 | 11 | 41 |
| [jobs/data-updater/README.md](/jobs/data-updater/README.md) | Markdown | 1 | 0 | 0 | 1 |
| [jobs/data-updater/data_updater/__init__.py](/jobs/data-updater/data_updater/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [jobs/data-updater/data_updater/config.py](/jobs/data-updater/data_updater/config.py) | Python | 16 | 1 | 8 | 25 |
| [jobs/data-updater/data_updater/updaters/__init__.py](/jobs/data-updater/data_updater/updaters/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [jobs/data-updater/data_updater/updaters/configurations.py](/jobs/data-updater/data_updater/updaters/configurations.py) | Python | 23 | 5 | 10 | 38 |
| [jobs/data-updater/data_updater/updaters/fixture_stats.py](/jobs/data-updater/data_updater/updaters/fixture_stats.py) | Python | 42 | 5 | 12 | 59 |
| [jobs/data-updater/data_updater/updaters/fixtures.py](/jobs/data-updater/data_updater/updaters/fixtures.py) | Python | 22 | 8 | 12 | 42 |
| [jobs/data-updater/data_updater/updaters/gameweeks.py](/jobs/data-updater/data_updater/updaters/gameweeks.py) | Python | 21 | 12 | 12 | 45 |
| [jobs/data-updater/data_updater/updaters/player_stats.py](/jobs/data-updater/data_updater/updaters/player_stats.py) | Python | 19 | 27 | 13 | 59 |
| [jobs/data-updater/data_updater/updaters/players.py](/jobs/data-updater/data_updater/updaters/players.py) | Python | 21 | 8 | 13 | 42 |
| [jobs/data-updater/data_updater/updaters/positions.py](/jobs/data-updater/data_updater/updaters/positions.py) | Python | 22 | 8 | 12 | 42 |
| [jobs/data-updater/data_updater/updaters/stat_details.py](/jobs/data-updater/data_updater/updaters/stat_details.py) | Python | 14 | 1 | 8 | 23 |
| [jobs/data-updater/data_updater/updaters/teams.py](/jobs/data-updater/data_updater/updaters/teams.py) | Python | 18 | 5 | 11 | 34 |
| [jobs/data-updater/data_updater/updaters/utils/__init__.py](/jobs/data-updater/data_updater/updaters/utils/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [jobs/data-updater/data_updater/updaters/utils/config_details.py](/jobs/data-updater/data_updater/updaters/utils/config_details.py) | Python | 11 | 2 | 6 | 19 |
| [jobs/data-updater/data_updater/updaters/utils/date_utilities.py](/jobs/data-updater/data_updater/updaters/utils/date_utilities.py) | Python | 7 | 0 | 4 | 11 |
| [jobs/data-updater/data_updater/updaters/utils/db_utilities.py](/jobs/data-updater/data_updater/updaters/utils/db_utilities.py) | Python | 20 | 0 | 9 | 29 |
| [jobs/data-updater/data_updater/updaters/utils/stat_details.py](/jobs/data-updater/data_updater/updaters/utils/stat_details.py) | Python | 161 | 2 | 6 | 169 |
| [jobs/data-updater/data_updater/worker.py](/jobs/data-updater/data_updater/worker.py) | Python | 30 | 0 | 5 | 35 |
| [jobs/data-updater/logging.conf](/jobs/data-updater/logging.conf) | Properties | 22 | 0 | 7 | 29 |
| [jobs/data-updater/poetry.lock](/jobs/data-updater/poetry.lock) | TOML | 1,507 | 1 | 118 | 1,626 |
| [jobs/data-updater/pyproject.toml](/jobs/data-updater/pyproject.toml) | TOML | 23 | 0 | 5 | 28 |
| [jobs/data-updater/setup.cfg](/jobs/data-updater/setup.cfg) | Properties | 8 | 0 | 2 | 10 |
| [jobs/data-updater/tests/__init__.py](/jobs/data-updater/tests/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [jobs/data-updater/update.py](/jobs/data-updater/update.py) | Python | 31 | 0 | 10 | 41 |
| [models/Makefile](/models/Makefile) | Makefile | 47 | 10 | 18 | 75 |
| [models/README.md](/models/README.md) | Markdown | 0 | 0 | 1 | 1 |
| [models/__init__.py](/models/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [models/config.py](/models/config.py) | Python | 39 | 2 | 20 | 61 |
| [models/manage.py](/models/manage.py) | Python | 11 | 0 | 7 | 18 |
| [models/migrations/alembic.ini](/models/migrations/alembic.ini) | Ini | 38 | 0 | 13 | 51 |
| [models/migrations/env.py](/models/migrations/env.py) | Python | 61 | 17 | 30 | 108 |
| [models/migrations/versions/441b4b9fc5e8_add_unique_constraint_to_positions.py](/models/migrations/versions/441b4b9fc5e8_add_unique_constraint_to_positions.py) | Python | 19 | 5 | 10 | 34 |
| [models/migrations/versions/628ad57a5e52_add_precision_to_player_stats.py](/models/migrations/versions/628ad57a5e52_add_precision_to_player_stats.py) | Python | 280 | 5 | 11 | 296 |
| [models/migrations/versions/687a81484bb8_make_season_columns_nullable.py](/models/migrations/versions/687a81484bb8_make_season_columns_nullable.py) | Python | 37 | 5 | 21 | 63 |
| [models/migrations/versions/6cec9828deda_remove_timestamps_from_some_stat_tables.py](/models/migrations/versions/6cec9828deda_remove_timestamps_from_some_stat_tables.py) | Python | 66 | 5 | 13 | 84 |
| [models/migrations/versions/77a166b6cfab_add_season_to_player_stats.py](/models/migrations/versions/77a166b6cfab_add_season_to_player_stats.py) | Python | 22 | 5 | 13 | 40 |
| [models/migrations/versions/7abb62dc2072_initial_migration.py](/models/migrations/versions/7abb62dc2072_initial_migration.py) | Python | 367 | 5 | 9 | 381 |
| [models/migrations/versions/922abbe6544e_add_unique_constraint_on_player_stats.py](/models/migrations/versions/922abbe6544e_add_unique_constraint_on_player_stats.py) | Python | 22 | 5 | 11 | 38 |
| [models/migrations/versions/a38dc19f6106_implement_fixture_stats_table.py](/models/migrations/versions/a38dc19f6106_implement_fixture_stats_table.py) | Python | 63 | 5 | 11 | 79 |
| [models/migrations/versions/bc190cfbc015_update_gameweek_to_support_timestamp.py](/models/migrations/versions/bc190cfbc015_update_gameweek_to_support_timestamp.py) | Python | 41 | 5 | 11 | 57 |
| [models/migrations/versions/c2cfd4d8096d_add_gameweek_relationship_on_fixture.py](/models/migrations/versions/c2cfd4d8096d_add_gameweek_relationship_on_fixture.py) | Python | 27 | 5 | 13 | 45 |
| [models/migrations/versions/c99e5c4a209a_update_top_player_for_a_gameweek.py](/models/migrations/versions/c99e5c4a209a_update_top_player_for_a_gameweek.py) | Python | 34 | 5 | 11 | 50 |
| [models/migrations/versions/e5c85bd667cb_update_unique_key_on_teams.py](/models/migrations/versions/e5c85bd667cb_update_unique_key_on_teams.py) | Python | 17 | 5 | 11 | 33 |
| [models/migrations/versions/edd961afb15c_add_configurations_table.py](/models/migrations/versions/edd961afb15c_add_configurations_table.py) | Python | 40 | 5 | 9 | 54 |
| [models/models/__init__.py](/models/models/__init__.py) | Python | 31 | 0 | 3 | 34 |
| [models/models/base.py](/models/models/base.py) | Python | 77 | 2 | 23 | 102 |
| [models/models/configuration.py](/models/models/configuration.py) | Python | 61 | 1 | 15 | 77 |
| [models/models/db.py](/models/models/db.py) | Python | 23 | 0 | 9 | 32 |
| [models/models/fixture.py](/models/models/fixture.py) | Python | 36 | 5 | 13 | 54 |
| [models/models/fixture_stat.py](/models/models/fixture_stat.py) | Python | 20 | 3 | 9 | 32 |
| [models/models/gameweek.py](/models/models/gameweek.py) | Python | 39 | 6 | 14 | 59 |
| [models/models/player.py](/models/models/player.py) | Python | 54 | 5 | 15 | 74 |
| [models/models/player_stats.py](/models/models/player_stats.py) | Python | 67 | 5 | 12 | 84 |
| [models/models/position.py](/models/models/position.py) | Python | 29 | 4 | 12 | 45 |
| [models/models/stat_details.py](/models/models/stat_details.py) | Python | 14 | 2 | 8 | 24 |
| [models/models/team.py](/models/models/team.py) | Python | 36 | 4 | 12 | 52 |
| [models/models/tinker.py](/models/models/tinker.py) | Python | 5 | 0 | 5 | 10 |
| [models/models/utils/__init__.py](/models/models/utils/__init__.py) | Python | 0 | 0 | 1 | 1 |
| [models/models/utils/date_utilities.py](/models/models/utils/date_utilities.py) | Python | 3 | 0 | 3 | 6 |
| [models/models/weighting.py](/models/models/weighting.py) | Python | 5 | 0 | 5 | 10 |
| [models/poetry.lock](/models/poetry.lock) | TOML | 685 | 1 | 70 | 756 |
| [models/pyproject.toml](/models/pyproject.toml) | TOML | 26 | 0 | 6 | 32 |
| [models/setup.cfg](/models/setup.cfg) | Properties | 8 | 0 | 2 | 10 |
| [models/tests/__init__.py](/models/tests/__init__.py) | Python | 246 | 0 | 30 | 276 |
| [models/tests/conftest.py](/models/tests/conftest.py) | Python | 45 | 2 | 14 | 61 |
| [models/tests/test_configuration.py](/models/tests/test_configuration.py) | Python | 166 | 2 | 18 | 186 |
| [models/tests/test_fixture.py](/models/tests/test_fixture.py) | Python | 116 | 2 | 19 | 137 |
| [models/tests/test_fixture_stats.py](/models/tests/test_fixture_stats.py) | Python | 182 | 2 | 22 | 206 |
| [models/tests/test_gameweek.py](/models/tests/test_gameweek.py) | Python | 74 | 2 | 15 | 91 |
| [models/tests/test_player.py](/models/tests/test_player.py) | Python | 102 | 2 | 17 | 121 |
| [models/tests/test_player_stats.py](/models/tests/test_player_stats.py) | Python | 104 | 2 | 16 | 122 |
| [models/tests/test_position.py](/models/tests/test_position.py) | Python | 71 | 2 | 15 | 88 |
| [models/tests/test_stat_details.py](/models/tests/test_stat_details.py) | Python | 70 | 2 | 15 | 87 |
| [models/tests/test_team.py](/models/tests/test_team.py) | Python | 71 | 2 | 15 | 88 |
| [models/tests/test_tinker.py](/models/tests/test_tinker.py) | Python | 0 | 0 | 1 | 1 |
| [models/tests/test_weighting.py](/models/tests/test_weighting.py) | Python | 0 | 0 | 1 | 1 |
| [web/.eslintrc.json](/web/.eslintrc.json) | JSON with Comments | 3 | 0 | 1 | 4 |
| [web/README.md](/web/README.md) | Markdown | 23 | 0 | 14 | 37 |
| [web/app/globals.css](/web/app/globals.css) | CSS | 29 | 0 | 5 | 34 |
| [web/app/layout.tsx](/web/app/layout.tsx) | TypeScript JSX | 16 | 0 | 3 | 19 |
| [web/app/page.tsx](/web/app/page.tsx) | TypeScript JSX | 3 | 0 | 0 | 3 |
| [web/next.config.mjs](/web/next.config.mjs) | JavaScript | 2 | 1 | 2 | 5 |
| [web/package-lock.json](/web/package-lock.json) | JSON | 5,251 | 0 | 1 | 5,252 |
| [web/package.json](/web/package.json) | JSON | 26 | 0 | 1 | 27 |
| [web/postcss.config.mjs](/web/postcss.config.mjs) | JavaScript | 6 | 1 | 2 | 9 |
| [web/tailwind.config.ts](/web/tailwind.config.ts) | TypeScript | 19 | 0 | 2 | 21 |
| [web/tsconfig.json](/web/tsconfig.json) | JSON with Comments | 26 | 0 | 1 | 27 |

[Summary](results.md) / Details / [Diff Summary](diff.md) / [Diff Details](diff-details.md)