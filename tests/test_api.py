from app.services.user_service import UserService

def test_user_service():
    s = UserService()
    u = s.create_user("alex@example.com", "Alex Developer", "admin")
    assert u.id is not None
    assert u.role == "admin"
    assert len(s.list_users()) == 1
