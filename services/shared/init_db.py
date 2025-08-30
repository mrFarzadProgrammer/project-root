from services.shared.base import Base
from services.profile.models import User, Cafe
from services.menu.models import MenuItem
from services.profile.db import engine

Base.metadata.create_all(bind=engine)