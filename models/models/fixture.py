"""Description"""
from .db import db

class Fixture(db.Model):
    __tablename__ = 'fixtures'

    id = db.Column(db.Integer, primary_key=True)
