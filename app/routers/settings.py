from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..schemas import SettingsOut, SettingsUpdate
from ..models import UserSettings
from ..deps import get_db, CurrentUser

router = APIRouter(prefix="/settings", tags=["Settings"])

@router.get("/", response_model=SettingsOut)
async def get_settings(db: AsyncSession = Depends(get_db), user = CurrentUser):
    result = await db.execute(select(UserSettings).where(UserSettings.user_id == user.id))
    st = result.scalar_one_or_none()
    if not st:
        raise HTTPException(404, "Settings not found")
    return st

@router.put("/", response_model=SettingsOut)
async def update_settings(payload: SettingsUpdate, db: AsyncSession = Depends(get_db), user = CurrentUser):
    result = await db.execute(select(UserSettings).where(UserSettings.user_id == user.id))
    st = result.scalar_one_or_none()
    if not st:
        raise HTTPException(404, "Settings not found")
    if payload.service_enabled is not None:
        st.service_enabled = payload.service_enabled
    if payload.support_email is not None:
        st.support_email = payload.support_email
    await db.commit()
    await db.refresh(st)
    return st
