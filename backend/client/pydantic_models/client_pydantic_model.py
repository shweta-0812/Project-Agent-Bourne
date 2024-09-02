from pydantic import BaseModel
from typing import Optional


class ClientDetailSchema(BaseModel):
    id: int
    uuid: str
    domain: str
    name: str
    status: int
    # @validator('domain')
    # def prevent_none(cls, v):
    #     assert v is not None, 'domain may not be None'
    #     return v


class CreateClientDetailSchema(BaseModel):
    domain: str
    name: Optional[str] = None


class UpdateClientDetailSchema(BaseModel):
    id: int
    name: Optional[str] = None


class FetchClientDetailSchema(BaseModel):
    id: Optional[str] = None
    uuid: Optional[str] = None
    domain: Optional[str] = None
    name: Optional[str] = None


class FetchAllClientDetailSchema(BaseModel):
    status: Optional[int] = None


class DeleteClientDetailSchema(BaseModel):
    id: Optional[str] = None
    uuid: Optional[str] = None
    domain: Optional[str] = None
    name: Optional[str] = None
    status: Optional[int] = None


class DeleteAllClientDetailSchema(BaseModel):
    status: int


class GetOrCreateClientDetailSchema(BaseModel):
    id: Optional[int] = None
    domain: Optional[str] = None
    name: Optional[str] = None
