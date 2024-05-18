
from lib.email import send_email
from lib.db import create_user, find_user
from lib.log import log
from lib.slack import post_slack_message
from lib.stringtools import get_random_string


def register_new_user(name:str, password:str, email:str):
    #create an entry in a database
    user = create_user(name, password, email)

    post_slack_message("sales", f"{user.name} has registered with email:{user.email}.")

    send_email(user.name, user.email, "selcome", "welcome {user.name} prepare to receive spam")

    log(f"user {user.name} registered with email:{user.email}")


def password_forgotten(email:str):
    user = find_user(email)

    user.reset_code = get_random_string(16)

    send_email(user.name, user.email, "reset passwword", f"reset opassword use this code:{user.reset_code}")
    log(f"User email {user.email} requested password reset")
