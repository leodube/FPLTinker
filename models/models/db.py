"""Create SQLAlchenmy and Schema managers.

These will get initialized by the application using the models
"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Numeric, func
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, mapped_column
from typing_extensions import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]  # pylint: disable=invalid-name
timestamp = Annotated[  # pylint: disable=invalid-name
    datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]
optional_timestamp = Annotated[  # pylint: disable=invalid-name
    datetime,
    mapped_column(nullable=True, server_default=func.CURRENT_TIMESTAMP()),
]
stat = Annotated[float, mapped_column(Numeric(8, 2))]  # pylint: disable=invalid-name


class SQLAlchemyBase(  # pylint: disable=too-few-public-methods
    DeclarativeBase, MappedAsDataclass, eq=False
):
    """The SQLAlchemy base model that adds support for declarative mapping and
    dataclass functionality"""


db = SQLAlchemy(model_class=SQLAlchemyBase)
