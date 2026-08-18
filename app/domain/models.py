from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: str
    email: str
    full_name: str
    is_active: bool = True
    role: str = "member"
    created_at: datetime = datetime.utcnow()
