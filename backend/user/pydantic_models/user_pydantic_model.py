from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserDetailSchema(BaseModel):
    id: int
    uuid: str
    name: str
    email: str
    profile_pic_url: str
    is_admin: bool
    status: int
    last_login: datetime

    # client = models.ForeignKey(ClientDetailModel, on_delete=models.CASCADE, related_name='users')
    # workspaces = models.ManyToManyField(WorkspaceDetailModel, related_name='users', blank=True)
    # @validator('domain')
    # def prevent_none(cls, v):
    #     assert v is not None, 'domain may not be None'
    #     return v


class CreateUserDetailSchema(BaseModel):
    name: str
    email: str
    is_admin: Optional[bool] = False
    status: Optional[int] = 1
    profile_pic_url: Optional[str] = None
    client_id: Optional[int] = None
    oauth_provider: Optional[str] = None
    oauth_id: Optional[str] = None
    user_type: Optional[int] = None


class UpdateUserDetailSchema(BaseModel):
    id: int
    name: Optional[str] = None
    profile_pic_url: Optional[str] = None
    is_admin: Optional[bool] = None
    status: Optional[int] = None


class FetchUserDetailSchema(BaseModel):
    id: Optional[str] = None
    uuid: Optional[str] = None
    email: Optional[str] = None
    status: Optional[int] = None


class FetchAllUserDetailSchema(BaseModel):
    status: Optional[int] = None


class DeleteUserDetailSchema(BaseModel):
    id: Optional[str] = None
    uuid: Optional[str] = None
    email: Optional[str] = None
    status: Optional[int] = None


class DeleteAllUserDetailSchema(BaseModel):
    status: int
