
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .extensions import db, migrate
from .routes.api import api
from .routes.main import main

db = SQLAlchemy()
#export FLASK_APP=sqlalchemy_blueprint
def create_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"   
    app.config["SECRET_KEY"]="asdfasdf"
    
    db.init_app(app)
    migrate.init_app(app,db)
    
    app.register_blueprint(main)
    app.register_blueprint(api)
     
    return app



#have to be one level up and import models, extensinons, create_app(), and then db.create_db(app=create_app())
#not clear redo this with db.init_app()
#and more docs on application factory
#