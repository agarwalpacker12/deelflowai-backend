"""
Analytics and metrics endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional, Dict, Any
from app.core.security import get_current_user, require_permission
from app.core.exceptions import NotFoundError, AuthorizationError
from app.services.analytics_service import AnalyticsService
from app.schemas.analytics import DashboardMetrics, BusinessMetrics, AIAnalytics
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/dashboard", response_model=DashboardMetrics)
async def get_dashboard_metrics(
    current_user = Depends(get_current_user)
):
    """Get dashboard metrics"""
    try:
        analytics_service = AnalyticsService()
        
        # Check permissions
        if not analytics_service.has_permission(current_user, "view_analytics"):
            raise AuthorizationError("Permission to view analytics required")
        
        metrics = await analytics_service.get_dashboard_metrics(current_user.organization_id)
        return metrics
    
    except Exception as e:
        logger.error(f"Get dashboard metrics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve dashboard metrics"
        )

@router.get("/business", response_model=BusinessMetrics)
async def get_business_metrics(
    current_user = Depends(get_current_user)
):
    """Get business metrics"""
    try:
        analytics_service = AnalyticsService()
        
        # Check permissions
        if not analytics_service.has_permission(current_user, "view_analytics"):
            raise AuthorizationError("Permission to view analytics required")
        
        metrics = await analytics_service.get_business_metrics(current_user.organization_id)
        return metrics
    
    except Exception as e:
        logger.error(f"Get business metrics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve business metrics"
        )

@router.get("/ai", response_model=AIAnalytics)
async def get_ai_analytics(
    current_user = Depends(get_current_user)
):
    """Get AI analytics"""
    try:
        analytics_service = AnalyticsService()
        
        # Check permissions
        if not analytics_service.has_permission(current_user, "view_analytics"):
            raise AuthorizationError("Permission to view analytics required")
        
        analytics = await analytics_service.get_ai_analytics(current_user.organization_id)
        return analytics
    
    except Exception as e:
        logger.error(f"Get AI analytics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve AI analytics"
        )

@router.get("/revenue")
async def get_revenue_metrics(
    period: str = Query("30d", description="Time period: 7d, 30d, 90d, 1y"),
    current_user = Depends(get_current_user)
):
    """Get revenue metrics"""
    try:
        analytics_service = AnalyticsService()
        
        # Check permissions
        if not analytics_service.has_permission(current_user, "view_analytics"):
            raise AuthorizationError("Permission to view analytics required")
        
        metrics = await analytics_service.get_revenue_metrics(
            current_user.organization_id,
            period
        )
        return metrics
    
    except Exception as e:
        logger.error(f"Get revenue metrics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve revenue metrics"
        )

@router.get("/users")
async def get_user_metrics(
    current_user = Depends(get_current_user)
):
    """Get user metrics"""
    try:
        analytics_service = AnalyticsService()
        
        # Check permissions
        if not analytics_service.has_permission(current_user, "view_analytics"):
            raise AuthorizationError("Permission to view analytics required")
        
        metrics = await analytics_service.get_user_metrics(current_user.organization_id)
        return metrics
    
    except Exception as e:
        logger.error(f"Get user metrics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve user metrics"
        )

@router.get("/campaigns")
async def get_campaign_metrics(
    current_user = Depends(get_current_user)
):
    """Get campaign metrics"""
    try:
        analytics_service = AnalyticsService()
        
        # Check permissions
        if not analytics_service.has_permission(current_user, "view_analytics"):
            raise AuthorizationError("Permission to view analytics required")
        
        metrics = await analytics_service.get_campaign_metrics(current_user.organization_id)
        return metrics
    
    except Exception as e:
        logger.error(f"Get campaign metrics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve campaign metrics"
        )

@router.get("/leads")
async def get_lead_metrics(
    current_user = Depends(get_current_user)
):
    """Get lead metrics"""
    try:
        analytics_service = AnalyticsService()
        
        # Check permissions
        if not analytics_service.has_permission(current_user, "view_analytics"):
            raise AuthorizationError("Permission to view analytics required")
        
        metrics = await analytics_service.get_lead_metrics(current_user.organization_id)
        return metrics
    
    except Exception as e:
        logger.error(f"Get lead metrics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve lead metrics"
        )

@router.get("/deals")
async def get_deal_metrics(
    current_user = Depends(get_current_user)
):
    """Get deal metrics"""
    try:
        analytics_service = AnalyticsService()
        
        # Check permissions
        if not analytics_service.has_permission(current_user, "view_analytics"):
            raise AuthorizationError("Permission to view analytics required")
        
        metrics = await analytics_service.get_deal_metrics(current_user.organization_id)
        return metrics
    
    except Exception as e:
        logger.error(f"Get deal metrics error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve deal metrics"
        )

@router.get("/activity")
async def get_activity_feed(
    limit: int = Query(50, ge=1, le=200),
    current_user = Depends(get_current_user)
):
    """Get activity feed"""
    try:
        analytics_service = AnalyticsService()
        
        # Check permissions
        if not analytics_service.has_permission(current_user, "view_analytics"):
            raise AuthorizationError("Permission to view analytics required")
        
        activities = await analytics_service.get_activity_feed(
            current_user.organization_id,
            limit
        )
        return activities
    
    except Exception as e:
        logger.error(f"Get activity feed error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve activity feed"
        )

@router.get("/compliance")
async def get_compliance_status(
    current_user = Depends(get_current_user)
):
    """Get compliance status"""
    try:
        analytics_service = AnalyticsService()
        
        # Check permissions
        if not analytics_service.has_permission(current_user, "view_analytics"):
            raise AuthorizationError("Permission to view analytics required")
        
        status = await analytics_service.get_compliance_status(current_user.organization_id)
        return status
    
    except Exception as e:
        logger.error(f"Get compliance status error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve compliance status"
        )
