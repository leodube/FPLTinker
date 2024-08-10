"""Create SQLAlchenmy and Schema managers.

These will get initialized by the application using the models
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_continuum import make_versioned

db = SQLAlchemy()
make_versioned(user_cls=None)