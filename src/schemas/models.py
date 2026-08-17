from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    full_name: str
    role: str = "member"

class UserResponse(BaseModel):
    id: str
    email: str
    full_name: str
    role: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
