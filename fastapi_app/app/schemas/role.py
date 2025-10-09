"""
Role and permission-related Pydantic schemas
"""

from pydantic import BaseModel, validator
from typing import Optional, List, Dict, Any
from datetime import datetime

class PermissionBase(BaseModel):
    """Base permission schema"""
    name: str
    label: str

class PermissionCreate(PermissionBase):
    """Permission creation schema"""
    pass

class PermissionResponse(PermissionBase):
    """Permission response schema"""
    id: int
    
    class Config:
        from_attributes = True

class RoleBase(BaseModel):
    """Base role schema"""
    name: str
    label: str

class RoleCreate(RoleBase):
    """Role creation schema"""
    permission_ids: Optional[List[int]] = []

class RoleUpdate(BaseModel):
    """Role update schema"""
    name: Optional[str] = None
    label: Optional[str] = None
    permission_ids: Optional[List[int]] = None

class RoleResponse(RoleBase):
    """Role response schema"""
    id: int
    permissions: List[PermissionResponse] = []
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class RoleListResponse(BaseModel):
    """Role list response schema"""
    roles: List[RoleResponse]
    total: int
    page: int
    limit: int
    has_next: bool
    has_prev: bool
