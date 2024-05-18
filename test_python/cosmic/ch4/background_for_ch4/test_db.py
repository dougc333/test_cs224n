from sqlalchemy import create_engine,Table,create_engine,Column, String, Integer
from sqlalchemy import MetaData
#this tests the creation of a table order_lines in a docker container
engine = create_engine('postgresql://postgres:asdf@localhost:5432')
metadata = MetaData()

order_lines = Table(
    "order_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(255)),
    Column("qty", Integer, nullable=False),
    Column("orderid", String(255)),
)

metadata.create_all(engine)






