"""All of the configurations for the service is captured here."""

import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


CONFIGURATION = {
    "development": "models.config.DevConfig",
    "testing": "models.config.TestConfig",
    "production": "models.config.ProdConfig",
}


class _Config:  # pylint: disable=too-few-public-methods
    """Base class configuration."""

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    # POSTGRESQL
    DB_USER = os.getenv("DATABASE_USERNAME", "")
    DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "")
    DB_NAME = os.getenv("DATABASE_NAME", "")
    DB_HOST = os.getenv("DATABASE_HOST", "")
    DB_PORT = os.getenv("DATABASE_PORT", "5432")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    DEBUG = False
    TESTING = False


class DevConfig(_Config):  # pylint: disable=too-few-public-methods
    """Dev class configuration."""

    DEBUG = True


class TestConfig(_Config):  # pylint: disable=too-few-public-methods
    """Test class configuration."""

    # POSTGRESQL
    DB_USER = os.getenv("TEST_DATABASE_USERNAME", "")
    DB_PASSWORD = os.getenv("TEST_DATABASE_PASSWORD", "")
    DB_NAME = os.getenv("TEST_DATABASE_NAME", "")
    DB_HOST = os.getenv("TEST_DATABASE_HOST", "")
    DB_PORT = os.getenv("TEST_DATABASE_PORT", "5432")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    DEBUG = True
    TESTING = True


class ProdConfig(_Config):  # pylint: disable=too-few-public-methods
    """Prod class configuration."""
