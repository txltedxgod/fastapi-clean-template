from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.user_service import UserService

app = FastAPI(title="Clean Architecture API", version="1.0.0")
service = UserService()

class CreateUserReq(BaseModel):
    email: str
    full_name: str
    role: str = "member"

@app.post("/api/v1/users")
def create_user(req: CreateUserReq):
    return service.create_user(req.email, req.full_name, req.role)

@app.get("/api/v1/users/{user_id}")
def get_user(user_id: str):
    u = service.get_user(user_id)
    if not u:
        raise HTTPException(status_code=404, detail="User not found")
    return u

@app.get("/api/v1/users")
def list_users():
    return service.list_users()

@app.get("/health")
def health():
    return {"status": "healthy"}
