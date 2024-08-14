"""Holds the configuration details."""

# pylint: skip-file;
# flake8: noqa

from models import Configuration

config_details: dict = {
    "season": {
        "value": "20232024",
        "type": Configuration.ConfigurationTypes.INTEGER,
        "description": "",
    }
}


def get_config_details(name: str):
    return config_details.get(name, None)
