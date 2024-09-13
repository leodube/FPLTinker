"""Create SQLAlchenmy and Schema managers.

These will get initialized by the application using the models
"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Numeric, event, func
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapper, mapped_column
from typing_extensions import Annotated

# Custom SQLAlchemy Types
intpk = Annotated[int, mapped_column(primary_key=True)]  # pylint: disable=invalid-name
timestamp = Annotated[  # pylint: disable=invalid-name
    datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]
optional_timestamp = Annotated[  # pylint: disable=invalid-name
    datetime,
    mapped_column(nullable=True),
]
stat = Annotated[float, mapped_column(Numeric(8, 2))]  # pylint: disable=invalid-name


# The base SQLAlchemy
class SQLAlchemyBase(  # pylint: disable=too-few-public-methods
    DeclarativeBase, MappedAsDataclass
):
    """The SQLAlchemy base model that adds support for declarative mapping and
    dataclass functionality"""


# Initalize the SQLAlchemy db
db = SQLAlchemy(model_class=SQLAlchemyBase)


# Setup marshmallow schemas after model configuration
@event.listens_for(Mapper, "after_configured")
def generate_marshmallow_schemas():
    """Generates marshmallow schemas after model configuration."""
    for mapper in db.Model.registry.mappers:
        _class = mapper.class_
        if hasattr(_class, "__tablename__"):

            class Meta(object):
                model = _class
                include_fk = True
                # include_relationships = True
                load_instance = True

            schema_class_name = "%sSchema" % _class.__name__

            schema_class = type(
                schema_class_name, (SQLAlchemyAutoSchema,), {"Meta": Meta}
            )

            setattr(_class, "__marshmallow__", schema_class)
