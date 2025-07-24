from tortoise import fields, models

class AdminUser(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=128)
    is_superuser = fields.BooleanField(default=True)

    class Meta:
        table = "users"  

class Settings(models.Model):
    user_id = fields.IntField(pk=True)
    service_enabled = fields.BooleanField(default=True)
    support_email = fields.CharField(max_length=120)

    class Meta:
        table = "user_settings"