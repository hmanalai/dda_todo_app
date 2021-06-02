from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    fields = (
        "task", "priority", "created_date", "completion_status",
    )

    list_display = (
        "task", "priority", "created_date", "completion_status",
    )

    readonly_fields = (
        "created_date",
    )