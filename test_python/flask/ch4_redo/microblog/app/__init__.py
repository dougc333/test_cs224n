from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#tricky flask migrate needs the models import even though it isnt used in the code
#it wont create the tables without the import models. not well documented. 
from app import routes,models

