"""Description"""
from .db import db

class PlayerStats(db.Model):
    __tablename__ = 'player_stats'

    id = db.Column(db.Integer, primary_key=True)
