from django.db import models
from django.utils import timezone

from enum import Enum


class Status(Enum):
    INACTIVE = 0
    ACTIVE = 1
    PENDING = 2
    DELETED = 3


class BaseModel(models.Model):
    status = models.IntegerField(choices=[(status.value, status.name) for status in Status],
                                 default=Status.INACTIVE.value)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
