

def create_db():
    from sqlalchemy_blueprint import db
    from sqlalchemy_blueprint.extensions import db
    from sqlalchemy_blueprint.models.User import User
    from sqlalchemy_blueprint import create_app
    db.create_all(app=create_app())

def drop_db():
    #rm the sqlite file
    print("remove the sqlite file")

