from django.db import models
from agent.models.task_detail_model import TaskDetail
from agent.models.step_detail_model import StepDetail

from main.models.base_model import BaseModel


class ArtifactDetail(BaseModel):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=30)
    relative_path = models.CharField(max_length=30)
    task = models.ForeignKey(TaskDetail, on_delete=models.CASCADE)
    step = models.ForeignKey(StepDetail, on_delete=models.CASCADE)
