from datetime import datetime, timedelta

from django.db import models
from django.utils.timezone import now


class TaskManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(deleted_at__isnull=True)
        )  # Exclude soft-deleted tasks


class Task(models.Model):
    date = models.DateField(default=datetime.today)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True, null=True
    )  # Remove default=now
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "tasks"

    objects = TaskManager()
    all_objects = models.Manager()

    @property
    def total_time(self):
        start = datetime.combine(self.date, self.start_time)
        end = datetime.combine(self.date, self.end_time)
        return (end - start) if end > start else timedelta()

    def soft_delete(self):
        self.deleted_at = now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.description
