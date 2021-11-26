from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy() 

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    species = db.Column(db.Text)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    available = db.Column(db.Boolean,  default = True)

def connect_db(app):
    db.app=app
    db.init_app(app)  
