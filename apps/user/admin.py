from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.user.models import User
from apps.rol.models import Roles
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass