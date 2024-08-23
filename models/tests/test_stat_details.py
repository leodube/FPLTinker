"""Test suite to ensure the stat details model is working as expected."""

from copy import deepcopy

import pytest

from models.models import StatDetails
from tests import factory_stat_details, stat_details_data


@pytest.mark.usefixtures("session")
class TestStatDetails:
    """The class pytest grouping for the stat details model."""

    @pytest.fixture
    def data(self) -> dict:
        """Returns a class-wide copy of the stat details data object."""
        return deepcopy(stat_details_data)

    def test_save(self):
        """Assert the stat details can be saved."""
        stat_details = factory_stat_details()
        assert stat_details.id

    def test_delete(self):
        """Assert the stat details can be deleted."""
        stat_details = factory_stat_details()
        assert stat_details.id
        stat_details.delete()
        assert StatDetails.count() == 0

    def test_all(self):
        """Assert all entries can be found for the stat details."""
        for i in range(num_stat_details := 5):
            factory_stat_details(name=f"stat details {i}")
        assert len(StatDetails.all()) == num_stat_details

    def test_count(self):
        """Assert a count of all stat details entries can be found."""
        for i in range(num_stat_details := 5):
            factory_stat_details(name=f"stat details {i}")
        assert StatDetails.count() == num_stat_details

    def test_find(self, data):
        """Assert a matching stat details object can be found."""
        stat_details = factory_stat_details(**data)
        assert stat_details == StatDetails.find(**data)

    def test_find_all(self, data):
        """Assert all matching stat details object can be found."""
        for i in range(num_stat_details := 5):
            data.update({"name": f"stat details {i}"})
            factory_stat_details(**data)
        del data["name"]
        results = StatDetails.find_all(**data)
        assert results and len(results.all()) == num_stat_details

    def test_index_constraints(self, db, metadata):
        """Assert the index constraints are unique."""
        table = metadata.tables["stat_details"]
        table_constraint = next(
            (
                constraint
                for constraint in table.constraints
                if isinstance(constraint, db.UniqueConstraint)
            ),
            None,
        )
        assert table_constraint
        for index_constraint in StatDetails.index_constraints():
            assert table_constraint.contains_column(table.c[index_constraint])

    def test_bulk_upsert(self, data):
        """Assert entries can be inserted and updated."""
        # Test inserting entries
        stat_details = []
        for i in range(num_stat_details_inserted := 5):
            data.update({"name": f"stat details {i}"})
            stat_details.append(deepcopy(data))
        StatDetails.bulk_upsert(stat_details)
        assert StatDetails.count() == num_stat_details_inserted

        # Test updating entries
        stat_details = []
        for i in range(3):
            data.update({"name": f"stat details {i}", "label": "new label"})
            stat_details.append(deepcopy(data))
        StatDetails.bulk_upsert(stat_details)
        assert StatDetails.count() == num_stat_details_inserted
