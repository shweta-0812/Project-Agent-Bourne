from django.db import models
from main.models.base_model import BaseModel


class TaskDetail(BaseModel):
    id = models.AutoField(primary_key=True)
    input = models.CharField(max_length=500)
    additional_input = models.CharField(max_length=500)
