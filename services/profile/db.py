from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://cafe-factory:myDream220321!@localhost:5432/cafe_bot_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)