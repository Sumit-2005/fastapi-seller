from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, ForeignKey
from sqlalchemy.sql.sqltypes import Text

class Listings(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    shipping_info = Column(String, nullable=False)
    image = Column(String, nullable=True)