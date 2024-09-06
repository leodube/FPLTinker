"""Test suite to ensure the FDR model is working as expected."""

from copy import deepcopy

import pytest
from sqlalchemy.exc import IntegrityError

from models.models import FDR, Team
from tests import factory_fdr, factory_team, fdr_data


@pytest.mark.usefixtures("session")
class TestFDR:
    """The class pytest grouping for the fdr model."""

    @pytest.fixture
    def team(self) -> Team:
        """Returns a class-wide team instance."""
        return factory_team()

    @pytest.fixture
    def data(self, team) -> dict:
        """Returns a class-wide copy of the fdr data object."""
        _data = deepcopy(fdr_data)
        _data.update({"team_id": team.id})
        return _data

    def test_save(self, team):
        """Assert the fdr can be saved."""
        fdr = factory_fdr(team_id=team.id)
        assert fdr.id

    def test_save_with_conflict(self, team):
        """Assert the fdr won't be saved if constraints violated."""
        factory_fdr(team_id=team.id)
        with pytest.raises(IntegrityError):
            factory_fdr(team_id=team.id)

    def test_delete(self, team):
        """Assert the fdr can be deleted."""
        fdr = factory_fdr(team_id=team.id)
        assert fdr.id
        fdr.delete()
        assert FDR.count() == 0

    def test_all(self, team):
        """Assert all entries can be found for the fdr."""
        types = FDR.FDRTypes.list()
        for i in range(num_fdrs := 5):
            factory_fdr(team_id=team.id, _type=types[i])
        assert len(FDR.all()) == num_fdrs

    def test_count(self, team):
        """Assert a count of all fdr entries can be found."""
        types = FDR.FDRTypes.list()
        for i in range(num_fdrs := 5):
            factory_fdr(team_id=team.id, _type=types[i])
        assert FDR.count() == num_fdrs

    def test_find(self, data):
        """Assert a matching fdr object can be found."""
        fdr = factory_fdr(**data)
        assert fdr == FDR.find(**data)

    def test_find_instance(self, data):
        """Assert a matching fdr object can be found."""
        created = factory_fdr(**data)
        keys = FDR.__dict__.keys()
        fdr = FDR(**{key: data[key] for key in keys if key in data})
        found = FDR.find_instance(fdr)
        assert created == found

    def test_find_all(self, data):
        """Assert all matching fdr object can be found."""
        types = FDR.FDRTypes.list()
        for i in range(num_fdrs := 5):
            data.update({"_type": types[i]})
            factory_fdr(**data)
        del data["_type"]
        results = FDR.find_all(**data)
        assert results and len(results.all()) == num_fdrs

    def test_index_constraints(self, db, metadata):
        """Assert the index constraints are unique."""
        table = metadata.tables["fdr"]
        table_constraint = next(
            (
                constraint
                for constraint in table.constraints
                if isinstance(constraint, db.UniqueConstraint)
            ),
            None,
        )
        assert table_constraint
        for index_constraint in FDR.index_constraints():
            assert table_constraint.contains_column(table.c[index_constraint])
