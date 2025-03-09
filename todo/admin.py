from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("description", "date", "start_time", "end_time", "deleted_at")
    list_filter = ("deleted_at",)
    actions = ["restore_tasks"]

    def restore_tasks(self, request, queryset):
        queryset.update(deleted_at=None)

    restore_tasks.short_description = "Restore selected tasks"


admin.site.register(Task, TaskAdmin)
