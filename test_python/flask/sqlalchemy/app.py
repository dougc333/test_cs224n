from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#3 slash for relative path, 4 slash for absoute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
#db must be declared after app config options set
db = SQLAlchemy(app)

#table which 
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)
    
@app.route("/")
def hi():
    return "<h4>Waiting to enter /user/location into url</h4>"

#need an init process we did this in cli from app import db then db.create_all()

@app.route("/<name>/<location>")
def index(name,location):
    user = User(name=name, location=location)
    db.session.add(user)
    db.session.commit()
    return f"<h4>added user {user} at location:{location}<h4>"

@app.route("/<name>")
def read(name):
    user = User.query.filter_by(name=name).first()
    return f"user {user.name} is located in {user.location}"

if __name__ == "__main__":
    app.run(debug=True)
    

