"""Description"""
from .db import db

class Tinker(db.Model):
    __tablename__ = 'tinkers'

    id = db.Column(db.Integer, primary_key=True)
