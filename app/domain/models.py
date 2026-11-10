"""Domain entity models."""

from datetime import UTC, datetime

from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    """Domain representation of a registered user."""

    id: str
    email: EmailStr
    full_name: str
    is_active: bool = True
    role: str = "member"
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
