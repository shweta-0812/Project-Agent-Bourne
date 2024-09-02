import uuid

from django.db import models
from main.models.base_model import BaseModel
from client.models.client_detail_model import ClientDetailModel
from workspace.models.workspace_detail_model import WorkspaceDetailModel
from enum import Enum


class UserTypes(Enum):
    INDIVIDUAL = 0
    CLIENT_ASSOCIATED = 1


class UserDetailModel(BaseModel):
    id = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, blank=False, null=False, unique=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=True)
    profile_pic_url = models.URLField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    oauth_provider = models.CharField(max_length=50, blank=True, null=True)
    oauth_id = models.CharField(max_length=255, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    user_type = models.IntegerField(
        choices=[(user_type.value, user_type.name) for user_type in UserTypes],
        default=UserTypes.INDIVIDUAL.value,
        help_text="Defines the type of user: 'Individual' or 'Client Associated'."
    )
    client = models.ForeignKey(
        ClientDetailModel,
        on_delete=models.CASCADE,
        related_name='users',
        null=True,
        blank=True,
        help_text="This field is for client-associated users only. Leave blank for individual users."
    )
    workspaces = models.ManyToManyField(WorkspaceDetailModel, related_name='users', blank=True)

    class Meta:
        db_table = 'user_detail'
        verbose_name = 'User Detail'
        verbose_name_plural = 'User Details'

    def __str__(self):
        if self.user_type == UserTypes.INDIVIDUAL.value:
            user_type = 'Individual'
        else:
            user_type = 'Client-Associated'
        return f"{self.name} {self.email} ({user_type})"

    # def save(self, *args, **kwargs):
    #     # Automatically set the domain based on the client admin's email
    #     if self.client_admin_user_id:
    #         email_domain = self.client_admin_user_id.email.split('@')[-1]
    #         self.domain = email_domain
    #     if not self.client_admin_user_id.is_active:
    #         raise ValidationError("Client admin must always be an active user.")
    #     super().save(*args, **kwargs)
    #
    # def clean(self):
    #     # Ensure that an active client has at least one active user
    #     if self.status and not self.users.filter(is_active=True).exists():
    #         raise ValidationError("An active client must have at least one active user.")
    # @receiver(post_delete, sender=UserDetailModel)
    # def prevent_admin_deletion(sender, instance, **kwargs):
    #     if hasattr(instance, 'client_admin_for'):
    #         raise ValidationError("Cannot delete the admin user for a client.")


class UserWorkspaceMappingDetailModel(BaseModel):
    workspace = models.ForeignKey(WorkspaceDetailModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetailModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'workspace_user_mapping_detail'
        verbose_name = 'Workspace User Mapping Detail'
        verbose_name_plural = 'Workspace User Mapping Details'

    def __str__(self):
        return self.workspace.name
