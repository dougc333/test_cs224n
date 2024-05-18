from flask import Blueprint
from ..extensions import db
from ..models.User import User

main = Blueprint('main', __name__)

@main.route("/user/<name>")
def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()

    return "Created User"


@main.route("/")
def hi():
    return "hi"
