from services.menu.models import MenuItem

def test_menu_item_fields():
    item = MenuItem(
        cafe_id=1,
        name="Espresso",
        description="Strong coffee shot",
        price=30000,
        category="Coffee",
        is_available=True
    )
    assert item.name == "Espresso"
    assert item.price == 30000
    assert item.is_available is True