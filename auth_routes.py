from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models import User
from app.schemas import UserCreate, UserLogin
from app.services.auth_service import hash_password, verify_password, create_access_token
from app.logger import logger

router = APIRouter()

#register
@router.post("/auth/register")
def register(data: UserCreate, db: Session = Depends(get_db)):

    user = User(
        username=data.username,
        email=data.email,
        password=hash_password(data.password),
        role=data.role
    )

    db.add(user)
    db.commit()

    logger.info("User registered")

    return {"message": "User created"}


# login
@router.post("/auth/login")
def login(data: UserLogin, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "sub": user.email,
        "role": user.role
    })

    logger.info("User logged in")

    return {
        "access_token": token,
        "token_type": "bearer"
    }