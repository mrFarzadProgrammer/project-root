from services.profile.db import SessionLocal
from services.profile.models import User, Base
from sqlalchemy import create_engine
import pytest

DATABASE_URL = "postgresql://cafe-factory:myDream220321!@localhost:5432/cafe_bot_db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

def test_create_user():
    session = SessionLocal()
    new_user = User(
        telegram_id=987654321,
        full_name="Test User",
        username="testuser",
        gender="male",
        interests=["coffee", "music"]
    )
    session.add(new_user)
    session.commit()

    user_from_db = session.query(User).filter_by(telegram_id=987654321).first()
    assert user_from_db is not None
    assert user_from_db.full_name == "Test User"
    session.close()