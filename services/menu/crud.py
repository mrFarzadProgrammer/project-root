from services.menu.db import SessionLocal
from services.menu.models import MenuItem

# افزودن آیتم جدید
def create_menu_item(data: dict):
    session = SessionLocal()
    item = MenuItem(**data)
    session.add(item)
    session.commit()
    session.refresh(item)
    session.close()
    return item

# دریافت لیست آیتم‌ها برای یک کافه
def get_menu_items(cafe_id: int):
    session = SessionLocal()
    items = session.query(MenuItem).filter_by(cafe_id=cafe_id).all()
    session.close()
    return items

# دریافت یک آیتم خاص
def get_menu_item(item_id: int):
    session = SessionLocal()
    item = session.query(MenuItem).filter_by(id=item_id).first()
    session.close()
    return item

# ویرایش آیتم
def update_menu_item(item_id: int, updates: dict):
    session = SessionLocal()
    item = session.query(MenuItem).filter_by(id=item_id).first()
    if item:
        for key, value in updates.items():
            setattr(item, key, value)
        session.commit()
        session.refresh(item)
    session.close()
    return item

# حذف آیتم
def delete_menu_item(item_id: int):
    session = SessionLocal()
    item = session.query(MenuItem).filter_by(id=item_id).first()
    if item:
        session.delete(item)
        session.commit()
    session.close()
    return item