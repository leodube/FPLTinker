"""Create SQLAlchenmy and Schema managers.

These will get initialized by the application using the models
"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, mapped_column
from sqlalchemy_continuum import make_versioned
from typing_extensions import Annotated

intpk = Annotated[  # pylint: disable=invalid-name
    int, mapped_column(primary_key=True)
]
timestamp = Annotated[  # pylint: disable=invalid-name
    datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]


class SQLAlchemyBase(  # pylint: disable=too-few-public-methods
    DeclarativeBase, MappedAsDataclass
):
    """The SQLAlchemy base model that adds support for declarative mapping and
    dataclass functionality"""


db = SQLAlchemy(model_class=SQLAlchemyBase)
make_versioned(user_cls=None)
