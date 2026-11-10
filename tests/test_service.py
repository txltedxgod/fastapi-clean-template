"""Unit tests for the application domain UserService and User entity defaults."""

import time

from app.services.user_service import UserService


def test_user_service() -> None:
    s = UserService()
    u = s.create_user("alex@example.com", "Alex Developer", "admin")
    assert u.id is not None
    assert u.role == "admin"
    assert len(s.list_users()) == 1

    time.sleep(0.01)
    u2 = s.create_user("bob@example.com", "Bob Builder")
    assert u2.created_at > u.created_at
    assert s.delete_user(u.id) is True
    assert s.get_user(u.id) is None
