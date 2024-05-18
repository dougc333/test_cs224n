check to match docs
1) verify in miroblog directory
from app.models import User
> u = User(username="f",email="f@example.com")
> u
> <User f>
> from app import db
> db.session.add(u)
> db.session.commit()
>

verify in sqlite3 database
app.db is under ~/app subdir. not under instance dir. 
sqlite3 app.db
.tables user
select * from user;

