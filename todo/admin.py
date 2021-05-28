from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Todo, CustomUser

@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    fields = (
        "task", "priority", "created_date", "status",
    )

    list_display = (
        "task", "priority", "created_date", "status",
    )

    readonly_fields = (
        "created_date",
    )