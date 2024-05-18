# Test Python

Python test programs
 1) flask, test Grinberg's material for teaching Python meetups. MegaFlask tutorial used to be on youtube but has since moved behind a paywall. It covers CRUD applications. Data science apps have additional requirements including task processing, pub/sub messaging and deploy to AWS as code. It would be more useful to take a DJANGO framework and run it in a container. Spending meetup hours to relearn authentication, ORM mapping, logging and administration is not as relevant in 2024. 

 

problem is you have to create the db in the CLI

cd one level up of project
from sqlalchemy import db
from sqlalchemy.extensions import db
from sqlalchemy.models import User
db.create_all(app=create_app)

application factory pattern 

#run this:
from sqlalchemy_blueprint.run_from_one_level_up import create_db
create_db()