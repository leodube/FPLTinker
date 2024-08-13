"""Create SQLAlchenmy and Schema managers.

These will get initialized by the application using the models
"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, mapped_column
from sqlalchemy_continuum import make_versioned
from typing_extensions import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]
timestamp = Annotated[
    datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]


class SQLAlchemyBase(DeclarativeBase, MappedAsDataclass):
    """The SQLAlchemy base model that adds support for declarative mapping and dataclass functionality"""

    pass


db = SQLAlchemy(model_class=SQLAlchemyBase)
make_versioned(user_cls=None)
