"""Test suite to ensure the position model is working as expected."""

from copy import deepcopy

import pytest
from sqlalchemy.exc import IntegrityError

from models.models import Position
from tests import factory_position, position_data


@pytest.mark.usefixtures("session")
class TestPosition:
    """The class pytest grouping for the position model."""

    @pytest.fixture
    def data(self) -> dict:
        """Returns a class-wide copy of the position data object."""
        return deepcopy(position_data)

    def test_save(self):
        """Assert the position can be saved."""
        position = factory_position()
        assert position.id

    def test_save_with_conflict(self):
        """Assert the position won't be saved if constraints violated."""
        factory_position()
        with pytest.raises(IntegrityError):
            factory_position()

    def test_delete(self):
        """Assert the position can be deleted."""
        position = factory_position()
        assert position.id
        position.delete()
        assert Position.count() == 0

    def test_all(self):
        """Assert all entries can be found for the position."""
        for i in range(num_positions := 5):
            factory_position(fpl_id=i, singular_name=f"position {i}")
        assert len(Position.all()) == num_positions

    def test_count(self):
        """Assert a count of all position entries can be found."""
        for i in range(num_positions := 5):
            factory_position(fpl_id=i, singular_name=f"position {i}")
        assert Position.count() == num_positions

    def test_exists(self):
        """Assert a position entry exists."""
        position = factory_position()
        assert Position.exists(position)

    def test_find(self, data):
        """Assert a matching position object can be found."""
        position = factory_position(**data)
        assert position == Position.find(**data)

    def test_find_all(self, data):
        """Assert all matching position object can be found."""
        for i in range(num_positions := 5):
            data.update({"fpl_id": i, "singular_name": f"position {i}"})
            factory_position(**data)
        del data["fpl_id"]
        del data["singular_name"]
        results = Position.find_all(**data)
        assert results and len(results.all()) == num_positions

    def test_index_constraints(self, db, metadata):
        """Assert the index constraints are unique."""
        table = metadata.tables["positions"]
        table_constraint = next(
            (
                constraint
                for constraint in table.constraints
                if isinstance(constraint, db.UniqueConstraint)
            ),
            None,
        )
        assert table_constraint
        for index_constraint in Position.index_constraints():
            assert table_constraint.contains_column(table.c[index_constraint])
