from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """
    Store here users comming from the bot
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, default=False)

    def __init__(self, name, email, organisations=""):
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User {}>".format(self.name)
