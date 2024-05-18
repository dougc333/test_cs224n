
from flask import Blueprint

site = Blueprint('site',__name__)

@site.route('/')
def index():
    return "<h6> welcome to home page</h6>"