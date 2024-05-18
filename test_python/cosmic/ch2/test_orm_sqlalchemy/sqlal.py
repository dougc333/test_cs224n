from sqlalchemy import Column, Integer, Numeric, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:")
Session_local = sessionmaker(bind=engine)
session = Session_local()

Base = declarative_base()


class Cookie(Base):
    __tablename__ = "cookies"
    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))

    def __repr__(self):
        return (
            str(self.cookie_id) + "," + self.cookie_name + "," + self.cookie_recipe_url
        )


Base.metadata.create_all(engine)
cc_cookie = Cookie(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://someaddress.com",
    cookie_sku="cc01",
    quantity=10,
    unit_cost=0.20,
)
session.add(cc_cookie)
session.commit()
res = session.query(Cookie).all()
print(res)
