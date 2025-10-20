"""
Role and Permission related Pydantic schemas
"""

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PermissionBase(BaseModel):
    name: str
    label: str

class PermissionCreate(PermissionBase):
    pass

class PermissionResponse(PermissionBase):
    id: int
    
    class Config:
        from_attributes = True

class RoleBase(BaseModel):
    name: str
    label: str

class RoleCreate(RoleBase):
    permission_ids: List[int] = []

class RoleUpdate(BaseModel):
    name: Optional[str] = None
    label: Optional[str] = None
    permission_ids: Optional[List[int]] = None

class RoleResponse(RoleBase):
    id: int
    permissions: List[PermissionResponse] = []
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class RoleListResponse(BaseModel):
    roles: List[RoleResponse]
    total: int
    page: int
    limit: int

class PermissionListResponse(BaseModel):
    permissions: List[PermissionResponse]
    total: int
    page: int
    limit: int