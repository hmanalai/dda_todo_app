from django.db import models


class Todo(models.Model):
    task                = models.CharField(max_length=255, null=False)
    priority            = models.CharField(max_length=255)
    created_date        = models.DateTimeField(auto_now_add=True)
    completion_status   = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task}"
