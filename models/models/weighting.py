"""Description"""
from .db import db

class Weighting(db.Model):
    __tablename__ = 'weightings'

    id = db.Column(db.Integer, primary_key=True)
