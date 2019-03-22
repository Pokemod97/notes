from app import db
from sqlalchemy import Column, Integer, String



class Note(db.Model):
    __tablename__ = 'Note'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=False, nullable=False)
    body = db.Column(db.String, unique=False, nullable=False)

    def __init__(self, title=None, body=None):
        self.title = title
        self.body = body

    def __repr__(self):
        return '<Note %r>' % self.title
