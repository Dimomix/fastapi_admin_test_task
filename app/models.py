from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .db import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    settings: Mapped["UserSettings"] = relationship(back_populates="user", uselist=False, cascade="all, delete")

class UserSettings(Base):
    __tablename__ = "user_settings"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    service_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    support_email: Mapped[str] = mapped_column(String(120), default="support@example.com")

    user: Mapped[User] = relationship(back_populates="settings")
