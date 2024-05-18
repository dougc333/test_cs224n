
orm for sqlalchemy syntax. 
start with tests and domain model, model.py

From Ch1 we have orderlines and batches. Implies at least 2 tables
We introduce a separate layer repository to act as the interface between storage and the tables

session is part of the pytest test fixture. Assume this is part of the user login. There is no test
for the session ending and seeing if data is lost or preserved. 

at high level this doesnt matter but there are network and system failuers which are part of the design. 

what is the difference between metadata and basedeclaration? 
both can be used to make tables

mypy might be better for declarative base. docs not clear