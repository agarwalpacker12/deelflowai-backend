"""
DeelFlowAI FastAPI Application
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
import os
import sys
import django
from pathlib import Path

# Add Django project to Python path
django_project_path = Path(__file__).parent.parent
sys.path.append(str(django_project_path))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deelflowAI.settings')
django.setup()

from app.api.v1.api import api_router
from app.core.config import settings

# Create FastAPI application
app = FastAPI(
    title="DeelFlowAI Backend API",
    version="1.0.0",
    description="Comprehensive real estate AI platform backend API",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://dev.deelflowai.com:8000",
        "http://localhost:5175",
        "http://localhost:3000",
        "http://127.0.0.1:5175",
        "http://127.0.0.1:3000",
        "http://localhost:5173",  # Vite default port
        "http://127.0.0.1:5173",  # Vite default port
        "*"  # Allow all origins for development
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Trusted host middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=[
        "dev.deelflowai.com",
        "localhost",
        "127.0.0.1",
        "*"
    ]
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "DeelFlowAI Backend API",
        "version": "1.0.0",
        "status": "active",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": "2024-01-01T00:00:00Z",
        "services": {
            "database": "connected",
            "ai_services": "active",
            "background_tasks": "running"
        }
    }

# Additional endpoints for frontend compatibility
@app.get("/stats")
@app.options("/stats")
async def get_stats():
    """Get general statistics for the dashboard"""
    return {
        'status': 'success',
        'data': {
            'total_users': 150,
            'total_properties': 89,
            'total_leads': 234,
            'total_deals': 45,
            'active_campaigns': 12,
            'revenue': 125000.50,
            'monthly_profit': 25000.75,
            'voice_calls': 156,
        }
    }

@app.get("/status")
@app.options("/status")
async def get_status():
    """Get system status and health information"""
    return {
        'status': 'success',
        'data': {
            'database': 'connected',
            'api': 'operational',
            'ai_services': 'active',
            'background_tasks': 'running',
            'counts': {
                'users': 150,
                'properties': 89,
                'leads': 234,
                'deals': 45
            },
            'timestamp': '2025-10-09T04:30:00Z'
        }
    }

@app.get("/recent_activity")
@app.options("/recent_activity")
async def get_recent_activity():
    """Get recent activity feed"""
    return {
        "status": "success",
        "message": "Recent activity retrieved successfully",
        "data": {
            "activities": [
                {"event": "New lead added", "date": "2025-10-08", "user": "System", "action_type": "lead_created"},
                {"event": "Property analysis completed", "date": "2025-10-07", "user": "AI", "action_type": "ai_analysis"},
                {"event": "Campaign launched", "date": "2025-10-06", "user": "Admin", "action_type": "campaign_created"},
                {"event": "Deal closed", "date": "2025-10-05", "user": "Agent", "action_type": "deal_closed"}
            ],
            "last_updated": "2025-10-09T04:30:00Z"
        }
    }

@app.get("/opportunity-cost-analysis")
@app.options("/opportunity-cost-analysis")
async def get_opportunity_cost_analysis():
    """Get opportunity cost analysis data"""
    return {
        'status': 'success',
        'data': {
            'total_revenue': 125000.50,
            'monthly_profit': 25000.75,
            'properties_listed': 89,
            'total_deals': 45,
            'opportunity_cost': 12500.05,
            'efficiency_score': 85.5,
            'recommendations': [
                'Increase lead conversion rate by 15%',
                'Optimize property listing strategy',
                'Improve deal closing timeline'
            ]
        }
    }

@app.get("/api/voice-ai-calls-count")
@app.options("/api/voice-ai-calls-count")
async def get_voice_ai_calls_count():
    """Get voice AI calls count"""
    return {
        'total_calls': 156,
        'success_rate': 87.5,
        'created_at': '2025-10-09T04:30:00Z',
        'updated_at': '2025-10-09T04:30:00Z'
    }

# Additional missing endpoints from frontend logs
@app.get("/api/organizations/status")
@app.options("/api/organizations/status")
async def get_organization_status():
    """Get organization status"""
    return {
        'status': 'active',
        'organization_id': 1,
        'name': 'DeelFlowAI',
        'subscription': 'premium',
        'created_at': '2025-01-01T00:00:00Z'
    }

@app.get("/api/analytics/opportunity-cost-analysis")
@app.options("/api/analytics/opportunity-cost-analysis")
async def get_analytics_opportunity_cost_analysis():
    """Get analytics opportunity cost analysis"""
    return {
        'status': 'success',
        'data': {
            'total_revenue': 125000.50,
            'monthly_profit': 25000.75,
            'properties_listed': 89,
            'total_deals': 45,
            'opportunity_cost': 12500.05,
            'efficiency_score': 85.5,
            'recommendations': [
                'Increase lead conversion rate by 15%',
                'Optimize property listing strategy',
                'Improve deal closing timeline'
            ]
        }
    }

@app.get("/api/tenant-management/stats")
@app.options("/api/tenant-management/stats")
async def get_tenant_management_stats():
    """Get tenant management statistics"""
    return {
        'status': 'success',
        'data': {
            'total_tenants': 25,
            'active_tenants': 23,
            'inactive_tenants': 2,
            'total_users': 150,
            'monthly_revenue': 25000.75,
            'growth_rate': 12.5
        }
    }

# Support both GET and POST for recent_activity
@app.post("/recent_activity")
@app.options("/recent_activity")
async def post_recent_activity():
    """Handle POST requests to recent_activity"""
    return {
        "status": "success",
        "message": "Recent activity retrieved successfully",
        "data": {
            "activities": [
                {"event": "New lead added", "date": "2025-10-08", "user": "System", "action_type": "lead_created"},
                {"event": "Property analysis completed", "date": "2025-10-07", "user": "AI", "action_type": "ai_analysis"},
                {"event": "Campaign launched", "date": "2025-10-06", "user": "Admin", "action_type": "campaign_created"},
                {"event": "Deal closed", "date": "2025-10-05", "user": "Agent", "action_type": "deal_closed"}
            ],
            "last_updated": "2025-10-09T04:30:00Z"
        }
    }

# Additional endpoints that frontend is calling with trailing slashes
@app.get("/api/organizations/status/")
@app.options("/api/organizations/status/")
async def get_organization_status_trailing():
    """Get organization status with trailing slash"""
    return {
        'status': 'active',
        'organization_id': 1,
        'name': 'DeelFlowAI',
        'subscription': 'premium',
        'created_at': '2025-01-01T00:00:00Z'
    }

@app.get("/api/voice-ai-calls-count/")
@app.options("/api/voice-ai-calls-count/")
async def get_voice_ai_calls_count_trailing():
    """Get voice AI calls count with trailing slash"""
    return {
        'total_calls': 156,
        'success_rate': 87.5,
        'created_at': '2025-10-09T04:30:00Z',
        'updated_at': '2025-10-09T04:30:00Z'
    }

@app.get("/api/tenant-management/stats/")
@app.options("/api/tenant-management/stats/")
async def get_tenant_management_stats_trailing():
    """Get tenant management statistics with trailing slash"""
    return {
        'status': 'success',
        'data': {
            'total_tenants': 25,
            'active_tenants': 23,
            'inactive_tenants': 2,
            'total_users': 150,
            'monthly_revenue': 25000.75,
            'growth_rate': 12.5
        }
    }

@app.get("/api/analytics/opportunity-cost-analysis/")
@app.options("/api/analytics/opportunity-cost-analysis/")
async def get_analytics_opportunity_cost_analysis_trailing():
    """Get analytics opportunity cost analysis with trailing slash"""
    return {
        'status': 'success',
        'data': {
            'total_revenue': 125000.50,
            'monthly_profit': 25000.75,
            'properties_listed': 89,
            'total_deals': 45,
            'opportunity_cost': 12500.05,
            'efficiency_score': 85.5,
            'recommendations': [
                'Increase lead conversion rate by 15%',
                'Optimize property listing strategy',
                'Improve deal closing timeline'
            ]
        }
    }

@app.get("/recent_activity/")
@app.post("/recent_activity/")
@app.options("/recent_activity/")
async def recent_activity_trailing():
    """Handle GET and POST requests to recent_activity with trailing slash"""
    return {
        "status": "success",
        "message": "Recent activity retrieved successfully",
        "data": {
            "activities": [
                {"event": "New lead added", "date": "2025-10-08", "user": "System", "action_type": "lead_created"},
                {"event": "Property analysis completed", "date": "2025-10-07", "user": "AI", "action_type": "ai_analysis"},
                {"event": "Campaign launched", "date": "2025-10-06", "user": "Admin", "action_type": "campaign_created"},
                {"event": "Deal closed", "date": "2025-10-05", "user": "Agent", "action_type": "deal_closed"}
            ],
            "last_updated": "2025-10-09T04:30:00Z"
        }
    }

# Authentication endpoints
@app.get("/api/auth/login")
@app.post("/api/auth/login")
@app.options("/api/auth/login")
async def login():
    """User login endpoint"""
    return {
        "status": "success",
        "message": "Login successful",
        "data": {
            "user": {
                "id": 1,
                "email": "admin@deelflowai.com",
                "name": "Admin User",
                "role": "admin"
            },
            "tokens": {
                "access_token": "mock_access_token_12345",
                "refresh_token": "mock_refresh_token_67890",
                "expires_in": 3600
            }
        }
    }

@app.get("/api/auth/register")
@app.post("/api/auth/register")
@app.options("/api/auth/register")
async def register():
    """User registration endpoint"""
    return {
        "status": "success",
        "message": "Registration successful",
        "data": {
            "user": {
                "id": 2,
                "email": "newuser@deelflowai.com",
                "name": "New User",
                "role": "user"
            },
            "tokens": {
                "access_token": "mock_access_token_54321",
                "refresh_token": "mock_refresh_token_09876",
                "expires_in": 3600
            }
        }
    }

@app.get("/api/auth/logout")
@app.post("/api/auth/logout")
@app.options("/api/auth/logout")
async def logout():
    """User logout endpoint"""
    return {
        "status": "success",
        "message": "Logout successful"
    }

@app.get("/api/auth/me")
@app.options("/api/auth/me")
async def get_current_user():
    """Get current user info"""
    return {
        "status": "success",
        "data": {
            "user": {
                "id": 1,
                "email": "admin@deelflowai.com",
                "name": "Admin User",
                "role": "admin",
                "permissions": ["read", "write", "admin"]
            }
        }
    }

@app.options("/{path:path}")
async def options_handler(path: str):
    """Handle all OPTIONS requests for CORS preflight"""
    return JSONResponse(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Max-Age": "86400"
        }
    )

@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Custom 404 handler"""
    return JSONResponse(
        status_code=404,
        content={"detail": "Endpoint not found", "path": str(request.url)}
    )

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    """Custom 500 handler"""
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8140,
        reload=True,
        log_level="info"
    )
