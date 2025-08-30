from sqlalchemy import Column, Integer, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True)
    cafe_id = Column(Integer, ForeignKey("cafes.id"))
    name = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(Integer)
    category = Column(Text)
    is_available = Column(Boolean, default=True)