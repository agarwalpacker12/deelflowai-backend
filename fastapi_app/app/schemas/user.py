"""
User-related Pydantic schemas
"""

from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List, Dict, Any
from datetime import datetime
from app.schemas.organization import OrganizationResponse
from app.schemas.role import RoleResponse

class UserBase(BaseModel):
    """Base user schema"""
    email: EmailStr
    first_name: str
    last_name: str
    phone: Optional[str] = None
    is_active: bool = True
    is_verified: bool = False

class UserCreate(UserBase):
    """User creation schema"""
    password: str
    organization_id: Optional[int] = None
    role: Optional[str] = "user"
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v

class UserUpdate(BaseModel):
    """User update schema"""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None
    is_verified: Optional[bool] = None
    role: Optional[str] = None

class UserResponse(UserBase):
    """User response schema"""
    id: int
    uuid: str
    role: str
    level: int
    points: int
    organization: Optional[OrganizationResponse] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class UserListResponse(BaseModel):
    """User list response schema"""
    users: List[UserResponse]
    total: int
    page: int
    limit: int
    has_next: bool
    has_prev: bool

class UserStats(BaseModel):
    """User statistics schema"""
    total_users: int
    active_users: int
    verified_users: int
    users_by_role: dict
    recent_signups: int
