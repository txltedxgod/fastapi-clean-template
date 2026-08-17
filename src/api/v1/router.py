from fastapi import APIRouter, status
from typing import List
from src.schemas.models import UserCreate, UserResponse
from src.services.service import UserRepository

router = APIRouter(prefix="/api/v1/users", tags=["Users"])
repo = UserRepository()

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate):
    return repo.create(payload.email, payload.full_name, payload.role)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    return repo.find_by_id(user_id)

@router.get("", response_model=List[UserResponse])
def list_users():
    return repo.list_all()
