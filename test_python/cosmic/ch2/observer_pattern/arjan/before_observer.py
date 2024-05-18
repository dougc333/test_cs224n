from atexit import register
from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan



register_new_user("Bob", "password1", "bob@email.com")

password_forgotten("bob@email.com")

upgrade_plan("bob@email.com")