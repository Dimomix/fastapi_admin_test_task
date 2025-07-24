from fastapi import APIRouter, Depends
from ..schemas import UserOut
from ..deps import CurrentUser

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserOut)
async def read_me(user = CurrentUser):
    return user
