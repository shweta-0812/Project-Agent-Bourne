from django.db import models
from main.models.base_model import BaseModel
from client.models.client_detail_model import ClientDetailModel


class WorkspaceDetailModel(BaseModel):
    id = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    name = models.CharField(max_length=255, unique=True)
    client = models.ForeignKey(ClientDetailModel, on_delete=models.CASCADE, related_name='workspaces')

    class Meta:
        db_table = 'workspace_detail'
        verbose_name = 'Workspace Detail'
        verbose_name_plural = 'Workspace Details'

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if self.client.client_admin_user_id != kwargs.get('admin_user'):
    #         raise PermissionError("Only the client admin can create a workspace.")
    #     super().save(*args, **kwargs)
    #
    # def delete(self, *args, **kwargs):
    #     if self.client.client_admin_user_id != kwargs.get('admin_user'):
    #         raise PermissionError("Only the client admin can delete a workspace.")
    #     super().delete(*args, **kwargs)


# @receiver(post_delete, sender=UserDetailModel)
# def remove_user_from_workspaces(sender, instance, **kwargs):
#     instance.workspaces.clear()
