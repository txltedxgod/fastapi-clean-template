"""Version 1 API endpoints for user lifecycle management."""

from fastapi import APIRouter, Query, Response, status

from src.schemas.models import UserCreate, UserResponse
from src.services.service import UserRepository

router = APIRouter(prefix="/api/v1/users", tags=["Users"])
repo = UserRepository()


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate) -> dict:
    """Register a new user."""
    return repo.create(payload.email, payload.full_name, payload.role)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str) -> dict:
    """Fetch a single user by identifier."""
    return repo.find_by_id(user_id)


@router.get("", response_model=list[UserResponse])
def list_users(
    limit: int = Query(default=100, ge=1, le=500),
    offset: int = Query(default=0, ge=0),
) -> list[dict]:
    """List registered users with pagination."""
    return repo.list_all(limit=limit, offset=offset)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str) -> Response:
    """Delete a user by identifier."""
    repo.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
