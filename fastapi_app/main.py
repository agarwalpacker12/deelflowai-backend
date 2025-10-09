"""
DeelFlowAI FastAPI Application
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import os
import sys
import django
from pathlib import Path

# Mock data functions (replacing deleted database module)
def get_dashboard_stats():
    """Mock dashboard statistics"""
    return {
        'total_revenue': 125000.50,
        'active_users': 150,
        'total_properties': 89,
        'total_deals': 45,
        'monthly_profit': 25000.75,
        'ai_conversations': 1250,
        'ai_accuracy': 87.5,
        'voice_calls': 156,
        'compliance_status': 'healthy'
    }

def get_ai_metrics():
    """Mock AI metrics data"""
    return {
        'vision_accuracy': 92.3,
        'nlp_accuracy': 88.7,
        'voice_success_rate': 87.5,
        'blockchain_success_rate': 95.2,
        'overall_performance': 90.9,
        'total_analyses': 1250,
        'processing_time_avg': 2.3
    }

def get_tenant_management_data():
    """Mock tenant management data"""
    return {
        'total_tenants': 25,
        'active_tenants': 23,
        'inactive_tenants': 2,
        'total_users': 150,
        'monthly_revenue': 25000.75,
        'growth_rate': 12.5
    }

def get_opportunity_cost_data():
    """Mock opportunity cost data"""
    return {
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

def get_revenue_growth_data():
    """Mock revenue growth data"""
    return {
        'revenue_growth': 12.5,
        'user_growth': 8.3,
        'property_growth': 15.2,
        'deal_growth': 22.1,
        'profit_growth': 18.7,
        'monthly_breakdown': [
            {'month': 'Jan', 'revenue': 100000},
            {'month': 'Feb', 'revenue': 110000},
            {'month': 'Mar', 'revenue': 125000}
        ]
    }

def get_market_alerts_data():
    """Mock market alerts data"""
    return {
        'alerts': [
            {'type': 'opportunity', 'message': 'New distressed property in Miami', 'priority': 'high'},
            {'type': 'market', 'message': 'Price increase in downtown area', 'priority': 'medium'},
            {'type': 'lead', 'message': 'High-value lead identified', 'priority': 'high'}
        ],
        'opportunities': 5,
        'warnings': 2,
        'last_updated': '2025-10-09T04:30:00Z'
    }

def get_live_activity_data():
    """Mock live activity data"""
    return {
        'activities': [
            {'event': 'New lead added', 'timestamp': '2025-10-09T04:25:00Z', 'user': 'System'},
            {'event': 'Property analysis completed', 'timestamp': '2025-10-09T04:20:00Z', 'user': 'AI'},
            {'event': 'Deal updated', 'timestamp': '2025-10-09T04:15:00Z', 'user': 'Agent'},
            {'event': 'Campaign launched', 'timestamp': '2025-10-09T04:10:00Z', 'user': 'Admin'}
        ],
        'total_activities': 156,
        'last_updated': '2025-10-09T04:30:00Z'
    }

def get_performance_metrics():
    """Mock performance metrics"""
    return {
        'overall_score': 87.5,
        'response_time': 1.2,
        'uptime': 99.9,
        'error_rate': 0.1,
        'user_satisfaction': 4.5,
        'system_health': 'excellent',
        'last_updated': '2025-10-09T04:30:00Z'
    }

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
    try:
        # Get data from database
        db_stats = get_dashboard_stats()
        
        return {
            'status': 'success',
            'data': {
                'total_revenue': db_stats['total_revenue'],
                'revenue_growth': 12.5,  # This would be calculated from historical data
                'active_users': db_stats['active_users'],
                'users_growth': 8.3,
                'properties_listed': db_stats['total_properties'],
                'properties_growth': 15.2,
                'ai_conversations': db_stats['ai_conversations'],
                'conversation_rate': 87.5,
                'total_deals': db_stats['total_deals'],
                'deals_growth': 22.1,
                'monthly_profit': db_stats['monthly_profit'],
                'profit_growth': 18.7,
                'ai_accuracy': db_stats['ai_accuracy'],
                'accuracy_improvement': 5.8,
                'voice_calls': db_stats['voice_calls'],
                'compliance_status': db_stats['compliance_status']
            }
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to fetch stats: {str(e)}',
            'data': {}
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
            'lostRevenue': 15000.50,
            'lostRevenueDescription': 'Revenue lost due to delayed deal closures and missed opportunities',
            'potentialRevenue': 200000.00,
            'currentRevenue': 125000.50,
            'projectedRevenue': 175000.75,
            'optimizationNeeded': 'Lead conversion process and property listing strategy',
            'roiConversionEfficiency': 78.5,
            'peakTimeMonths': ['March', 'April', 'May', 'September', 'October'],
            'peakDescription': 'Spring and fall seasons show highest property activity and deal closures'
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
            'lostRevenue': 15000.50,
            'lostRevenueDescription': 'Revenue lost due to delayed deal closures and missed opportunities',
            'potentialRevenue': 200000.00,
            'currentRevenue': 125000.50,
            'projectedRevenue': 175000.75,
            'optimizationNeeded': 'Lead conversion process and property listing strategy',
            'roiConversionEfficiency': 78.5,
            'peakTimeMonths': ['March', 'April', 'May', 'September', 'October'],
            'peakDescription': 'Spring and fall seasons show highest property activity and deal closures'
        }
    }

@app.get("/api/tenant-management/stats")
@app.options("/api/tenant-management/stats")
async def get_tenant_management_stats():
    """Get tenant management statistics"""
    return {
        'status': 'success',
        'data': {
            'activeTenants': "0",
            'paymentOverdue': "0",
            'suspended': "0",
            'monthlyRevenue': "$0"
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
            'activeTenants': "0",
            'paymentOverdue': "0",
            'suspended': "0",
            'monthlyRevenue': "$0"
        }
    }

@app.get("/api/analytics/opportunity-cost-analysis/")
@app.options("/api/analytics/opportunity-cost-analysis/")
async def get_analytics_opportunity_cost_analysis_trailing():
    """Get analytics opportunity cost analysis with trailing slash"""
    return {
        'status': 'success',
        'data': {
            'lostRevenue': 15000.50,
            'lostRevenueDescription': 'Revenue lost due to delayed deal closures and missed opportunities',
            'potentialRevenue': 200000.00,
            'currentRevenue': 125000.50,
            'projectedRevenue': 175000.75,
            'optimizationNeeded': 'Lead conversion process and property listing strategy',
            'roiConversionEfficiency': 78.5,
            'peakTimeMonths': ['March', 'April', 'May', 'September', 'October'],
            'peakDescription': 'Spring and fall seasons show highest property activity and deal closures'
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
    from app.core.security import create_access_token, create_refresh_token
    import uuid
    import time
    
    # Generate dynamic tokens
    user_id = 1
    user_email = "admin@deelflowai.com"
    
    # Create JWT tokens
    access_token = create_access_token(data={"sub": user_email, "user_id": user_id})
    refresh_token = create_refresh_token(data={"sub": user_email, "user_id": user_id})
    
    return {
        "status": "success",
        "message": "Login successful",
        "data": {
            "user": {
                "id": user_id,
                "email": user_email,
                "name": "Admin User",
                "role": "admin"
            },
            "tokens": {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "expires_in": 3600,
                "token_type": "bearer"
            }
        }
    }

class RegisterRequest(BaseModel):
    """Registration request model"""
    first_name: str
    last_name: str
    organization_name: str
    phone: Optional[str] = None
    email: str
    password: str

@app.get("/api/auth/register")
@app.post("/api/auth/register")
@app.options("/api/auth/register")
async def register(request: RegisterRequest = None):
    """User registration endpoint"""
    from app.core.security import create_access_token, create_refresh_token
    import uuid
    import time
    
    # If it's a GET request, return registration form info
    if request is None:
        return {
            "status": "info",
            "message": "Please send POST request with registration data",
            "required_fields": [
                "first_name",
                "last_name", 
                "organization_name",
                "phone",
                "email",
                "password"
            ]
        }
    
    # Generate dynamic tokens for new user
    user_id = 2
    user_email = request.email
    full_name = f"{request.first_name} {request.last_name}"
    
    # Create JWT tokens
    access_token = create_access_token(data={"sub": user_email, "user_id": user_id})
    refresh_token = create_refresh_token(data={"sub": user_email, "user_id": user_id})
    
    return {
        "status": "success",
        "message": "Registration successful",
        "data": {
            "user": {
                "id": user_id,
                "email": user_email,
                "first_name": request.first_name,
                "last_name": request.last_name,
                "full_name": full_name,
                "phone": request.phone,
                "organization_name": request.organization_name,
                "role": "user"
            },
            "tokens": {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "expires_in": 3600,
                "token_type": "bearer"
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
async def get_current_user(authorization: str = None):
    """Get current user info"""
    from app.core.security import get_current_user as get_user_from_token
    from fastapi import Header, HTTPException
    
    try:
        # Extract token from Authorization header
        if authorization and authorization.startswith("Bearer "):
            token = authorization.split(" ")[1]
            # For now, return mock user data (in production, validate the token)
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
        else:
            # No token provided, return error
            raise HTTPException(status_code=401, detail="Authorization token required")
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

# ==================== DASHBOARD API ENDPOINTS ====================

@app.get("/api/dashboard/overview")
@app.options("/api/dashboard/overview")
async def get_dashboard_overview():
    """Get dashboard overview data"""
    try:
        # Get data from database
        db_stats = get_dashboard_stats()
        
        return {
            'status': 'success',
            'data': {
                'total_revenue': db_stats['total_revenue'],
                'revenue_growth': 12.5,
                'active_users': db_stats['active_users'],
                'users_growth': 8.3,
                'properties_listed': db_stats['total_properties'],
                'properties_growth': 15.2,
                'ai_conversations': db_stats['ai_conversations'],
                'conversation_rate': 87.5,
                'total_deals': db_stats['total_deals'],
                'deals_growth': 22.1,
                'monthly_profit': db_stats['monthly_profit'],
                'profit_growth': 18.7,
                'ai_accuracy': db_stats['ai_accuracy'],
                'accuracy_improvement': 5.8,
                'voice_calls': db_stats['voice_calls'],
                'compliance_status': db_stats['compliance_status']
            }
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to fetch dashboard overview: {str(e)}',
            'data': {}
        }

@app.get("/api/dashboard/ai-metrics")
@app.options("/api/dashboard/ai-metrics")
async def get_dashboard_ai_metrics():
    """Get AI performance metrics"""
    try:
        # Get data from database
        ai_data = get_ai_metrics()
        
        return {
            'status': 'success',
            'data': ai_data
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to fetch AI metrics: {str(e)}',
            'data': {}
        }

@app.get("/api/dashboard/tenant-management")
@app.options("/api/dashboard/tenant-management")
async def get_dashboard_tenant_management():
    """Get tenant management overview"""
    try:
        # Get data from database
        tenant_data = get_tenant_management_data()
        
        return {
            'status': 'success',
            'data': tenant_data
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to fetch tenant management data: {str(e)}',
            'data': {}
        }

@app.get("/api/dashboard/opportunity-cost")
@app.options("/api/dashboard/opportunity-cost")
async def get_dashboard_opportunity_cost():
    """Get opportunity cost analysis"""
    try:
        # Get data from database
        opportunity_data = get_opportunity_cost_data()
        
        return {
            'status': 'success',
            'data': opportunity_data
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to fetch opportunity cost data: {str(e)}',
            'data': {}
        }

@app.get("/api/dashboard/revenue-growth")
@app.options("/api/dashboard/revenue-growth")
async def get_dashboard_revenue_growth():
    """Get revenue and user growth data"""
    try:
        # Get data from database
        revenue_data = get_revenue_growth_data()
        
        return {
            'status': 'success',
            'data': revenue_data
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to fetch revenue growth data: {str(e)}',
            'data': {}
        }

@app.get("/api/dashboard/market-alerts")
@app.options("/api/dashboard/market-alerts")
async def get_dashboard_market_alerts():
    """Get market alerts and opportunities"""
    try:
        # Get data from database
        alerts_data = get_market_alerts_data()
        
        return {
            'status': 'success',
            'data': alerts_data
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to fetch market alerts: {str(e)}',
            'data': {}
        }

@app.get("/api/dashboard/live-activity")
@app.options("/api/dashboard/live-activity")
async def get_dashboard_live_activity():
    """Get live activity feed"""
    try:
        # Get data from database
        activity_data = get_live_activity_data()
        
        return {
            'status': 'success',
            'data': activity_data
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to fetch live activity: {str(e)}',
            'data': {}
        }

@app.get("/api/dashboard/performance")
@app.options("/api/dashboard/performance")
async def get_dashboard_performance_metrics():
    """Get overall performance metrics"""
    try:
        # Get data from database
        performance_data = get_performance_metrics()
        
        return {
            'status': 'success',
            'data': performance_data
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to fetch performance metrics: {str(e)}',
            'data': {}
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
