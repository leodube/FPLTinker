"""Test suite to ensure the gameweek model is working as expected."""

from copy import deepcopy

import pytest

from models.models import Gameweek
from tests import (
    factory_gameweek,
    gameweek_data,
)


@pytest.mark.usefixtures("session")
class TestGameweek:
    @pytest.fixture
    def data(self) -> dict:
        return deepcopy(gameweek_data)

    def test_save(self):
        """Assert the gameweek can be saved."""
        gameweek = factory_gameweek()
        assert gameweek.id

    def test_delete(self):
        """Assert the gameweek can be deleted."""
        gameweek = factory_gameweek()
        assert gameweek.id
        gameweek.delete()
        assert Gameweek.count() == 0

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

    def test_bulk_upsert(self, data):
        """Assert entries can be inserted and updated."""
        # Test inserting entries
        gameweeks = []
        for i in range(num_gameweeks_inserted := 5):
            data.update({"fpl_id": i, "name": f"gameweek {i}"})
            gameweeks.append(deepcopy(data))
        Gameweek.bulk_upsert(gameweeks)
        assert Gameweek.count() == num_gameweeks_inserted

        # Test updating entries
        gameweeks = []
        for i in range(3):
            data.update({"fpl_id": i, "name": f"new name {i}"})
            gameweeks.append(deepcopy(data))
        Gameweek.bulk_upsert(gameweeks)
        assert Gameweek.count() == num_gameweeks_inserted
