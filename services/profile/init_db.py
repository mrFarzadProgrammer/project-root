from services.profile.models import Base as ProfileBase
from services.menu.models import Base as MenuBase
from services.profile.db import engine

ProfileBase.metadata.create_all(bind=engine)
MenuBase.metadata.create_all(bind=engine)