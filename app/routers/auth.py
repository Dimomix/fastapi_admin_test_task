from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import timedelta
from ..schemas import UserCreate, Token
from ..models import User, UserSettings
from ..security import create_access_token, get_password_hash, verify_password
from ..db import get_session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=Token, status_code=201)
async def register(data: UserCreate, session: AsyncSession = Depends(get_session)):
    # check unique
    q = await session.execute(select(User).where((User.username == data.username) | (User.email == data.email)))
    if q.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        username=data.username,
        email=data.email,
        hashed_password=get_password_hash(data.password)
    )
    session.add(user)
    await session.flush()  # need primary key
    # default settings for this user
    s = UserSettings(user_id=user.id)
    session.add(s)
    await session.commit()

    token = create_access_token({"sub": user.username}, expires_delta=timedelta(minutes=60))
    return Token(access_token=token)

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_session)
):
    result = await session.execute(select(User).where(User.username == form_data.username))
    user = result.scalar_one_or_none()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return Token(access_token=token)
