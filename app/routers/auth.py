from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select

from app.database import engine
from app.models.user import User
from app.core.security import verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.get("/ping")
def ping():
    return {"message": "Auth module up!"}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    with Session(engine) as session:
        statement = select(User).where(User.username == form_data.username)
        user = session.exec(statement).first()

        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Credenciais inválidas")

        token = create_access_token({"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
