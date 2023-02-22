from django.db import models
import uuid


class ToDo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    completed = models.BooleanField(default=False, null=False, blank=False)
