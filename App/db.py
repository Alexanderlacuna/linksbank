from flask_sqlalchemy import SQLAlchemy
from App import uuid, db


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(256), unique=True, nullable=False)
    access = db.Column(db.String(20),default="private")
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    link = db.Column(db.String(128), nullable=False)
