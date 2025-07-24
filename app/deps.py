from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .db import get_session
from .security import get_current_user
from .models import User

async def get_db(session: AsyncSession = Depends(get_session)):
    return session

CurrentUser = Depends(get_current_user)
