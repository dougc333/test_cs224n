from flask import Flask

#export FLASK_APP=myapp; flask run
#http://localhost:5000 and http://localhost/api/getdata
#2 blueprints, one for API one for site
from .api.routes import api
from .site.routes import site

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.register_blueprint(site)
    return app

