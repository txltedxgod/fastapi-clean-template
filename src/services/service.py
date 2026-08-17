import uuid
from typing import Dict, List, Optional
from src.core.exceptions import ResourceNotFoundError

class UserRepository:
    def __init__(self):
        self._db: Dict[str, dict] = {}

    def create(self, email: str, full_name: str, role: str) -> dict:
        user_id = str(uuid.uuid4())[:8]
        user = {"id": user_id, "email": email, "full_name": full_name, "role": role, "is_active": True}
        self._db[user_id] = user
        return user

    def find_by_id(self, user_id: str) -> dict:
        if user_id not in self._db:
            raise ResourceNotFoundError("User", user_id)
        return self._db[user_id]

    def list_all(self) -> List[dict]:
        return list(self._db.values())
