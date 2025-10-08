"""
Role and permission management endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from app.core.security import get_current_user, require_permission
from app.core.exceptions import NotFoundError, AuthorizationError
from app.services.role_service import RoleService
from app.schemas.role import RoleResponse, RoleCreate, RoleUpdate, RoleListResponse, PermissionResponse
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/", response_model=RoleListResponse)
async def get_roles(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    search: Optional[str] = None,
    current_user = Depends(get_current_user)
):
    """Get list of roles with filtering and pagination"""
    try:
        role_service = RoleService()
        
        # Check permissions
        if not role_service.has_permission(current_user, "view_role"):
            raise AuthorizationError("Permission to view roles required")
        
        roles = await role_service.get_roles(
            skip=skip,
            limit=limit,
            search=search
        )
        
        total = len(roles)  # This should be improved with proper count query
        
        return RoleListResponse(
            roles=[RoleResponse.from_orm(role) for role in roles],
            total=total,
            page=skip // limit + 1,
            limit=limit,
            has_next=skip + limit < total,
            has_prev=skip > 0
        )
    
    except Exception as e:
        logger.error(f"Get roles error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve roles"
        )

@router.get("/{role_id}", response_model=RoleResponse)
async def get_role(
    role_id: int,
    current_user = Depends(get_current_user)
):
    """Get specific role by ID"""
    try:
        role_service = RoleService()
        
        # Check permissions
        if not role_service.has_permission(current_user, "view_role"):
            raise AuthorizationError("Permission to view roles required")
        
        role = await role_service.get_role_by_id(role_id)
        if not role:
            raise NotFoundError("Role not found")
        
        return RoleResponse.from_orm(role)
    
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )
    except Exception as e:
        logger.error(f"Get role error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve role"
        )

@router.post("/", response_model=RoleResponse)
async def create_role(
    role_data: RoleCreate,
    current_user = Depends(require_permission("add_role"))
):
    """Create a new role"""
    try:
        role_service = RoleService()
        
        role = await role_service.create_role(role_data)
        
        return RoleResponse.from_orm(role)
    
    except Exception as e:
        logger.error(f"Create role error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to create role"
        )

@router.put("/{role_id}", response_model=RoleResponse)
async def update_role(
    role_id: int,
    role_data: RoleUpdate,
    current_user = Depends(require_permission("change_role"))
):
    """Update an existing role"""
    try:
        role_service = RoleService()
        
        role = await role_service.update_role(role_id, role_data)
        if not role:
            raise NotFoundError("Role not found")
        
        return RoleResponse.from_orm(role)
    
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )
    except Exception as e:
        logger.error(f"Update role error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to update role"
        )

@router.delete("/{role_id}")
async def delete_role(
    role_id: int,
    current_user = Depends(require_permission("delete_role"))
):
    """Delete a role"""
    try:
        role_service = RoleService()
        
        success = await role_service.delete_role(role_id)
        if not success:
            raise NotFoundError("Role not found")
        
        return {"message": "Role deleted successfully"}
    
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )
    except Exception as e:
        logger.error(f"Delete role error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete role"
        )

@router.get("/permissions/", response_model=List[PermissionResponse])
async def get_permissions(
    current_user = Depends(get_current_user)
):
    """Get all available permissions"""
    try:
        role_service = RoleService()
        
        # Check permissions
        if not role_service.has_permission(current_user, "view_permission"):
            raise AuthorizationError("Permission to view permissions required")
        
        permissions = await role_service.get_permissions()
        
        return [PermissionResponse.from_orm(permission) for permission in permissions]
    
    except Exception as e:
        logger.error(f"Get permissions error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve permissions"
        )

@router.put("/{role_id}/permissions")
async def update_role_permissions(
    role_id: int,
    permission_ids: List[int],
    current_user = Depends(require_permission("change_role"))
):
    """Update role permissions"""
    try:
        role_service = RoleService()
        
        success = await role_service.update_role_permissions(role_id, permission_ids)
        if not success:
            raise NotFoundError("Role not found")
        
        return {"message": "Role permissions updated successfully"}
    
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )
    except Exception as e:
        logger.error(f"Update role permissions error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to update role permissions"
        )

@router.get("/{role_id}/permissions", response_model=List[PermissionResponse])
async def get_role_permissions(
    role_id: int,
    current_user = Depends(get_current_user)
):
    """Get permissions for a specific role"""
    try:
        role_service = RoleService()
        
        # Check permissions
        if not role_service.has_permission(current_user, "view_role"):
            raise AuthorizationError("Permission to view roles required")
        
        permissions = await role_service.get_role_permissions(role_id)
        
        return [PermissionResponse.from_orm(permission) for permission in permissions]
    
    except Exception as e:
        logger.error(f"Get role permissions error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve role permissions"
        )
