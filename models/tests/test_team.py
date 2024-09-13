"""Test suite to ensure the team model is working as expected."""

from copy import deepcopy

import pytest
from sqlalchemy.exc import IntegrityError

from models.models import Team

# from models.schemas import Schema
from tests import factory_team, team_data


@pytest.mark.usefixtures("session")
class TestTeam:
    """The class pytest grouping for the team model."""

    @pytest.fixture
    def data(self) -> dict:
        """Returns a class-wide copy of the team data object."""
        return deepcopy(team_data)

    def test_save(self):
        """Assert the team can be saved."""
        team = factory_team()
        assert team.id

    def test_save_with_conflict(self):
        """Assert the team won't be saved if constraints violated."""
        factory_team()
        with pytest.raises(IntegrityError):
            factory_team()

    def test_delete(self):
        """Assert the team can be deleted."""
        team = factory_team()
        assert team.id
        team.delete()
        assert Team.count() == 0

    def test_serialize(self):
        """Assert the team object can be serialized."""
        team = factory_team()
        assert team.serialize()

    # TODO: Add test_diff tests to rest of models
    def test_diff(self):
        """Assert the team object can be diffed."""
        team_1 = factory_team(code=1, name=f"team 1")
        team_2 = factory_team(code=2, name=f"team 2")
        diff = team_1.diff(team_2, exclude=("id",))
        assert diff
        assert "code" in diff.affected_root_keys
        assert "name" in diff.affected_root_keys

    def test_all(self):
        """Assert all entries can be found for the team."""
        for i in range(num_teams := 5):
            factory_team(code=i, name=f"team {i}")
        assert len(Team.all()) == num_teams

    def test_count(self):
        """Assert a count of all team entries can be found."""
        for i in range(num_teams := 5):
            factory_team(code=i, name=f"team {i}")
        assert Team.count() == num_teams

    def test_find(self, data):
        """Assert a matching team object can be found."""
        team = factory_team(**data)
        assert team == Team.find(**data)

    def test_find_instance(self, data):
        """Assert a matching team object can be found."""
        created = factory_team(**data)
        keys = Team.__dict__.keys()
        team = Team(**{key: data[key] for key in keys if key in data})
        found = Team.find_instance(team)
        assert created == found

    def test_find_all(self, data):
        """Assert all matching team object can be found."""
        for i in range(num_teams := 5):
            data.update({"code": i, "name": f"team {i}"})
            factory_team(**data)
        del data["code"]
        del data["name"]
        results = Team.find_all(**data)
        assert results and len(results.all()) == num_teams

    def test_index_constraints(self, db, metadata):
        """Assert the index constraints are unique."""
        table = metadata.tables["teams"]
        table_constraint = next(
            (
                constraint
                for constraint in table.constraints
                if isinstance(constraint, db.UniqueConstraint)
            ),
            None,
        )
        assert table_constraint
        for index_constraint in Team.index_constraints():
            assert table_constraint.contains_column(table.c[index_constraint])
