import uuid

from django.db import models
from main.models.base_model import BaseModel


class ClientDetailModel(BaseModel):
    id = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, blank=False, null=False, unique=True, editable=False)
    domain = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'client_detail'
        verbose_name = 'Client Detail'
        verbose_name_plural = 'Client Details'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.domain

    # def delete(self, *args, **kwargs):
    #     # Delete all associated users when a client is deleted
    #     self.users.all().delete()
    #     super().delete(*args, **kwargs)
