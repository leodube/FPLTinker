"""Common setup and fixtures for the pytest suite."""

import pytest
from flask_migrate import Migrate, downgrade, upgrade
from sqlalchemy.orm import scoped_session, sessionmaker

from ..manage import create_app
from ..models import SQLAlchemyBase
from ..models import db as _db


@pytest.fixture(scope="session")
def app():  # pylint: disable=redefined-outer-name
    """Returns a session-wide application configured in TEST mode."""
    _app = create_app("testing")
    yield _app


@pytest.fixture(scope="session")
def metadata():  # pylint: disable=redefined-outer-name
    """Returns a session-wide metadata object for the db tables."""
    _metadata = SQLAlchemyBase.metadata
    yield _metadata


@pytest.fixture(scope="session")
def db(app, metadata):  # pylint: disable=redefined-outer-name
    """Returns a session-wide initialised database."""
    with app.app_context():
        # Recreate database
        _db.create_all()
        Migrate(app, _db)
        downgrade(revision="base")
        metadata.drop_all(_db.engine)
        upgrade()
        yield _db


@pytest.fixture(scope="function")
def session(app, db):  # pylint: disable=redefined-outer-name
    """Returns a function-scoped session."""
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()

        _session = scoped_session(
            session_factory=sessionmaker(
                bind=connection,
                join_transaction_mode="create_savepoint",
            )
        )

        db.session = _session
        yield _session

        # Cleanup
        _session.remove()
        db.session.close()
        transaction.rollback()
        connection.close()
