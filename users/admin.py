from django.contrib import admin

from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "ID",
        "nickname",
        "created_at",
        "last_login",
        "is_staff",
        "is_active",
        "rank",
        "rating",
    ]
