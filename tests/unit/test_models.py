from services.profile.models import User

def test_user_model_fields():
    user = User(telegram_id=123456789, full_name="Ali", username="mrFarzad")
    assert user.telegram_id == 123456789
    assert user.full_name == "Ali"
    assert user.username == "mrFarzad"