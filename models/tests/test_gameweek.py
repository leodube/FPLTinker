"""Test suite to ensure the gameweek model is working as expected."""

from copy import deepcopy

import pytest
from sqlalchemy.exc import IntegrityError

from models.models import Gameweek
from tests import factory_gameweek, gameweek_data


@pytest.mark.usefixtures("session")
class TestGameweek:
    """The class pytest grouping for the gameweek model."""

    @pytest.fixture
    def data(self) -> dict:
        """Returns a class-wide copy of the gameweek data object."""
        return deepcopy(gameweek_data)

    def test_save(self):
        """Assert the gameweek can be saved."""
        gameweek = factory_gameweek()
        assert gameweek.id

    def test_save_with_conflict(self):
        """Assert the gameweek won't be saved if constraints violated."""
        factory_gameweek()
        with pytest.raises(IntegrityError):
            factory_gameweek()

    def test_delete(self):
        """Assert the gameweek can be deleted."""
        gameweek = factory_gameweek()
        assert gameweek.id
        gameweek.delete()
        assert Gameweek.count() == 0

    def test_serialize(self):
        """Assert the gameweek object can be serialized."""
        gameweek = factory_gameweek()
        assert gameweek.serialize()

    def test_all(self):
        """Assert all entries can be found for the gameweek."""
        for i in range(num_gameweeks := 5):
            factory_gameweek(fpl_id=i, name=f"gameweek {i}")
        assert len(Gameweek.all()) == num_gameweeks

    def test_count(self):
        """Assert a count of all gameweek entries can be found."""
        for i in range(num_gameweeks := 5):
            factory_gameweek(fpl_id=i, name=f"gameweek {i}")
        assert Gameweek.count() == num_gameweeks

    def test_find(self, data):
        """Assert a matching gameweek object can be found."""
        gameweek = factory_gameweek(**data)
        assert gameweek == Gameweek.find(**data)

    def test_find_instance(self, data):
        """Assert a matching gameweek object can be found."""
        created = factory_gameweek(**data)
        keys = Gameweek.__dict__.keys()
        team = Gameweek(**{key: data[key] for key in keys if key in data})
        found = Gameweek.find_instance(team)
        assert created == found

    def test_find_all(self, data):
        """Assert all matching gameweek object can be found."""
        for i in range(num_gameweeks := 5):
            data.update({"fpl_id": i, "name": f"gameweek {i}"})
            factory_gameweek(**data)
        del data["fpl_id"]
        del data["name"]
        results = Gameweek.find_all(**data)
        assert results and len(results.all()) == num_gameweeks

    def test_index_constraints(self, db, metadata):
        """Assert the index constraints are unique."""
        table = metadata.tables["gameweeks"]
        table_constraint = next(
            (
                constraint
                for constraint in table.constraints
                if isinstance(constraint, db.UniqueConstraint)
            ),
            None,
        )
        assert table_constraint
        for index_constraint in Gameweek.index_constraints():
            assert table_constraint.contains_column(table.c[index_constraint])
