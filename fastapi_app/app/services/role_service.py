"""
Role and permission service for business logic
"""

from typing import List, Optional
from app.schemas.role import RoleCreate, RoleUpdate
from app.core.exceptions import NotFoundError, ValidationError
import logging

logger = logging.getLogger(__name__)

class RoleService:
    """Role service class"""
    
    def __init__(self):
        self.django_role_model = None
        self.django_permission_model = None
        self._setup_django_models()
    
    def _setup_django_models(self):
        """Setup Django models"""
        try:
            import django
            from django.apps import apps
            
            self.django_role_model = apps.get_model('deelflow', 'Role')
            self.django_permission_model = apps.get_model('deelflow', 'Permission')
        except Exception as e:
            logger.error(f"Failed to setup Django models: {e}")
    
    async def get_role_by_id(self, role_id: int):
        """Get role by ID"""
        try:
            return self.django_role_model.objects.get(id=role_id)
        except self.django_role_model.DoesNotExist:
            return None
        except Exception as e:
            logger.error(f"Error getting role by ID: {e}")
            raise
    
    async def get_roles(self, skip: int = 0, limit: int = 100, search: str = None):
        """Get roles with filtering and pagination"""
        try:
            queryset = self.django_role_model.objects.all()
            
            # Apply filters
            if search:
                queryset = queryset.filter(
                    models.Q(name__icontains=search) |
                    models.Q(label__icontains=search)
                )
            
            # Apply pagination
            return queryset[skip:skip + limit]
        except Exception as e:
            logger.error(f"Error getting roles: {e}")
            raise
    
    async def create_role(self, role_data: RoleCreate):
        """Create a new role"""
        try:
            # Create role
            role = self.django_role_model.objects.create(
                name=role_data.name,
                label=role_data.label
            )
            
            # Add permissions if provided
            if role_data.permission_ids:
                permissions = self.django_permission_model.objects.filter(
                    id__in=role_data.permission_ids
                )
                role.permissions.set(permissions)
            
            return role
        except Exception as e:
            logger.error(f"Error creating role: {e}")
            raise
    
    async def update_role(self, role_id: int, role_data: RoleUpdate):
        """Update role information"""
        try:
            role = await self.get_role_by_id(role_id)
            if not role:
                raise NotFoundError("Role not found")
            
            # Update fields
            update_data = role_data.dict(exclude_unset=True)
            for field, value in update_data.items():
                if field == "permission_ids":
                    # Handle permissions separately
                    if value is not None:
                        permissions = self.django_permission_model.objects.filter(
                            id__in=value
                        )
                        role.permissions.set(permissions)
                else:
                    setattr(role, field, value)
            
            role.save()
            return role
        except Exception as e:
            logger.error(f"Error updating role: {e}")
            raise
    
    async def delete_role(self, role_id: int):
        """Delete role"""
        try:
            role = await self.get_role_by_id(role_id)
            if not role:
                raise NotFoundError("Role not found")
            
            role.delete()
        except Exception as e:
            logger.error(f"Error deleting role: {e}")
            raise
    
    async def get_permissions(self):
        """Get all available permissions"""
        try:
            return self.django_permission_model.objects.all()
        except Exception as e:
            logger.error(f"Error getting permissions: {e}")
            raise
    
    async def update_role_permissions(self, role_id: int, permission_ids: List[int]):
        """Update role permissions"""
        try:
            role = await self.get_role_by_id(role_id)
            if not role:
                raise NotFoundError("Role not found")
            
            permissions = self.django_permission_model.objects.filter(
                id__in=permission_ids
            )
            role.permissions.set(permissions)
        except Exception as e:
            logger.error(f"Error updating role permissions: {e}")
            raise
    
    async def get_role_permissions(self, role_id: int):
        """Get permissions for a specific role"""
        try:
            role = await self.get_role_by_id(role_id)
            if not role:
                raise NotFoundError("Role not found")
            
            return role.permissions.all()
        except Exception as e:
            logger.error(f"Error getting role permissions: {e}")
            raise
    
    def has_permission(self, user, permission_name: str) -> bool:
        """Check if user has specific permission"""
        try:
            if not user or not user.role:
                return False
            
            # Get user's role
            role = self.django_role_model.objects.get(name=user.role)
            
            # Check if role has permission
            return role.permissions.filter(name=permission_name).exists()
        except Exception as e:
            logger.error(f"Error checking permission: {e}")
            return False
