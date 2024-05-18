from ..extensions import db

#we should be using dataclasses then
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(50))
    
    
