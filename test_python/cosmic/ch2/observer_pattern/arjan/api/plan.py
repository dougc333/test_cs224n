
from lib.email import send_email
from lib.db import create_user, find_user
from lib.log import log
from lib.slack import post_slack_message

def upgrade_plan(email:str):
    #find the user
    user = find_user(email)

    #upgrade the plan
    user.plan="paid"

    #post slack message to sales department
    post_slack_message("sales",f"{user.name} has upgraded plan to paid")

    #send user thank you email, confirmation upgraded
    send_email(user.name, user.email, "thank you", f"ty for upgrading")

    #write server log
    log(f"user at email:{user.email} has upgraded to paid")

