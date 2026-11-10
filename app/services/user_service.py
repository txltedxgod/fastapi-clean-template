"""Application service layer for user management."""

from __future__ import annotations

import uuid

from app.domain.models import User


class UserService:
    """In-memory service managing User domain entities."""

    def __init__(self) -> None:
        self._db: dict[str, User] = {}

    def create_user(self, email: str, full_name: str, role: str = "member") -> User:
        """Create and persist a new User entity."""
        user_id = str(uuid.uuid4())[:8]
        user = User(id=user_id, email=email, full_name=full_name, role=role)
        self._db[user_id] = user
        return user

    def get_user(self, user_id: str) -> User | None:
        """Look up a user by ID."""
        return self._db.get(user_id)

    def list_users(self) -> list[User]:
        """List all persisted users."""
        return list(self._db.values())

    def delete_user(self, user_id: str) -> bool:
        """Delete a user by ID, returning True if deleted."""
        return self._db.pop(user_id, None) is not None
