from flask_sqlalchemy import SQLAlchemy
from App import uuid, db
from flask import jsonify


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(256), unique=True, nullable=False)
    access = db.Column(db.String(20), default="private")
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'{self.title} {self.public_id} {self.link}'

    def get_links():
        try:
            links = Links.query.all()
        except Exception as e:
            raise e

        return links

    def get_link(link_id):

        try:
            link = Links.query.filter_by(public_id=link_id).first()
        except Exception as e:
            raise e

        return link

    def serializer(self):
        return {"public_id": self.public_id, "title": self.title, "access": self.access, "description": self.description, "link": self.link}

    def add_db(self):
        try:
            db.create_all()

            db.session.add(self)
            db.session.commit()
        except Exception as e:
            raise e

        return "success"
