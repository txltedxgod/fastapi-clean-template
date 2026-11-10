"""Pydantic request and response schemas for the v1 API."""

from datetime import UTC, datetime

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """User registration payload."""

    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=120)
    role: str = Field(default="member", min_length=1, max_length=64)


class UserResponse(BaseModel):
    """Serialized user representation."""

    id: str
    email: EmailStr
    full_name: str
    role: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
