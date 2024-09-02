from django.db import models
from agent.models.task_detail_model import TaskDetail
from main.models.base_model import BaseModel


class StepDetail(BaseModel):
    id = models.AutoField(primary_key=True)
    input = models.CharField(max_length=30)
    additional_input = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    output = models.CharField(max_length=30)
    additional_output = models.CharField(max_length=30)
    is_last = models.CharField(max_length=30)
    task = models.ForeignKey(TaskDetail, on_delete=models.CASCADE)
