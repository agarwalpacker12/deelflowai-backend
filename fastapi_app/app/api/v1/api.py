"""
API v1 Router Configuration
"""

from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth, users, properties, leads, deals, campaigns, 
    ai, analytics, roles, websocket
)

api_router = APIRouter()

# Authentication endpoints
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# User management endpoints (commented out to use main.py endpoints)
# api_router.include_router(users.router, prefix="/users", tags=["Users"])

# Property management endpoints (commented out to use main.py endpoints)
# api_router.include_router(properties.router, prefix="/properties", tags=["Properties"])

# Lead management endpoints (commented out to use main.py endpoints)
# api_router.include_router(leads.router, prefix="/leads", tags=["Leads"])

# Deal management endpoints (commented out to use main.py endpoints)
# api_router.include_router(deals.router, prefix="/deals", tags=["Deals"])

# Campaign management endpoints (commented out to use main.py endpoints)
# api_router.include_router(campaigns.router, prefix="/campaigns", tags=["Campaigns"])

# AI services endpoints
api_router.include_router(ai.router, prefix="/ai", tags=["AI Services"])

# Analytics endpoints
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])

# Role and permission management endpoints
api_router.include_router(roles.router, prefix="/roles", tags=["Roles & Permissions"])

# WebSocket endpoints
api_router.include_router(websocket.router, prefix="/ws", tags=["WebSocket"])
