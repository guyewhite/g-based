from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(200), unique=True, nullable=False)
    google_email = db.Column(db.String(200))
    google_name = db.Column(db.String(200))
    google_picture = db.Column(db.String(500)) 