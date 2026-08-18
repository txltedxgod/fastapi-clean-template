from app.domain.models import User
from typing import Dict, Optional, List
import uuid

class UserService:
    def __init__(self):
        self._db: Dict[str, User] = {}

    def create_user(self, email: str, full_name: str, role: str = "member") -> User:
        user_id = str(uuid.uuid4())[:8]
        user = User(id=user_id, email=email, full_name=full_name, role=role)
        self._db[user_id] = user
        return user

    def get_user(self, user_id: str) -> Optional[User]:
        return self._db.get(user_id)

    def list_users(self) -> List[User]:
        return list(self._db.values())
