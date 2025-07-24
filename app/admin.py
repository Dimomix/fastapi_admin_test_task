from sqladmin import Admin, ModelView
from .db import engine
from .models import User, UserSettings

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email, User.is_active]

class UserSettingsAdmin(ModelView, model=UserSettings):
    column_list = [UserSettings.user_id, UserSettings.service_enabled, UserSettings.support_email]

def init_admin(app):
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)
    admin.add_view(UserSettingsAdmin)
