"""In-memory user repository with duplicate email protection and pagination."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from src.core.exceptions import DuplicateResourceError, ResourceNotFoundError


class UserRepository:
    """Repository managing user entities."""

    def __init__(self) -> None:
        self._db: dict[str, dict] = {}

    def create(self, email: str, full_name: str, role: str) -> dict:
        """Create a new user after verifying unique email."""
        normalized_email = email.strip().lower()
        if any(u["email"].lower() == normalized_email for u in self._db.values()):
            raise DuplicateResourceError("User", normalized_email)

        user_id = str(uuid.uuid4())[:8]
        user = {
            "id": user_id,
            "email": email,
            "full_name": full_name.strip(),
            "role": role,
            "is_active": True,
            "created_at": datetime.now(UTC),
        }
        self._db[user_id] = user
        return user

    def find_by_id(self, user_id: str) -> dict:
        """Return a user or raise ResourceNotFoundError."""
        if user_id not in self._db:
            raise ResourceNotFoundError("User", user_id)
        return self._db[user_id]

    def list_all(self, limit: int = 100, offset: int = 0) -> list[dict]:
        """Return a paginated slice of users."""
        users = list(self._db.values())
        return users[offset : offset + limit]

    def delete(self, user_id: str) -> None:
        """Delete a user or raise ResourceNotFoundError."""
        if user_id not in self._db:
            raise ResourceNotFoundError("User", user_id)
        del self._db[user_id]
