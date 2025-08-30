from sqlalchemy import Column, Integer, Text, BigInteger, String, ARRAY, TIMESTAMP, ForeignKey, Boolean
from services.shared.base import Base
from sqlalchemy.sql import func


class MenuItem(Base):
    __tablename__ = "menu_items"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True)
    cafe_id = Column(Integer, ForeignKey("cafes.id"))
    name = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(Integer)
    category = Column(Text)
    is_available = Column(Boolean, default=True)
    