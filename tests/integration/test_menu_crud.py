import pytest
from services.menu.db import SessionLocal
from services.menu.crud import (
    create_menu_item,
    get_menu_items,
    get_menu_item,
    update_menu_item,
    delete_menu_item
)

# داده تستی اولیه
test_data = {
    "cafe_id": 1,
    "name": "Latte",
    "description": "Milk coffee",
    "price": 45000,
    "category": "Coffee",
    "is_available": True
}

def test_create_and_read_menu_item():
    item = create_menu_item(test_data)
    assert item.id is not None
    assert item.name == "Latte"

    fetched = get_menu_item(item.id)
    assert fetched.name == "Latte"
    assert fetched.price == 45000

def test_update_menu_item():
    item = create_menu_item(test_data)
    updated = update_menu_item(item.id, {"price": 50000, "name": "Latte Grande"})
    assert updated.price == 50000
    assert updated.name == "Latte Grande"

def test_delete_menu_item():
    item = create_menu_item(test_data)
    deleted = delete_menu_item(item.id)
    assert deleted is not None

    fetched = get_menu_item(item.id)
    assert fetched is None