from pydantic import BaseModel, EmailStr

# --- Auth ---
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# --- User & Settings ---
class SettingsBase(BaseModel):
    service_enabled: bool
    support_email: EmailStr 

class SettingsUpdate(BaseModel):
    service_enabled: bool | None = None
    support_email: EmailStr | None = None

class SettingsOut(SettingsBase):
    pass

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    settings: SettingsOut | None

    class Config:
        from_attributes = True
