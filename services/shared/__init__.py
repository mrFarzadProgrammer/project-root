from services.shared.base import Base
from services.profile.models import User, Cafe, CafeFeature
from services.menu.models import MenuItem
from services.profile.db import engine

print("✅ Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully.")