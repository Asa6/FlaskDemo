from . import db

class cmdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
