from django.contrib import admin

from .models import Board, Category, Client_Request

# Register your models here.

admin.site.register(Category)
admin.site.register(Client_Request)


@admin.register(Board)
class BbsBoardAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "content",
        "deadline",
        "image",
        "created_at",
        "updated_at",
        "category",
        "author",
    ]
