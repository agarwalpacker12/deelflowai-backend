"""
DeelFlowAI FastAPI Application
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
import os
import sys
import django
import datetime
from pathlib import Path

# Mock data functions (replacing deleted database module)
# Import database functions
from database import (
    get_dashboard_stats,
    get_ai_metrics,
    get_tenant_management_data,
    get_opportunity_cost_data,
    get_revenue_growth_data,
    get_market_alerts_data,
    get_live_activity_data,
    get_performance_metrics
)








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
        "http://dev.deelflowai.com:8140",
        "http://localhost:5173",  # Vite default port
        "http://localhost:5175",
        "http://localhost:3000",
        "http://127.0.0.1:5173",  # Vite default port
        "http://127.0.0.1:5175",
        "http://127.0.0.1:3000"
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

# Dashboard API endpoints
@app.get("/api/total-revenue/")
@app.options("/api/total-revenue/")
async def get_api_total_revenue():
    """Get total revenue metrics"""
    stats = await get_dashboard_stats()
    return {
        "status": "success",
        "data": {
            "totalRevenue": stats.get("totalRevenue", 0),
            "monthlyRevenue": stats.get("monthlyRevenue", 0),
            "growthRate": stats.get("growthRate", 0)
        }
    }

@app.get("/api/active-users/")
@app.options("/api/active-users/")
async def get_api_active_users():
    """Get active users count"""
    stats = await get_dashboard_stats()
    return {
        "status": "success",
        "data": {
            "activeUsers": stats.get("totalUsers", 0),
            "newUsers": stats.get("recentUsers", 0),
            "userGrowth": 15.2
        }
    }

@app.get("/api/properties-listed/")
@app.options("/api/properties-listed/")
async def get_api_properties_listed():
    """Get properties listed count"""
    stats = await get_dashboard_stats()
    return {
        "status": "success",
        "data": {
            "totalProperties": stats.get("totalProperties", 0),
            "activeListings": stats.get("totalProperties", 0),
            "soldThisMonth": stats.get("recentProperties", 0)
        }
    }

@app.get("/api/ai-conversations/")
@app.options("/api/ai-conversations/")
async def get_api_ai_conversations():
    """Get AI conversations count"""
    ai_metrics = await get_ai_metrics()
    return {
        "status": "success",
        "data": {
            "totalConversations": ai_metrics.get("totalAnalyses", 0),
            "activeConversations": ai_metrics.get("totalAnalyses", 0),
            "avgResponseTime": 2.3
        }
    }

@app.get("/api/total-deals/")
@app.options("/api/total-deals/")
async def get_api_total_deals():
    """Get total deals count"""
    stats = await get_dashboard_stats()
    return {
        "status": "success",
        "data": {
            "totalDeals": stats.get("totalDeals", 0),
            "closedThisMonth": stats.get("recentDeals", 0),
            "pendingDeals": stats.get("totalDeals", 0)
        }
    }

@app.get("/api/monthly-profit/")
@app.options("/api/monthly-profit/")
async def get_api_monthly_profit():
    """Get monthly profit metrics"""
    return {
        "status": "success",
        "data": {
            "monthlyProfit": 25000.75,
            "profitMargin": 18.5,
            "profitGrowth": 8.2
        }
    }

@app.get("/api/voice-calls-count/")
@app.options("/api/voice-calls-count/")
async def get_api_voice_calls_count():
    """Get voice calls count"""
    return {
        "status": "success",
        "data": {
            "totalCalls": 89,
            "callsToday": 12,
            "avgCallDuration": 4.5
        }
    }

@app.get("/api/compliance-status/")
@app.options("/api/compliance-status/")
async def get_api_compliance_status():
    """Get compliance status"""
    return {
        "status": "success",
        "data": {
            "complianceScore": 95.5,
            "pendingReviews": 3,
            "lastAudit": "2024-01-15"
        }
    }

@app.get("/api/live-activity-feed/")
@app.options("/api/live-activity-feed/")
async def get_api_live_activity_feed():
    """Get live activity feed"""
    return {
        "status": "success",
        "data": [
            {
                "id": 1,
                "type": "property_viewed",
                "message": "Property 123 Main St viewed by lead",
                "timestamp": "2024-01-15T10:30:00Z"
            },
            {
                "id": 2,
                "type": "deal_updated",
                "message": "Deal #456 status updated to 'Under Contract'",
                "timestamp": "2024-01-15T09:15:00Z"
            }
        ]
    }

@app.get("/api/revenue-user-growth-chart-data/")
@app.options("/api/revenue-user-growth-chart-data/")
async def get_api_revenue_user_growth_chart_data():
    """Get revenue and user growth chart data"""
    return {
        "status": "success",
        "data": {
            "revenueData": [10000, 12000, 15000, 18000, 20000, 22000, 25000],
            "userData": [10, 15, 22, 28, 35, 42, 45],
            "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
        }
    }

@app.get("/api/vision-analysis/")
@app.options("/api/vision-analysis/")
async def get_api_vision_analysis():
    """Get vision analysis metrics"""
    return {
        "status": "success",
        "data": {
            "imagesProcessed": 156,
            "accuracy": 94.2,
            "processingTime": 1.8
        }
    }

@app.get("/api/nlp-processing/")
@app.options("/api/nlp-processing/")
async def get_api_nlp_processing():
    """Get NLP processing metrics"""
    return {
        "status": "success",
        "data": {
            "documentsProcessed": 89,
            "sentimentAccuracy": 91.5,
            "avgProcessingTime": 2.1
        }
    }

@app.get("/api/blockchain-txns/")
@app.options("/api/blockchain-txns/")
async def get_api_blockchain_txns():
    """Get blockchain transactions count"""
    return {
        "status": "success",
        "data": {
            "totalTransactions": 234,
            "pendingTransactions": 12,
            "avgConfirmationTime": 3.2
        }
    }

@app.get("/api/ai-metrics/overall-accuracy/")
@app.options("/api/ai-metrics/overall-accuracy/")
async def get_api_ai_metrics_overall_accuracy():
    """Get AI overall accuracy metrics"""
    return {
        "status": "success",
        "data": {
            "overallAccuracy": 92.8,
            "predictionAccuracy": 89.5,
            "classificationAccuracy": 95.1
        }
    }

@app.get("/api/market-alerts/recent/")
@app.options("/api/market-alerts/recent/")
async def get_api_market_alerts_recent():
    """Get recent market alerts"""
    return {
        "status": "success",
        "data": [
            {
                "id": 1,
                "type": "price_drop",
                "message": "Property prices dropped 5% in downtown area",
                "timestamp": "2024-01-15T08:00:00Z"
            },
            {
                "id": 2,
                "type": "market_trend",
                "message": "High demand detected for 3-bedroom properties",
                "timestamp": "2024-01-15T07:30:00Z"
            }
        ]
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
        "user": {
            "id": user_id,
            "email": user_email,
            "name": "Admin User",
            "role": "admin"
        },
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": 3600,
        "token_type": "bearer"
    }

@app.post("/test-login/")
async def test_login(request: Request):
    """Test login endpoint"""
    try:
        credentials = await request.json()
        return {"status": "success", "data": credentials}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/login/")
async def login_with_trailing_slash(request: Request):
    """User login endpoint with trailing slash to match frontend calls"""
    
    # Get credentials from request body
    try:
        credentials = await request.json()
    except:
        credentials = {}
    
    # Accept both username and email fields
    username_or_email = credentials.get("username") or credentials.get("email", "")
    password = credentials.get("password", "")
    
    # Mock authentication (accept any credentials for now)
    if username_or_email and password:
        user_id = 1
        
        # Create mock tokens (simplified for now)
        access_token = f"mock_access_token_{user_id}_{username_or_email}"
        refresh_token = f"mock_refresh_token_{user_id}_{username_or_email}"
        
        return {
            "status": "success",
            "message": "Login successful",
            "data": {
                "token": access_token,  # Frontend expects 'token' not 'access_token'
                "user": {
                    "id": user_id,
                    "email": username_or_email,
                    "name": "Admin User",
                    "role": "admin"
                }
            },
            "user": {
                "id": user_id,
                "email": username_or_email,
                "name": "Admin User",
                "role": "admin"
            },
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_in": 3600,
            "token_type": "bearer"
        }
    else:
        return JSONResponse(
            status_code=401,
            content={"status": "error", "message": "Invalid credentials"}
        )

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

# ==================== FRONTEND DASHBOARD ENDPOINTS ====================

# Individual metric endpoints that frontend calls
@app.get("/total-revenue/")
@app.options("/total-revenue/")
async def get_total_revenue():
    """Get total revenue with change percentage"""
    return {
        "status": "success",
        "data": {
            "total_revenue": 125000.50,
            "change_percentage": 12.5
        }
    }

@app.get("/active-users/")
@app.options("/active-users/")
async def get_active_users():
    """Get active users with change percentage"""
    return {
        "status": "success",
        "data": {
            "active_users": 150,
            "change_percentage": 8.3
        }
    }

@app.get("/properties-listed/")
@app.options("/properties-listed/")
async def get_properties_listed():
    """Get properties listed with change percentage"""
    return {
        "status": "success",
        "data": {
            "properties_listed": 89,
            "change_percentage": 15.2
        }
    }

@app.get("/ai-conversations/")
@app.options("/ai-conversations/")
async def get_ai_conversations():
    """Get AI conversations with average rate"""
    return {
        "status": "success",
        "data": {
            "ai_conversations": 1250,
            "avg_rate": 87.5
        }
    }

@app.get("/total-deals/")
@app.options("/total-deals/")
async def get_total_deals():
    """Get total deals with change percentage"""
    return {
        "status": "success",
        "data": {
            "total_deals": 47,
            "change_percentage": 22.1
        }
    }

@app.get("/monthly-profit/")
@app.options("/monthly-profit/")
async def get_monthly_profit():
    """Get monthly profit with change percentage"""
    return {
        "status": "success",
        "data": {
            "monthly_profit": 127500.0,
            "change_percentage": 18.7
        }
    }

@app.get("/voice-calls-count/")
@app.options("/voice-calls-count/")
async def get_voice_calls_count_frontend():
    """Get voice calls count for frontend"""
    return {
        "status": "success",
        "data": {
            "voice_calls": 89,
            "change_percentage": 5.2
        }
    }

@app.get("/compliance-status/")
@app.options("/compliance-status/")
async def get_compliance_status():
    """Get compliance status"""
    return {
        "status": "success",
        "data": {
            "compliance_status": 96.0,
            "improvement": 2.5
        }
    }

@app.get("/live-activity-feed/")
@app.options("/live-activity-feed/")
async def get_live_activity_feed():
    """Get live activity feed"""
    return {
        "status": "success",
        "data": {
            "activities": [
                {"event": "New lead added", "timestamp": "2025-10-09T04:25:00Z", "user": "System"},
                {"event": "Property analysis completed", "timestamp": "2025-10-09T04:20:00Z", "user": "AI"},
                {"event": "Deal updated", "timestamp": "2025-10-09T04:15:00Z", "user": "Agent"}
            ]
        }
    }

@app.get("/revenue-user-growth-chart-data/")
@app.options("/revenue-user-growth-chart-data/")
async def get_revenue_user_growth_chart_data():
    """Get revenue and user growth chart data"""
    return {
        "status": "success",
        "data": {
            "revenue_growth": 12.5,
            "user_growth": 8.3,
            "monthly_breakdown": [
                {"month": "Jan", "revenue": 100000, "users": 120},
                {"month": "Feb", "revenue": 110000, "users": 135},
                {"month": "Mar", "revenue": 125000, "users": 150}
            ]
        }
    }

# AI Performance Metrics endpoints
@app.get("/vision-analysis/")
@app.options("/vision-analysis/")
async def get_vision_analysis():
    """Get vision analysis metrics"""
    return {
        "status": "success",
        "data": {
            "total": 89,
            "accuracy": 92.3,
            "processing_time": 2.1
        }
    }

@app.get("/nlp-processing/")
@app.options("/nlp-processing/")
async def get_nlp_processing():
    """Get NLP processing metrics"""
    return {
        "status": "success",
        "data": {
            "total": 234,
            "accuracy": 94.2,
            "avg_response_time": 1.8
        }
    }

@app.get("/blockchain-txns/")
@app.options("/blockchain-txns/")
async def get_blockchain_txns():
    """Get blockchain transactions metrics"""
    return {
        "status": "success",
        "data": {
            "total": 45,
            "success_rate": 98.7,
            "avg_processing_time": 3.5
        }
    }

@app.get("/ai-metrics/overall-accuracy/")
@app.options("/ai-metrics/overall-accuracy/")
async def get_ai_accuracy():
    """Get overall AI accuracy"""
    return {
        "status": "success",
        "data": {
            "ai_accuracy": 94.2,
            "improvement": 5.8
        }
    }

@app.get("/market-alerts/recent/")
@app.options("/market-alerts/recent/")
async def get_market_alerts_recent():
    """Get recent market alerts"""
    return {
        "status": "success",
        "data": {
            "alerts": [
                {"type": "opportunity", "message": "New distressed property in Miami", "priority": "high"},
                {"type": "market", "message": "Price increase in downtown area", "priority": "medium"},
                {"type": "lead", "message": "High-value lead identified", "priority": "high"}
            ]
        }
    }

@app.get("/compliance-status/details/")
@app.options("/compliance-status/details/")
async def get_compliance_details():
    """Get detailed compliance status"""
    return {
        "status": "success",
        "data": {
            "overall_compliance": 96.0,
            "data_privacy": 98.5,
            "security_standards": 94.2,
            "audit_ready": True,
            "last_audit": "2025-10-01T00:00:00Z"
        }
    }

@app.get("/deal-completions-scheduling/")
@app.options("/deal-completions-scheduling/")
async def get_deal_completions_scheduling():
    """Get deal completions scheduling data"""
    return {
        "status": "success",
        "data": {
            "scheduled_completions": 12,
            "completed_this_month": 8,
            "pending_completions": 4,
            "completion_rate": 66.7
        }
    }

@app.get("/current-subscription/")
@app.options("/current-subscription/")
async def get_current_subscription():
    """Get current subscription details"""
    return {
        "status": "success",
        "data": {
            "plan": "premium",
            "features": ["ai_analysis", "voice_calls", "blockchain", "analytics"],
            "expires_at": "2025-12-31T23:59:59Z",
            "usage": {
                "ai_calls": 1250,
                "voice_calls": 89,
                "properties_analyzed": 156
            }
        }
    }

# Tenant Management endpoints (matching frontend expectations)
@app.get("/tenant-management/stats/")
@app.options("/tenant-management/stats/")
async def get_tenant_management_stats_frontend():
    """Get tenant management stats for frontend"""
    return {
        "status": "success",
        "data": {
            "activeTenants": "25",
            "paymentOverdue": "3",
            "suspended": "1",
            "monthlyRevenue": "$25,000"
        }
    }

# ==================== PROPERTY MANAGEMENT ENDPOINTS ====================

@app.get("/api/properties/")
@app.options("/api/properties/")
async def get_properties():
    """Get all properties"""
    return {
        "status": "success",
        "data": [
            {
                "id": 1,
                "address": "123 Main St",
                "unit": None,
                "city": "Atlanta",
                "state": "GA",
                "zip": "30309",
                "county": "Fulton",
                "property_type": "Single Family",
                "bedrooms": 3,
                "bathrooms": 2.0,
                "square_feet": 1500,
                "lot_size": 0.25,
                "year_built": 2010,
                "purchase_price": 200000.0,
                "arv": 250000.0,
                "repair_estimate": 15000.0,
                "holding_costs": 5000.0,
                "transaction_type": "sale",
                "assignment_fee": 10000.0,
                "description": "Beautiful single family home in prime location",
                "seller_notes": "Motivated seller",
                "potential_profit": 25000.0,
                "status": "active",
                "created_at": "2025-10-09T04:30:00Z",
                "updated_at": "2025-10-09T04:30:00Z"
            }
        ],
        "total": 1,
        "page": 1,
        "limit": 20
    }

class PropertyCreate(BaseModel):
    """Property creation request model"""
    address: str
    unit: Optional[str] = None
    city: str
    state: str
    zip: str
    county: Optional[str] = "Unknown"
    property_type: str
    bedrooms: Optional[int] = None
    bathrooms: Optional[float] = None
    square_feet: Optional[int] = None
    lot_size: Optional[float] = None
    year_built: Optional[int] = None
    purchase_price: Optional[float] = None
    arv: Optional[float] = None
    repair_estimate: Optional[float] = None
    holding_costs: Optional[float] = None
    transaction_type: Optional[str] = "sale"
    assignment_fee: Optional[float] = None
    description: str
    seller_notes: Optional[str] = None

class PropertyUpdate(BaseModel):
    """Property update request model - all fields optional for partial updates"""
    address: Optional[str] = None
    unit: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    county: Optional[str] = None
    property_type: Optional[str] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[float] = None
    square_feet: Optional[int] = None
    lot_size: Optional[float] = None
    year_built: Optional[int] = None
    purchase_price: Optional[float] = None
    arv: Optional[float] = None
    repair_estimate: Optional[float] = None
    holding_costs: Optional[float] = None
    transaction_type: Optional[str] = None
    assignment_fee: Optional[float] = None
    description: Optional[str] = None
    seller_notes: Optional[str] = None

@app.get("/properties/")
@app.options("/properties/")
async def get_properties():
    """Get all properties"""
    # Calculate potential profit for each property
    purchase_price = 200000.0
    arv = 250000.0
    repair_estimate = 15000.0
    potential_profit = arv - purchase_price - repair_estimate
    
    return {
        "status": "success",
        "data": [
            {
                "id": 1,
                "address": "123 Main St",
                "unit": "Apt 1",
                "city": "Atlanta",
                "state": "GA",
                "zip": "30309",
                "county": "Fulton",
                "property_type": "Single Family",
                "bedrooms": 3,
                "bathrooms": 2.0,
                "square_feet": 1500,
                "lot_size": 0.25,
                "year_built": 2020,
                "purchase_price": purchase_price,
                "arv": arv,
                "repair_estimate": repair_estimate,
                "holding_costs": 5000.0,
                "transaction_type": "Wholesale",
                "assignment_fee": 10000.0,
                "description": "Beautiful single family home",
                "seller_notes": "Motivated seller",
                "potential_profit": potential_profit,
                "status": "active",
                "created_at": "2025-10-09T04:30:00Z",
                "updated_at": "2025-10-09T04:30:00Z"
            }
        ],
        "total": 1,
        "page": 1,
        "limit": 20
    }

@app.post("/properties/")
@app.options("/properties/")
async def create_property(property_data: PropertyCreate):
    """Create a new property"""
    # Generate a new property ID
    property_id = 2
    
    # Calculate potential profit
    purchase_price = property_data.purchase_price or 0
    arv = property_data.arv or 0
    repair_estimate = property_data.repair_estimate or 0
    potential_profit = arv - purchase_price - repair_estimate
    
    new_property = {
        "id": property_id,
        "address": property_data.address,
        "unit": property_data.unit,
        "city": property_data.city,
        "state": property_data.state,
        "zip": property_data.zip,
        "county": property_data.county,
        "property_type": property_data.property_type,
        "bedrooms": property_data.bedrooms,
        "bathrooms": property_data.bathrooms,
        "square_feet": property_data.square_feet,
        "lot_size": property_data.lot_size,
        "year_built": property_data.year_built,
        "purchase_price": property_data.purchase_price,
        "arv": property_data.arv,
        "repair_estimate": property_data.repair_estimate,
        "holding_costs": property_data.holding_costs,
        "transaction_type": property_data.transaction_type,
        "assignment_fee": property_data.assignment_fee,
        "description": property_data.description,
        "seller_notes": property_data.seller_notes,
        "potential_profit": potential_profit,
        "status": "active",
        "created_at": "2025-10-09T04:30:00Z",
        "updated_at": "2025-10-09T04:30:00Z"
    }
    
    return {
        "status": "success",
        "message": "Property created successfully",
        "data": new_property
    }

@app.post("/api/properties/")
@app.options("/api/properties/")
async def create_property_api(property_data: PropertyCreate):
    """Create a new property via /api/properties/ endpoint"""
    # Generate a new property ID
    property_id = 2
    
    # Calculate potential profit
    purchase_price = property_data.purchase_price or 0
    arv = property_data.arv or 0
    repair_estimate = property_data.repair_estimate or 0
    potential_profit = arv - purchase_price - repair_estimate
    
    new_property = {
        "id": property_id,
        "address": property_data.address,
        "unit": property_data.unit,
        "city": property_data.city,
        "state": property_data.state,
        "zip": property_data.zip,
        "county": property_data.county,
        "property_type": property_data.property_type,
        "bedrooms": property_data.bedrooms,
        "bathrooms": property_data.bathrooms,
        "square_feet": property_data.square_feet,
        "lot_size": property_data.lot_size,
        "year_built": property_data.year_built,
        "purchase_price": purchase_price,
        "arv": arv,
        "repair_estimate": repair_estimate,
        "holding_costs": property_data.holding_costs,
        "transaction_type": property_data.transaction_type,
        "assignment_fee": property_data.assignment_fee,
        "description": property_data.description,
        "seller_notes": property_data.seller_notes,
        "potential_profit": potential_profit,
        "status": "active",
        "created_at": "2025-10-09T04:30:00Z",
        "updated_at": "2025-10-09T04:30:00Z"
    }
    
    return {
        "status": "success",
        "message": "Property created successfully",
        "data": new_property
    }

# Store updated properties in memory for testing
updated_properties = {}

@app.get("/properties/{property_id}/")
@app.options("/properties/{property_id}/")
async def get_property(property_id: int):
    """Get a specific property by ID"""
    # Check if property has been updated
    if property_id in updated_properties:
        return {
            "status": "success",
            "data": updated_properties[property_id]
        }
    
    # Default property data
    return {
        "status": "success",
        "data": {
            "id": property_id,
            "address": "123 Main St",
            "unit": "Apt 1",
            "city": "Atlanta",
            "state": "GA",
            "zip": "30309",
            "county": "Fulton",
            "property_type": "Single Family",
            "bedrooms": 3,
            "bathrooms": 2.0,
            "square_feet": 1500,
            "lot_size": 0.25,
            "year_built": 2020,
            "purchase_price": 200000.0,
            "arv": 250000.0,
            "repair_estimate": 15000.0,
            "holding_costs": 5000.0,
            "transaction_type": "Wholesale",
            "assignment_fee": 10000.0,
            "description": "Beautiful single family home",
            "seller_notes": "Motivated seller",
            "potential_profit": 35000.0,
            "status": "active",
            "created_at": "2025-10-09T04:30:00Z",
            "updated_at": "2025-10-09T04:30:00Z"
        }
    }

@app.put("/properties/{property_id}/")
@app.options("/properties/{property_id}/")
async def update_property(property_id: int, property_data: PropertyUpdate):
    """Update a property"""
    # Filter out None values for partial updates
    update_data = {k: v for k, v in property_data.dict().items() if v is not None}
    
    # Store the updated property data
    updated_property = {
        "id": property_id,
        "address": update_data.get("address", "123 Main St"),
        "unit": update_data.get("unit", "Apt 1"),
        "city": update_data.get("city", "Atlanta"),
        "state": update_data.get("state", "GA"),
        "zip": update_data.get("zip", "30309"),
        "county": update_data.get("county", "Fulton"),
        "property_type": update_data.get("property_type", "Single Family"),
        "bedrooms": update_data.get("bedrooms", 3),
        "bathrooms": update_data.get("bathrooms", 2.0),
        "square_feet": update_data.get("square_feet", 1500),
        "lot_size": update_data.get("lot_size", 0.25),
        "year_built": update_data.get("year_built", 2020),
        "purchase_price": update_data.get("purchase_price", 200000.0),
        "arv": update_data.get("arv", 250000.0),
        "repair_estimate": update_data.get("repair_estimate", 15000.0),
        "holding_costs": update_data.get("holding_costs", 5000.0),
        "transaction_type": update_data.get("transaction_type", "Wholesale"),
        "assignment_fee": update_data.get("assignment_fee", 10000.0),
        "description": update_data.get("description", "Beautiful single family home"),
        "seller_notes": update_data.get("seller_notes", "Motivated seller"),
        "potential_profit": 35000.0,
        "status": "active",
        "created_at": "2025-10-09T04:30:00Z",
        "updated_at": "2025-10-09T04:30:00Z"
    }
    
    # Store the updated property
    updated_properties[property_id] = updated_property
    
    return {
        "status": "success",
        "message": "Property updated successfully",
        "data": updated_property
    }

@app.delete("/properties/{property_id}/")
@app.options("/properties/{property_id}/")
async def delete_property(property_id: int):
    """Delete a property"""
    return {
        "status": "success",
        "message": "Property deleted successfully"
    }

@app.get("/properties/{property_id}/ai-analysis/")
@app.options("/properties/{property_id}/ai-analysis/")
async def get_property_ai_analysis(property_id: int):
    """Get AI analysis for a property"""
    return {
        "status": "success",
        "data": {
            "property_id": property_id,
            "analysis_type": "property_valuation",
            "confidence_score": 87.5,
            "recommended_price": 245000.0,
            "market_analysis": {
                "comparable_properties": 12,
                "average_price_per_sqft": 163.33,
                "market_trend": "increasing"
            },
            "risk_assessment": {
                "overall_risk": "low",
                "location_score": 8.5,
                "condition_score": 7.2
            },
            "recommendations": [
                "Property shows strong investment potential",
                "Consider minor cosmetic updates to increase value",
                "Market conditions are favorable for this area"
            ],
            "created_at": "2025-10-09T04:30:00Z"
        }
    }

# ==================== CAMPAIGN MANAGEMENT ENDPOINTS ====================

class CampaignCreate(BaseModel):
    """Campaign creation request model with all required fields"""
    # Basic campaign information
    name: str
    campaign_type: str
    channel: str = "email"
    budget: float
    scheduled_at: str
    subject_line: str
    email_content: str
    use_ai_personalization: bool = True
    status: str = "draft"
    
    # Geographic scope (for general campaigns)
    geographic_scope_type: str = "zip"
    geographic_scope_values: List[str] = []
    
    # Basic property filters
    location: str = "Atlanta, GA"
    property_type: str = "Single Family"
    minimum_equity: float = 0
    min_price: float = 250000
    max_price: float = 750000
    distress_indicators: List[str] = []
    
    # Buyer Finder - Demographic Details
    last_qualification: str = ""
    age_range: str = ""
    ethnicity: str = ""
    salary_range: str = ""
    marital_status: str = ""
    employment_status: str = ""
    home_ownership_status: str = ""
    
    # Buyer Finder - Geographic Details
    buyer_country: str = ""
    buyer_state: str = ""
    buyer_counties: str = ""
    buyer_city: str = ""
    buyer_districts: str = ""
    buyer_parish: str = ""
    
    # Seller Finder - Geographic Details
    seller_country: str = ""
    seller_state: str = ""
    seller_counties: str = ""
    seller_city: str = ""
    seller_districts: str = ""
    seller_parish: str = ""
    
    # Seller Finder - Additional Fields
    property_year_built_min: str = ""
    property_year_built_max: str = ""
    seller_keywords: str = ""

class CampaignUpdate(BaseModel):
    """Campaign update request model - all fields optional for partial updates"""
    name: Optional[str] = None
    campaign_type: Optional[str] = None
    channel: Optional[str] = None
    budget: Optional[float] = None
    scheduled_at: Optional[str] = None
    subject_line: Optional[str] = None
    email_content: Optional[str] = None
    use_ai_personalization: Optional[bool] = None
    status: Optional[str] = None
    geographic_scope_type: Optional[str] = None
    geographic_scope_values: Optional[List[str]] = None
    location: Optional[str] = None
    property_type: Optional[str] = None
    minimum_equity: Optional[float] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    distress_indicators: Optional[List[str]] = None
    last_qualification: Optional[str] = None
    age_range: Optional[str] = None
    ethnicity: Optional[str] = None
    salary_range: Optional[str] = None
    marital_status: Optional[str] = None
    employment_status: Optional[str] = None
    home_ownership_status: Optional[str] = None
    buyer_country: Optional[str] = None
    buyer_state: Optional[str] = None
    buyer_counties: Optional[str] = None
    buyer_city: Optional[str] = None
    buyer_districts: Optional[str] = None
    buyer_parish: Optional[str] = None
    seller_country: Optional[str] = None
    seller_state: Optional[str] = None
    seller_counties: Optional[str] = None
    seller_city: Optional[str] = None
    seller_districts: Optional[str] = None
    seller_parish: Optional[str] = None
    property_year_built_min: Optional[str] = None
    property_year_built_max: Optional[str] = None
    seller_keywords: Optional[str] = None

@app.get("/campaigns/")
@app.options("/campaigns/")
async def get_campaigns():
    """Get all campaigns"""
    return {
        "status": "success",
        "data": [
            {
                "id": 1,
                "name": "Q4 Property Marketing Campaign",
                "campaign_type": "new",
                "channel": "email",
                "budget": 5000.0,
                "scheduled_at": "2025-10-15T09:00:00Z",
                "subject_line": "Exclusive Property Investment Opportunities",
                "email_content": "Discover amazing real estate investment opportunities...",
                "use_ai_personalization": True,
                "status": "active",
                "geographic_scope_type": "zip",
                "geographic_scope_values": ["30309", "30310", "30311"],
                "location": "Atlanta, GA",
                "property_type": "Single Family",
                "minimum_equity": 50000,
                "min_price": 200000,
                "max_price": 500000,
                "distress_indicators": ["foreclosure", "short_sale"],
                "last_qualification": "2025-10-01",
                "age_range": "25-55",
                "ethnicity": "all",
                "salary_range": "50000-150000",
                "marital_status": "all",
                "employment_status": "employed",
                "home_ownership_status": "renting",
                "buyer_country": "USA",
                "buyer_state": "GA",
                "buyer_counties": "Fulton, DeKalb",
                "buyer_city": "Atlanta",
                "buyer_districts": "Downtown, Midtown",
                "buyer_parish": "",
                "seller_country": "USA",
                "seller_state": "GA",
                "seller_counties": "Fulton, DeKalb",
                "seller_city": "Atlanta",
                "seller_districts": "Downtown, Midtown",
                "seller_parish": "",
                "property_year_built_min": "1990",
                "property_year_built_max": "2020",
                "seller_keywords": "motivated, quick sale, investment",
                "created_at": "2025-10-09T04:30:00Z",
                "updated_at": "2025-10-09T04:30:00Z"
            }
        ],
        "total": 1,
        "page": 1,
        "limit": 20
    }

@app.post("/campaigns/")
@app.options("/campaigns/")
async def create_campaign(campaign_data: CampaignCreate):
    """Create a new campaign"""
    # Generate a new campaign ID
    campaign_id = 2
    
    new_campaign = {
        "id": campaign_id,
        **campaign_data.dict(),
        "created_at": "2025-10-09T04:30:00Z",
        "updated_at": "2025-10-09T04:30:00Z"
    }
    
    return {
        "status": "success",
        "message": "Campaign created successfully",
        "data": new_campaign
    }

@app.get("/campaigns/{campaign_id}/")
@app.options("/campaigns/{campaign_id}/")
async def get_campaign(campaign_id: int):
    """Get a specific campaign by ID"""
    return {
        "status": "success",
        "data": {
            "id": campaign_id,
            "name": "Sample Campaign",
            "campaign_type": "new",
            "channel": "email",
            "budget": 5000.0,
            "scheduled_at": "2025-10-15T09:00:00Z",
            "subject_line": "Exclusive Property Investment Opportunities",
            "email_content": "Discover amazing real estate investment opportunities...",
            "use_ai_personalization": True,
            "status": "active",
            "geographic_scope_type": "zip",
            "geographic_scope_values": ["30309", "30310"],
            "location": "Atlanta, GA",
            "property_type": "Single Family",
            "minimum_equity": 50000,
            "min_price": 200000,
            "max_price": 500000,
            "distress_indicators": ["foreclosure"],
            "created_at": "2025-10-09T04:30:00Z",
            "updated_at": "2025-10-09T04:30:00Z"
        }
    }

@app.put("/campaigns/{campaign_id}/")
@app.options("/campaigns/{campaign_id}/")
async def update_campaign(campaign_id: int, campaign_data: CampaignUpdate):
    """Update a campaign"""
    # Filter out None values for partial updates
    update_data = {k: v for k, v in campaign_data.dict().items() if v is not None}
    
    return {
        "status": "success",
        "message": "Campaign updated successfully",
        "data": {
            "id": campaign_id,
            **update_data,
            "updated_at": "2025-10-09T04:30:00Z"
        }
    }

@app.delete("/campaigns/{campaign_id}/")
@app.options("/campaigns/{campaign_id}/")
async def delete_campaign(campaign_id: int):
    """Delete a campaign"""
    return {
        "status": "success",
        "message": "Campaign deleted successfully"
    }

# Add missing endpoints that frontend is calling directly
@app.get("/overall-accuracy")
@app.options("/overall-accuracy")
@app.get("/overall-accuracy/")
@app.options("/overall-accuracy/")
async def get_overall_accuracy_direct():
    """Get overall AI accuracy - direct endpoint"""
    return {
        "status": "success",
        "data": {
            "ai_accuracy": 94.2,
            "improvement": 5.8
        }
    }

@app.get("/recent")
@app.options("/recent")
@app.get("/recent/")
@app.options("/recent/")
async def get_recent_direct():
    """Get recent market alerts - direct endpoint"""
    return {
        "status": "success",
        "data": {
            "alerts": [
                {
                    "type": "opportunity",
                    "message": "New distressed property in Miami",
                    "priority": "high"
                },
                {
                    "type": "market",
                    "message": "Price increase in downtown area",
                    "priority": "medium"
                }
            ]
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
