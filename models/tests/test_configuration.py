"""Test suite to ensure the configuration model is working as expected."""

from copy import deepcopy

import pytest
from sqlalchemy.exc import IntegrityError

from models.models import Configuration
from tests import configuration_data, factory_configuration


@pytest.mark.usefixtures("session")
class TestConfiguration:
    """The class pytest grouping for the configuration model."""

    @pytest.fixture
    def data(self) -> dict:
        """Returns a class-wide copy of the configuration data object."""
        return deepcopy(configuration_data)

    def test_save(self):
        """Assert the configuration can be saved."""
        configuration = factory_configuration()
        assert configuration.id

    def test_save_with_conflict(self):
        """Assert the configuration won't be saved if constraints violated."""
        factory_configuration()
        with pytest.raises(IntegrityError):
            factory_configuration()

    def test_delete(self):
        """Assert the configuration can be deleted."""
        configuration = factory_configuration()
        assert configuration.id
        configuration.delete()
        assert Configuration.count() == 0

    def test_all(self):
        """Assert all entries can be found for the configuration."""
        for i in range(num_configs := 5):
            factory_configuration(name=f"config {i}")
        assert len(Configuration.all()) == num_configs

    def test_count(self):
        """Assert a count of all configuration entries can be found."""
        for i in range(num_configs := 5):
            factory_configuration(name=f"config {i}")
        assert Configuration.count() == num_configs

    def test_exists(self):
        """Assert a configuration entry exists."""
        configuration = factory_configuration()
        assert Configuration.exists(configuration)

    def test_find(self, data):
        """Assert a matching configuration object can be found."""
        config = factory_configuration(**data)
        assert config == Configuration.find(**data)

    def test_find_all(self, data):
        """Assert all matching configuration object can be found."""
        for i in range(num_configs := 5):
            data.update({"name": f"config {i}"})
            factory_configuration(**data)
        del data["name"]
        results = Configuration.find_all(**data)
        assert results and len(results.all()) == num_configs

    def test_find_by_name(self):
        """Assert all configuration object can be found by name."""
        test_name = "config name"
        factory_configuration(name=test_name)
        result = Configuration.find_by_name(name=test_name)
        assert result and result.name == test_name

    @pytest.mark.parametrize(
        "value,_type,error",
        [
            ("string", Configuration.ConfigurationTypes.STRING, False),
            ("string", Configuration.ConfigurationTypes.INTEGER, True),
            ("string", Configuration.ConfigurationTypes.BOOLEAN, False),
            ("123", Configuration.ConfigurationTypes.INTEGER, False),
            ("123", Configuration.ConfigurationTypes.STRING, False),
            ("123", Configuration.ConfigurationTypes.BOOLEAN, False),
            ("True", Configuration.ConfigurationTypes.BOOLEAN, False),
            ("True", Configuration.ConfigurationTypes.STRING, False),
            ("True", Configuration.ConfigurationTypes.INTEGER, True),
        ],
    )
    def test_cast_value(self, value, _type, error):
        """Assert the configuration value is cast to the correct type."""
        if error:
            with pytest.raises(ValueError):
                Configuration.cast_value(value=value, _type=_type)
        else:
            value = Configuration.cast_value(value=value, _type=_type)
            assert value

    @pytest.mark.parametrize(
        "name,value,_type,error",
        [
            (
                "string_as_string",
                "string",
                Configuration.ConfigurationTypes.STRING,
                False,
            ),
            (
                "string_as_integer",
                "string",
                Configuration.ConfigurationTypes.INTEGER,
                True,
            ),
            (
                "string_as_boolean",
                "string",
                Configuration.ConfigurationTypes.BOOLEAN,
                False,
            ),
            (
                "integer_as_integer",
                "123",
                Configuration.ConfigurationTypes.INTEGER,
                False,
            ),
            (
                "integer_as_string",
                "123",
                Configuration.ConfigurationTypes.STRING,
                False,
            ),
            (
                "integer_as_boolean",
                "123",
                Configuration.ConfigurationTypes.BOOLEAN,
                False,
            ),
            (
                "boolean_as_boolean",
                "True",
                Configuration.ConfigurationTypes.BOOLEAN,
                False,
            ),
            (
                "boolean_as_string",
                "True",
                Configuration.ConfigurationTypes.STRING,
                False,
            ),
            (
                "boolean_as_integer",
                "True",
                Configuration.ConfigurationTypes.INTEGER,
                True,
            ),
        ],
    )
    def test_get(self, name, value, _type, error):
        """Assert the configuration value can be returned."""
        factory_configuration(name=name, value=value, _type=_type)
        if error:
            with pytest.raises(ValueError):
                Configuration.get(name=name)
        else:
            value = Configuration.get(name=name)
            assert value

    def test_index_constraints(self, db, metadata):
        """Assert the index constraints are unique."""
        table = metadata.tables["configurations"]
        table_constraint = next(
            (
                constraint
                for constraint in table.constraints
                if isinstance(constraint, db.UniqueConstraint)
            ),
            None,
        )
        assert table_constraint
        for index_constraint in Configuration.index_constraints():
            assert table_constraint.contains_column(table.c[index_constraint])
