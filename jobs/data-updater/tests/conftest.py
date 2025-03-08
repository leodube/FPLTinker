"""Common setup and fixtures for the pytest suite."""

import aiohttp
import pytest
import pytest_asyncio
from fpl import FPL
from fpltinker.models import SQLAlchemyBase
from fpltinker.models import db as _db
from sqlalchemy.orm import scoped_session, sessionmaker

from update import create_app


@pytest.fixture(scope="session")
def app():  # pylint: disable=redefined-outer-name, invalid-name
    """Return a session-wide application configured in TEST mode."""
    _app = create_app("testing")
    yield _app


@pytest_asyncio.fixture(scope="function")
async def fpl():  # pylint: disable=redefined-outer-name, invalid-name
    """Return a session-wide fpl object."""
    _session = aiohttp.ClientSession()
    _fpl = FPL(_session)
    yield _fpl
    await _session.close()


@pytest.fixture(scope="session")
def metadata(app):  # pylint: disable=redefined-outer-name, invalid-name
    """Return a session-wide metadata object for the db tables."""
    _metadata = SQLAlchemyBase.metadata
    yield _metadata


@pytest.fixture(scope="session")
def db(app, metadata):  # pylint: disable=redefined-outer-name, invalid-name
    """Return a session-wide initialised database."""
    with app.app_context():
        # Recreate database
        metadata.drop_all(_db.engine)
        metadata.create_all(_db.engine)
        yield _db


@pytest.fixture(scope="function")
def session(app, db):
    """Return a function-scoped session."""
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
