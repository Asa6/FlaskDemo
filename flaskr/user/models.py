from . import db

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    chinese_name = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=True)
