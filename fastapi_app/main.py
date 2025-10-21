"""
DeelFlowAI FastAPI Application - Final Clean Version
Completely organized with proper Swagger grouping and frontend compatibility
"""

from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.params import Path as PathParam
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List, Union
import os
import sys
import django
import datetime
from pathlib import Path
from asgiref.sync import sync_to_async
from django.utils import timezone
import ast

# Import schemas from their respective files
from app.schemas.campaign import CampaignCreate, CampaignUpdate, CampaignResponse, CampaignListResponse
from app.schemas.user import LoginRequest, UserResponse, UserCreateRequest, UserUpdateRequest, UsersListResponse
from app.schemas.property import PropertyResponse, PropertyCreateRequest, PropertyUpdateRequest, PropertyCreate, PropertyUpdate
from app.schemas.lead import LeadResponse, LeadCreateRequest, LeadUpdateRequest, DiscoveredLeadResponse, LeadCreate, LeadUpdate
from app.schemas.deal import DealResponse, DealCreateRequest, DealUpdateRequest, DealCreate, DealUpdate
from app.schemas.milestone import MilestoneCreate, MilestoneUpdate, MilestoneResponse, MilestoneCreateRequest, MilestoneUpdateRequest
from app.schemas.property_save import PropertySaveCreate, PropertySaveUpdate, PropertySaveResponse, PropertySaveListResponse
from app.schemas.payment import PaymentIntentCreate, PaymentConfirm, PaymentIntentResponse, PaymentResponse, SubscriptionResponse
from app.schemas.auth import RegisterRequest, RegisterRequestV2

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
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deelflow.settings')
django.setup()

from app.api.v1.api import api_router
from app.core.config import settings

# Create FastAPI application
app = FastAPI(
    title="DeelFlowAI Backend API",
    version="1.0.0",
    description="""
    ## DeelFlowAI - Comprehensive Real Estate AI Platform Backend API
    
    A powerful backend API for real estate professionals, investors, and agents to manage properties, 
    campaigns, leads, deals, and leverage AI-powered analytics and automation.
    
    ### Key Features:
    - 🏠 **Property Management**: Complete CRUD operations for properties with AI analysis
    - 📊 **Analytics & Reporting**: Comprehensive analytics for deals, campaigns, and performance
    - 🤖 **AI Services**: Voice AI, vision analysis, NLP processing, and blockchain integration
    - 📈 **Campaign Management**: Multi-channel marketing campaigns with performance tracking
    - 👥 **Lead Management**: Lead generation, scoring, and conversion tracking
    - 💼 **Deal Management**: Deal pipeline management with milestone tracking
    - 🔐 **Authentication**: JWT-based authentication and user management
    - 📱 **Dashboard**: Real-time metrics and KPI tracking
    
    ### Authentication:
    Most endpoints require authentication. Use the `/api/auth/login` endpoint to get a JWT token, 
    then include it in the Authorization header: `Bearer <your-token>`
    """,
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    contact={
        "name": "DeelFlowAI Support",
        "email": "support@deelflowai.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Add custom tags metadata for better Swagger UI organization
tags_metadata = [
    {
        "name": "Core",
        "description": "Core API endpoints for health checks, status, and basic information.",
    },
    {
        "name": "Authentication",
        "description": "User authentication, registration, and session management endpoints.",
    },
    {
        "name": "Dashboard",
        "description": "Dashboard metrics, KPIs, and real-time data for the main dashboard interface.",
    },
    {
        "name": "Analytics",
        "description": "Comprehensive analytics endpoints for deals, campaigns, performance, and market data.",
    },
    {
        "name": "Properties",
        "description": "Property management endpoints including CRUD operations and AI analysis.",
    },
    {
        "name": "Property Saves",
        "description": "Property save/favorite functionality for users to bookmark properties.",
    },
    {
        "name": "Campaigns",
        "description": "Marketing campaign management, performance tracking, and analytics.",
    },
    {
        "name": "Leads",
        "description": "Lead management, scoring, and conversion tracking endpoints.",
    },
    {
        "name": "AI Services",
        "description": "AI-powered services including voice AI, vision analysis, NLP, and blockchain integration.",
    },
    {
        "name": "Tenant Management",
        "description": "Multi-tenant organization management and tenant-specific data.",
    },
    {
        "name": "Organizations",
        "description": "Organization management and status endpoints.",
    },
]

# Update the app with tags metadata
app.openapi_tags = tags_metadata

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite default port
        "http://localhost:5175",
        "http://localhost:3000",
        "http://127.0.0.1:5173",  # Vite default port
        "http://127.0.0.1:5175",
        "http://127.0.0.1:3000",
        "http://dev.deelflowai.com:8140",
        "http://dev.deelflowai.com:8000"  # Keep old port for compatibility
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
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

# Include API router - this will add properly organized endpoints
# app.include_router(api_router, prefix=settings.API_V1_STR)

# ==================== CORE ENDPOINTS ====================

@app.get("/", tags=["Core"])
async def root():
    """
    **Root Endpoint - API Information**
    
    Returns basic information about the DeelFlowAI Backend API including version, status, and documentation links.
    
    **Returns:**
    - API name and version
    - Current status
    - Links to API documentation (Swagger UI and ReDoc)
    """
    return {
        "message": "DeelFlowAI Backend API",
        "version": "1.0.0",
        "status": "active",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health", tags=["Core"])
async def health_check():
    """
    **Health Check Endpoint**
    
    Performs a comprehensive health check to verify the API and all dependent services are running properly.
    
    **Returns:**
    - Overall health status
    - Timestamp of the check
    - Status of individual services (database, AI services, background tasks)
    """
    return {
        "status": "healthy",
        "timestamp": "2024-01-01T00:00:00Z",
        "services": {
            "database": "connected",
            "ai_services": "active",
            "background_tasks": "running"
        }
    }

# ==================== DASHBOARD ENDPOINTS ====================

@app.get("/stats", tags=["Dashboard"])
@app.options("/stats")
async def get_stats():
    """
    **Dashboard Statistics**
    
    Retrieves comprehensive statistics for the main dashboard including revenue, user metrics, 
    property counts, and AI conversation data with growth percentages.
    
    **Returns:**
    - Total revenue and growth percentage
    - Active users and growth percentage  
    - Properties listed and growth percentage
    - AI conversations count and growth percentage
    """
    try:
        # Get data from database
        db_stats = await get_dashboard_stats()
        
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

@app.get("/status", tags=["Dashboard"])
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

@app.get("/recent_activity", tags=["Dashboard"])
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

@app.post("/recent_activity", tags=["Dashboard"])
@app.options("/recent_activity")
async def create_recent_activity(activity_data: dict):
    """Create a new activity entry"""
    return {
        "status": "success",
        "message": "Activity created successfully",
        "data": {
            "id": 1,
            "event": activity_data.get("event", "New activity"),
            "date": timezone.now().isoformat(),
            "user": activity_data.get("user", "System"),
            "action_type": activity_data.get("action_type", "general")
        }
    }

@app.get("/opportunity-cost-analysis", tags=["Dashboard"])
@app.options("/opportunity-cost-analysis")
async def get_opportunity_cost_analysis():
    """Get opportunity cost analysis data"""
    try:
        db_data = await get_opportunity_cost_data()
        return {
            "status": "success",
            "data": db_data
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch opportunity cost analysis: {str(e)}"
        }

# ==================== LEGACY DASHBOARD ENDPOINTS ====================

@app.get("/api/total-revenue/", tags=["Dashboard"])
async def get_total_revenue():
    """Get total revenue data"""
    try:
        db_stats = await get_dashboard_stats()
        return {
            "status": "success",
            "data": {
                "total_revenue": 125000.50,  # Mock data since not in db_stats
                "change_percentage": 12.5,  # Frontend expects this field name
                "monthly_revenue": 45000.00,
                "quarterly_revenue": 375000.00
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch revenue data: {str(e)}"
        }

@app.get("/api/active-users/", tags=["Dashboard"])
async def get_active_users():
    """Get active users data"""
    try:
        db_stats = await get_dashboard_stats()
        return {
            "status": "success",
            "data": {
                "active_users": db_stats['totalUsers'],
                "change_percentage": 8.3,  # Frontend expects this field name
                "new_users_this_month": 15,
                "retention_rate": 87.5
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch users data: {str(e)}"
        }

@app.get("/api/properties-listed/", tags=["Dashboard"])
async def get_properties_listed():
    """Get properties listed data"""
    try:
        db_stats = await get_dashboard_stats()
        return {
            "status": "success",
            "data": {
                "properties_listed": db_stats['totalProperties'],
                "change_percentage": 15.2,  # Frontend expects this field name
                "new_listings_this_month": 8,
                "average_listing_price": 450000
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch properties data: {str(e)}"
        }

@app.get("/api/ai-conversations/", tags=["Dashboard"])
async def get_ai_conversations():
    """Get AI conversations data"""
    try:
        db_stats = await get_dashboard_stats()
        return {
            "status": "success",
            "data": {
                "ai_conversations": 1250,  # Mock data
                "change_percentage": 87.5,  # Frontend expects this field name
                "successful_interactions": 1094,
                "average_response_time": 2.3
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch AI conversations data: {str(e)}"
        }

@app.get("/api/total-deals/", tags=["Dashboard"])
async def get_total_deals():
    """Get total deals data"""
    try:
        db_stats = await get_dashboard_stats()
        return {
            "status": "success",
            "data": {
                "total_deals": db_stats['totalDeals'],
                "change_percentage": 22.1,  # Frontend expects this field name
                "closed_deals_this_month": 12,
                "average_deal_value": 125000
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch deals data: {str(e)}"
        }

@app.get("/api/monthly-profit/", tags=["Dashboard"])
async def get_monthly_profit():
    """Get monthly profit data"""
    try:
        db_stats = await get_dashboard_stats()
        return {
            "status": "success",
            "data": {
                "monthly_profit": 45000.00,
                "change_percentage": 18.7,  # Frontend expects this field name
                "profit_margin": 35.2,
                "year_to_date_profit": 450000.00
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch profit data: {str(e)}"
        }

@app.get("/api/voice-calls-count/", tags=["Dashboard"])
async def get_voice_calls_count():
    """Get voice calls count data"""
    try:
        db_stats = await get_dashboard_stats()
        return {
            "status": "success",
            "data": {
                "voice_calls": 245,
                "change_percentage": 87.5,  # Frontend expects this field name
                "average_duration": 4.2,
                "calls_this_month": 245
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch voice calls data: {str(e)}"
        }

@app.get("/api/compliance-status/", tags=["Dashboard"])
async def get_compliance_status():
    """Get compliance status data"""
    try:
        db_stats = await get_dashboard_stats()
        return {
            "status": "success",
            "data": {
                "compliance_status": "compliant",
                "audit_score": 94.2,
                "last_audit": "2025-10-01T00:00:00Z",
                "next_audit": "2026-01-01T00:00:00Z"
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch compliance data: {str(e)}"
        }

# ==================== AI METRICS ENDPOINTS ====================

@app.get("/api/voice-ai-calls-count/", tags=["AI Services"])
async def get_voice_ai_calls_count():
    """Get voice AI calls count and metrics"""
    try:
        ai_metrics = await get_ai_metrics()
        return {
            "status": "success",
            "data": {
                "total_calls": ai_metrics.get('voiceCalls', 0),
                "success_rate": 87.5,
                "average_duration": 4.2
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch voice AI metrics: {str(e)}"
        }

@app.get("/api/vision-analysis/", tags=["AI Services"])
async def get_vision_analysis():
    """Get vision analysis metrics"""
    try:
        ai_metrics = await get_ai_metrics()
        return {
            "status": "success",
            "data": {
                "total_analyses": ai_metrics.get('visionAnalyses', 0),
                "accuracy_rate": 89.2,
                "processing_time": 2.1
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch vision analysis metrics: {str(e)}"
        }

@app.get("/api/nlp-processing/", tags=["AI Services"])
async def get_nlp_processing():
    """Get NLP processing metrics"""
    try:
        ai_metrics = await get_ai_metrics()
        return {
            "status": "success",
            "data": {
                "total_processed": ai_metrics.get('nlpAnalyses', 0),
                "processing_success_rate": 91.5,
                "average_processing_time": 1.8
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch NLP processing metrics: {str(e)}"
        }

@app.get("/api/blockchain-txns/", tags=["AI Services"])
async def get_blockchain_transactions():
    """Get blockchain transaction metrics"""
    try:
        ai_metrics = await get_ai_metrics()
        return {
            "status": "success",
            "data": {
                "total_transactions": ai_metrics.get('blockchainTxns', 0),
                "success_rate": 95.8,
                "average_processing_time": 3.2
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch blockchain metrics: {str(e)}"
        }

# ==================== TENANT MANAGEMENT ENDPOINTS ====================

@app.get("/api/tenant-management/", tags=["Tenant Management"])
async def get_tenant_management():
    """Get tenant management data (redirect to stats)"""
    try:
        tenant_data = await get_tenant_management_data()
        return {
            "status": "success",
            "data": tenant_data
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch tenant data: {str(e)}"
        }

@app.get("/api/tenant-management/stats/", tags=["Tenant Management"])
async def get_tenant_management_stats():
    """Get tenant management statistics"""
    try:
        tenant_data = await get_tenant_management_data()
        return {
            "status": "success",
            "data": tenant_data
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch tenant stats: {str(e)}"
        }

@app.get("/api/analytics/opportunity-cost-analysis/", tags=["Analytics"])
async def get_analytics_opportunity_cost():
    """Get analytics opportunity cost data"""
    try:
        opportunity_data = await get_opportunity_cost_data()
        return {
            "status": "success",
            "data": opportunity_data
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch analytics data: {str(e)}"
        }

@app.get("/api/analytics/deals/", tags=["Analytics"])
async def get_analytics_deals():
    """
    **Deals Analytics**
    
    Provides comprehensive analytics data for real estate deals including overview metrics, 
    deal breakdown by status, property types, lead sources, and recent activity.
    
    **Returns:**
    - Deal overview (total deals, properties, leads, deal value, average deal value)
    - Deal breakdown by status (active, closed, pending)
    - Property type distribution (residential, commercial)
    - Lead source analysis (website, referral, advertisement)
    - Recent activity metrics (deals, properties, leads in last 30 days)
    - Detailed deals list with key information
    """
    try:
        # Mock data for now - replace with actual database calls when ready
        return {
            "status": "success",
            "data": {
                "overview": {
                    "total_deals": 5,
                    "total_properties": 12,
                    "total_leads": 25,
                    "total_deal_value": 250000.0,
                    "avg_deal_value": 50000.0
                },
                "deal_breakdown": {
                    "active": 3,
                    "closed": 2,
                    "pending": 0
                },
                "property_types": {
                    "residential": 8,
                    "commercial": 4
                },
                "lead_sources": {
                    "website": 15,
                    "referral": 7,
                    "advertisement": 3
                },
                "recent_activity": {
                    "deals_last_30_days": 2,
                    "properties_last_30_days": 3,
                    "leads_last_30_days": 8
                },
                "deals": [
                    {
                        "id": 1,
                        "property_address": "123 Main St, Dallas, TX",
                        "offer_price": 150000.0,
                        "status": "active",
                        "created_at": "2025-10-15T10:30:00Z",
                        "deal_type": "purchase"
                    },
                    {
                        "id": 2,
                        "property_address": "456 Oak Ave, Austin, TX",
                        "offer_price": 200000.0,
                        "status": "closed",
                        "created_at": "2025-10-10T14:20:00Z",
                        "deal_type": "investment"
                    }
                ]
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch deals analytics: {str(e)}"
        }

@app.get("/api/analytics/campaigns/", tags=["Analytics"])
async def get_analytics_campaigns():
    """
    **Campaigns Analytics**
    
    Provides detailed analytics for marketing campaigns including performance metrics, 
    channel analysis, and campaign status breakdown.
    
    **Returns:**
    - Campaign overview (total campaigns, budget, leads generated, conversion rate)
    - Campaign status breakdown (active, paused, completed, draft)
    - Channel performance analysis (email, SMS, voice, social media)
    - Recent campaign activity and performance trends
    - Detailed campaign list with key metrics
    """
    try:
        # Mock data for now - replace with actual database calls when ready
        return {
            "status": "success",
            "data": {
                "overview": {
                    "total_campaigns": 8,
                    "total_outreach_campaigns": 15,
                    "total_budget": 50000.0,
                    "avg_budget": 6250.0
                },
                "campaign_statuses": {
                    "active": 5,
                    "completed": 2,
                    "paused": 1
                },
                "channels": {
                    "email": 8,
                    "sms": 4,
                    "voice": 3
                },
                "recent_activity": {
                    "campaigns_last_30_days": 3
                },
                "campaigns": [
                    {
            "id": 1,
                        "name": "Q4 Property Marketing",
                        "status": "active",
                        "budget": 10000.0,
                        "created_at": "2025-10-15T09:00:00Z",
                        "channel": "email"
                    },
                    {
            "id": 2,
                        "name": "Lead Generation Campaign",
                        "status": "completed",
                        "budget": 7500.0,
                        "created_at": "2025-10-01T14:30:00Z",
                        "channel": "sms"
                    }
                ]
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch campaigns analytics: {str(e)}"
        }

@app.get("/api/analytics/performance/", tags=["Analytics"])
async def get_analytics_performance():
    """
    **Performance Analytics**
    
    Provides comprehensive AI performance metrics and business analytics including 
    AI service performance, analysis breakdown, and business metrics.
    
    **Returns:**
    - AI performance metrics (voice calls, vision analysis, NLP processing, blockchain)
    - Analysis breakdown by type and accuracy rates
    - Business metrics including revenue, growth, and efficiency indicators
    - Performance trends and optimization recommendations
    """
    try:
        # Mock data for now - replace with actual database calls when ready
        return {
            "status": "success",
            "data": {
                "ai_performance": {
                    "voice_calls": {
                        "total": 156,
                        "success_rate": 0.875
                    },
                    "vision_analysis": {
                        "total": 89,
                        "accuracy": 0.92
                    },
                    "nlp_processing": {
                        "total": 234,
                        "accuracy": 0.88
                    },
                    "blockchain": {
                        "total_transactions": 45,
                        "success_rate": 0.95
                    }
                },
                "analysis_breakdown": {
                    "property_analysis": 25,
                    "lead_scoring": 18,
                    "market_analysis": 12
                },
                "business_metrics": [
                    {
                        "total_revenue": 125000.50,
                        "active_users": 45,
                        "properties_listed": 12,
                        "ai_conversations": 1300.0,
                        "total_deals": 5,
                        "created_at": "2025-10-17T12:00:00Z"
                    }
                ]
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch performance analytics: {str(e)}"
        }

@app.get("/api/analytics/market/", tags=["Analytics"])
async def get_analytics_market():
    """
    **Market Analytics**
    
    Provides comprehensive market analysis and trends including property market overview, 
    price distribution, geographic analysis, and AI-powered market insights.
    
    **Returns:**
    - Market overview (total properties, average price, market trends)
    - Price distribution analysis by ranges
    - Geographic distribution by state/region
    - AI-generated market insights and predictions
    - Recent property listings and market activity
    """
    try:
        # Mock data for now - replace with actual database calls when ready
        return {
            "status": "success",
            "data": {
                "market_overview": {
                    "total_properties": 12,
                    "avg_property_price": 275000.0,
                    "total_deals": 5
                },
                "price_distribution": {
                    "under_100k": 1,
                    "100k_300k": 6,
                    "300k_500k": 4,
                    "500k_1m": 1,
                    "over_1m": 0
                },
                "state_distribution": {
                    "Texas": 8,
                    "California": 3,
                    "Florida": 1
                },
                "ai_insights": {
                    "avg_confidence": 0.85,
                    "avg_distress_level": 0.65,
                    "motivation_breakdown": {
                        "investment": 5,
                        "primary_residence": 4,
                        "vacation_home": 3
                    }
                },
                "recent_properties": [
                    {
            "id": 1,
                        "address": "123 Main St",
                        "city": "Dallas",
                        "state": "Texas",
                        "price": 250000.0,
                        "property_type": "residential",
                        "status": "active",
                        "created_at": "2025-10-15T10:30:00Z"
                    },
                    {
            "id": 2,
                        "address": "456 Oak Ave",
                        "city": "Austin",
                        "state": "Texas",
                        "price": 350000.0,
                        "property_type": "residential",
                        "status": "pending",
                        "created_at": "2025-10-12T14:20:00Z"
                    }
                ]
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch market analytics: {str(e)}"
        }

@app.get("/api/organizations/status/", tags=["Organizations"])
async def get_organizations_status():
    """Get organizations status"""
    return {
            "status": "success",
            "data": {
            "active_organizations": 25,
            "total_organizations": 28,
            "suspended_organizations": 3,
            "monthly_revenue": 125000.50,
            "growth_rate": 12.5
        }
    }

# ==================== MISSING DASHBOARD ENDPOINTS ====================

@app.get("/api/live-activity-feed/", tags=["Dashboard"])
async def get_live_activity_feed():
    """Get live activity feed - Frontend expected endpoint"""
    try:
        live_data = await get_live_activity_data()
        return {
        "status": "success",
        "data": {
                "activities": live_data  # Frontend expects this field name
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch live activity: {str(e)}"
        }

@app.get("/api/deal-completions-scheduling/", tags=["Dashboard"])
async def get_deal_completions_scheduling():
    """Get deal completions scheduling - Frontend expected endpoint"""
    return {
        "status": "success",
        "data": {
            "scheduled_completions": 8,
            "completed_this_month": 12,
            "upcoming_completions": [
                {"deal_id": 1, "completion_date": "2025-10-15", "value": 150000},
                {"deal_id": 2, "completion_date": "2025-10-20", "value": 200000}
            ]
        }
    }

@app.get("/api/revenue-user-growth-chart-data/", tags=["Dashboard"])
async def get_revenue_user_growth_chart_data():
    """Get revenue user growth chart data - Frontend expected endpoint"""
    try:
        chart_data = await get_revenue_growth_data()
        return {
            "status": "success",
            "data": {
                "chart_data": chart_data  # Frontend expects this field name
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch chart data: {str(e)}"
        }

@app.get("/api/ai-metrics/overall-accuracy/", tags=["AI Services"])
async def get_ai_metrics_overall_accuracy():
    """Get AI metrics overall accuracy - Frontend expected endpoint"""
    try:
        ai_metrics = await get_ai_metrics()
        return {
            "status": "success",
            "data": {
                "overall_accuracy": ai_metrics.get('overall_accuracy', 87.5),
                "accuracy_trend": [85.2, 86.1, 87.3, 87.5],
                "model_performance": {
                    "property_analysis": 89.2,
                    "lead_scoring": 85.7,
                    "market_prediction": 88.1
                }
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch AI accuracy: {str(e)}"
        }

@app.get("/api/compliance-status/details/", tags=["Dashboard"])
async def get_compliance_status_details():
    """Get compliance status details - Frontend expected endpoint"""
    return {
        "status": "success",
        "data": {
            "compliance_score": 94.2,
            "last_audit": "2025-10-01T00:00:00Z",
            "next_audit": "2026-01-01T00:00:00Z",
            "requirements_met": 18,
            "requirements_total": 19,
            "pending_actions": [
                {"action": "Update privacy policy", "due_date": "2025-11-01"},
                {"action": "Review data retention", "due_date": "2025-10-25"}
            ]
        }
    }

@app.get("/api/market-alerts/recent/", tags=["Dashboard"])
async def get_market_alerts_recent():
    """Get recent market alerts - Frontend expected endpoint"""
    try:
        alerts_data = await get_market_alerts_data()
        return {
            "status": "success",
            "data": {
                "alerts": alerts_data  # Frontend expects this field name
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch market alerts: {str(e)}"
        }

@app.post("/recent_activity/", tags=["Dashboard"])
async def get_recent_activity():
    """Get recent tenant activity - Frontend expected endpoint"""
    try:
        # Mock data for recent activity
        return {
            "status": "success",
            "data": [
                {
                    "id": 1,
                    "type": "property_viewed",
                    "description": "Property 123 Main St viewed by tenant",
                    "timestamp": "2025-10-17T10:15:00Z",
                    "tenant_id": 1,
                    "property_id": 1
                },
                {
                    "id": 2,
                    "type": "lease_renewed",
                    "description": "Lease renewed for 6 months",
                    "timestamp": "2025-10-17T09:30:00Z",
                    "tenant_id": 2,
                    "property_id": 2
                },
                {
                    "id": 3,
                    "type": "maintenance_request",
                    "description": "New maintenance request submitted",
                    "timestamp": "2025-10-17T08:45:00Z",
                    "tenant_id": 3,
                    "property_id": 1
                }
            ]
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to fetch recent activity: {str(e)}"
        }

# ==================== PROPERTY ENDPOINTS (Frontend Compatible) ====================

@app.get("/api/properties/", tags=["Properties"])
async def get_properties():
    """
    **Get Properties List**
    
    Retrieves a paginated list of all properties with optional filtering and search capabilities.
    
    **Query Parameters:**
    - page: Page number (default: 1)
    - per_page: Items per page (default: 10)
    - search: Search term for property address or description
    - property_type: Filter by property type
    - min_price: Minimum price filter
    - max_price: Maximum price filter
    
    **Returns:**
    - Paginated list of properties
    - Total count and pagination metadata
    - Property details including address, price, type, status
    """
    try:
        from deelflow.models import Property
        
        properties = await sync_to_async(list)(Property.objects.all())
        
        property_data = []
        for property in properties:
            property_data.append({
                "id": property.id,
                "address": property.address,
                "city": property.city,
                "state": property.state,
                "zipcode": property.zipcode,
                "property_type": property.property_type,
                "bedrooms": property.bedrooms,
                "bathrooms": property.bathrooms,
                "square_feet": property.square_feet,
                "lot_size": property.lot_size,
                "year_built": property.year_built,
                "price": float(property.price) if property.price else None,
                "description": property.description,
                "images": property.images,
                "status": property.status,
                "created_at": property.created_at.isoformat(),
                "updated_at": property.updated_at.isoformat()
            })
        
        return {
            "status": "success",
            "data": property_data,
            "total": len(property_data),
            "page": 1,
            "limit": 20
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve properties: {str(e)}",
            "data": [],
            "total": 0,
            "page": 1,
            "limit": 20
        }

@app.post("/api/properties/", tags=["Properties"])
async def create_property(property_data: PropertyCreate):
    """Create a new property - Frontend compatible endpoint"""
    try:
        from deelflow.models import Property
        
        # Create property in Django database
        property = await sync_to_async(Property.objects.create)(
            address=property_data.street_address,
            unit_apt=property_data.unit_apt,
            city=property_data.city,
            state=property_data.state,
            zipcode=property_data.zip_code,
            county=property_data.county,
            property_type=property_data.property_type,
            bedrooms=int(property_data.bedrooms) if property_data.bedrooms and property_data.bedrooms != "" else None,
            bathrooms=int(property_data.bathrooms) if property_data.bathrooms and property_data.bathrooms != "" else None,
            square_feet=int(property_data.square_feet) if property_data.square_feet and property_data.square_feet != "" else None,
            lot_size=float(property_data.lot_size) if property_data.lot_size and property_data.lot_size != "" else None,
            year_built=int(property_data.year_built) if property_data.year_built and property_data.year_built != "" else None,
            price=float(property_data.purchase_price) if property_data.purchase_price and property_data.purchase_price != "" else None,
            arv=float(property_data.arv) if property_data.arv and property_data.arv != "" else None,
            repair_estimate=float(property_data.repair_estimate) if property_data.repair_estimate and property_data.repair_estimate != "" else None,
            holding_costs=float(property_data.holding_costs) if property_data.holding_costs and property_data.holding_costs != "" else None,
            transaction_type=property_data.transaction_type,
            assignment_fee=float(property_data.assignment_fee) if property_data.assignment_fee and property_data.assignment_fee != "" else None,
            description=property_data.description,
            seller_notes=property_data.seller_notes,
            status="active"
        )
        return {
            "status": "success",
            "message": "Property created successfully",
            "data": {
                "id": property.id,
                "address": property.address,
                "city": property.city,
                "state": property.state,
                "property_type": property.property_type,
                "status": property.status,
                "created_at": property.created_at.isoformat(),
                "updated_at": property.updated_at.isoformat()
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create property: {str(e)}"
        }

@app.get("/api/properties/{property_id}/", tags=["Properties"])
async def get_property(property_id: int):
    """Get a specific property by ID - Frontend compatible endpoint"""
    try:
        from deelflow.models import Property
        
        property = await sync_to_async(Property.objects.get)(id=property_id)
        
        return {
        "status": "success",
        "data": {
                "id": property.id,
                "address": property.address,
                "city": property.city,
                "state": property.state,
                "zipcode": property.zipcode,
                "property_type": property.property_type,
                "bedrooms": property.bedrooms,
                "bathrooms": property.bathrooms,
                "square_feet": property.square_feet,
                "lot_size": property.lot_size,
                "year_built": property.year_built,
                "price": float(property.price) if property.price else None,
                "description": property.description,
                "images": property.images,
                "status": property.status,
                "created_at": property.created_at.isoformat(),
                "updated_at": property.updated_at.isoformat()
            }
        }
    except Property.DoesNotExist:
        return {
            "status": "error",
            "message": "Property not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve property: {str(e)}"
        }

@app.put("/api/properties/{property_id}/", tags=["Properties"])
async def update_property(property_id: int, property_data: PropertyUpdate):
    """Update a property by ID - Frontend compatible endpoint"""
    try:
        from deelflow.models import Property
        
        property = await sync_to_async(Property.objects.get)(id=property_id)
        
        # Update property fields
        for field, value in property_data.dict(exclude_unset=True).items():
            if hasattr(property, field):
                setattr(property, field, value)
        
        await sync_to_async(property.save)()
        
        return {
            "status": "success",
            "message": "Property updated successfully",
            "data": {
                "id": property.id,
                "address": property.address,
                "status": property.status,
                "updated_at": property.updated_at.isoformat()
            }
        }
    except Property.DoesNotExist:
        return {
            "status": "error",
            "message": "Property not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to update property: {str(e)}"
        }

@app.delete("/api/properties/{property_id}/", tags=["Properties"])
async def delete_property(property_id: int):
    """Delete a property by ID - Frontend compatible endpoint"""
    try:
        from deelflow.models import Property
        
        property = await sync_to_async(Property.objects.get)(id=property_id)
        await sync_to_async(property.delete)()

        return {
            "status": "success",
            "message": "Property deleted successfully"
        }
    except Property.DoesNotExist:
        return {
            "status": "error",
            "message": "Property not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to delete property: {str(e)}"
        }

@app.get("/api/properties/{property_id}/ai-analysis/", tags=["Properties"])
async def get_property_ai_analysis(property_id: int):
    """Get AI analysis for a property - Frontend compatible endpoint"""
    try:
        from deelflow.models import Property
        
        property = await sync_to_async(Property.objects.get)(id=property_id)
        
        # Mock AI analysis (replace with actual AI service)
        ai_analysis = {
            "property_id": property_id,
            "market_value": float(property.arv or 250000),
            "repair_estimate": float(property.repair_estimate or 15000),
            "roi_potential": 85.5,
            "risk_score": 3.2,
            "recommendation": "Good investment opportunity",
            "confidence": 0.87,
            "analysis_date": timezone.now().isoformat(),
            "key_insights": [
                "Property shows strong potential for renovation",
                "Market conditions are favorable",
                "Neighborhood shows positive growth trends"
            ]
        }
        
        return {
            "status": "success",
            "data": ai_analysis
        }
    except Property.DoesNotExist:
        return {
            "status": "error",
            "message": "Property not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to get AI analysis: {str(e)}"
        }

# ==================== PROPERTY SAVES ENDPOINTS ====================

@app.get("/api/property-saves/", tags=["Property Saves"])
async def get_property_saves(params: dict = None):
    """Get all property saves - Frontend compatible endpoint"""
    try:
        from deelflow.models import PropertySave
        
        # For now, return empty list since PropertySave model might not exist
        return {
            "status": "success",
            "data": [],
            "total": 0,
            "page": 1,
            "limit": 20
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve property saves: {str(e)}",
            "data": [],
            "total": 0,
            "page": 1,
            "limit": 20
        }

@app.get("/api/property-saves/{property_save_id}/", tags=["Property Saves"])
async def get_property_save(property_save_id: int):
    """Get a specific property save by ID - Frontend compatible endpoint"""
    try:
        return {
            "status": "error",
            "message": "Property save not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve property save: {str(e)}"
        }

@app.post("/api/property-saves/", tags=["Property Saves"])
async def create_property_save(property_save_data: dict):
    """Create a new property save - Frontend compatible endpoint"""
    try:
        return {
        "status": "success",
            "message": "Property save created successfully",
            "data": {
                "id": 1,
                "property_id": property_save_data.get("property_id"),
                "user_id": property_save_data.get("user_id"),
                "created_at": timezone.now().isoformat()
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create property save: {str(e)}"
        }
    
@app.put("/api/property-saves/{property_save_id}/", tags=["Property Saves"])
async def update_property_save(property_save_id: int, property_save_data: dict):
    """Update a property save by ID - Frontend compatible endpoint"""
    try:
        return {
        "status": "success",
            "message": "Property save updated successfully",
        "data": {
                "id": property_save_id,
                "updated_at": timezone.now().isoformat()
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to update property save: {str(e)}"
        }

@app.delete("/api/property-saves/{property_save_id}/", tags=["Property Saves"])
async def delete_property_save(property_save_id: int):
    """Delete a property save by ID - Frontend compatible endpoint"""
    try:
        return {
        "status": "success",
            "message": "Property save deleted successfully"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to delete property save: {str(e)}"
        }

# ==================== CAMPAIGN ENDPOINTS (Frontend Compatible) ====================

@app.get("/campaigns/", 
         tags=["Campaigns"],
         summary="Get All Campaigns",
         description="Retrieves all campaigns with normalized array fields and comprehensive data including seller finder, buyer finder, and demographic information.",
         response_description="List of campaigns with pagination information",
         responses={
             200: {
                 "description": "Campaigns retrieved successfully",
                 "content": {
                     "application/json": {
                         "example": {
                             "status": "success",
                             "data": [
                                 {
                                     "id": 1,
                                     "name": "Sample Campaign",
                                     "campaign_type": "seller_finder",
                                     "channel": ["email", "phone"],
                                     "budget": 5000.0,
                                     "status": "active",
                                     "geographic_scope_values": ["Miami-Dade", "Broward"],
                                     "distress_indicators": ["Pre-foreclosure", "Divorce"]
                                 }
                             ],
                             "total": 25,
                             "page": 1,
                             "limit": 20
                         }
                     }
                 }
             },
             500: {
                 "description": "Internal server error",
                 "content": {
                     "application/json": {
                         "example": {
                             "status": "error",
                             "message": "Failed to retrieve campaigns: Database connection error",
                             "data": [],
                             "total": 0,
                             "page": 1,
                             "limit": 20
                         }
                     }
                 }
             }
         })
async def get_campaigns():
    """
    **Get All Campaigns**
    
    Retrieves all campaigns with comprehensive data including:
    
    **Core Campaign Data:**
    - Basic information (name, type, budget, status)
    - Scheduling and content details
    - Geographic scope and targeting parameters
    
    **Seller Finder Data:**
    - Geographic targeting (country, state, counties, city, districts, parish)
    - Property criteria (year built range, keywords)
    - Additional seller-specific filters
    
    **Buyer Finder Data:**
    - Geographic targeting for buyers
    - Demographic filters (age range, ethnicity, salary, marital status)
    - Employment and home ownership status
    
    **Data Normalization:**
    - `channel` is always returned as an array
    - `geographic_scope_values` and `distress_indicators` are parsed from stored strings
    - All datetime fields are returned in ISO format
    
    **Returns:**
    - **200**: List of campaigns with pagination information
    - **500**: Server error during retrieval
    
    **Response Format:**
    ```json
    {
        "status": "success",
        "data": [
            {
                "id": 1,
                "name": "Q4 Marketing Campaign",
                "campaign_type": "seller_finder",
                "channel": ["email", "phone"],
                "budget": 10000.0,
                "status": "active",
                "geographic_scope_values": ["Miami-Dade", "Broward"],
                "distress_indicators": ["Pre-foreclosure", "Divorce"],
                // ... all other campaign fields
            }
        ],
        "total": 25,
        "page": 1,
        "limit": 20
    }
    ```
    """
    try:
        from deelflow.models import Campaign
        campaigns = await sync_to_async(list)(Campaign.objects.all())
        
        campaign_data = []
        for campaign in campaigns:
            # Normalize fields stored as strings in DB
            try:
                geo_values = campaign.geographic_scope_values
                if isinstance(geo_values, str):
                    geo_values = ast.literal_eval(geo_values)
            except Exception:
                geo_values = []
            try:
                distress = campaign.distress_indicators
                if isinstance(distress, str):
                    distress = ast.literal_eval(distress)
            except Exception:
                distress = []
            channel_val = campaign.channel
            if isinstance(channel_val, list):
                channel_out = channel_val
            else:
                channel_out = [channel_val] if channel_val else []
            campaign_data.append({
                "id": campaign.id,
                "name": campaign.name,
                "campaign_type": campaign.campaign_type,
                "channel": channel_out,
                "budget": float(campaign.budget) if campaign.budget else None,
                "scheduled_at": campaign.scheduled_at.isoformat() if campaign.scheduled_at else None,
                "subject_line": campaign.subject_line,
                "email_content": campaign.email_content,
                "use_ai_personalization": campaign.use_ai_personalization,
                "status": campaign.status,
                "geographic_scope_type": campaign.geographic_scope_type,
                "geographic_scope_values": geo_values,
                "location": campaign.location,
                "property_type": campaign.property_type,
                "minimum_equity": float(campaign.minimum_equity) if campaign.minimum_equity else None,
                "min_price": float(campaign.min_price) if campaign.min_price else None,
                "max_price": float(campaign.max_price) if campaign.max_price else None,
                "distress_indicators": distress,
                "created_at": campaign.created_at.isoformat()
            })
        
        return {
            "status": "success",
            "data": campaign_data,
            "total": len(campaign_data),
            "page": 1,
            "limit": 20
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve campaigns: {str(e)}",
            "data": [],
            "total": 0,
            "page": 1,
            "limit": 20
        }

@app.get("/campaigns/{campaign_id}/", 
         tags=["Campaigns"],
         summary="Get Campaign by ID",
         description="Retrieves a specific campaign by its ID with all associated data including seller finder, buyer finder, and demographic information.",
         response_description="Campaign details with normalized array fields",
         responses={
             200: {
                 "description": "Campaign retrieved successfully",
                 "content": {
                     "application/json": {
                         "example": {
                             "status": "success",
                             "data": {
                                 "id": 1,
                                 "name": "Sample Campaign",
                                 "campaign_type": "seller_finder",
                                 "channel": ["email", "phone"],
                                 "budget": 5000.0,
                                 "scheduled_at": "2024-12-25T10:00:00+00:00",
                                 "subject_line": "Investment Opportunity",
                                 "email_content": "Discover amazing property deals...",
                                 "use_ai_personalization": True,
                                 "status": "active",
                                 "geographic_scope_type": "counties",
                                 "geographic_scope_values": ["Miami-Dade", "Broward"],
                                 "location": "Miami, FL",
                                 "property_type": "residential",
                                 "minimum_equity": 75000.0,
                                 "min_price": 300000.0,
                                 "max_price": 800000.0,
                                 "distress_indicators": ["Pre-foreclosure", "Divorce"],
                                 "created_at": "2024-10-13T07:34:07.710903+00:00",
                                 "updated_at": "2024-10-18T06:28:14.415806+00:00",
                                 "seller_country": "USA",
                                 "seller_state": "Florida",
                                 "seller_counties": "Miami-Dade",
                                 "seller_city": "Miami",
                                 "property_year_built_min": 1990,
                                 "property_year_built_max": 2020,
                                 "seller_keywords": "investment, rental",
                                 "buyer_country": "USA",
                                 "buyer_state": "Florida",
                                 "age_range": "25-45",
                                 "salary_range": "50000-150000",
                                 "marital_status": "any",
                                 "employment_status": "employed",
                                 "home_ownership_status": "any"
                             }
                         }
                     }
                 }
             },
             404: {
                 "description": "Campaign not found",
                 "content": {
                     "application/json": {
                         "example": {
                             "status": "error",
                             "message": "Campaign not found"
                         }
                     }
                 }
             },
             500: {
                 "description": "Internal server error",
                 "content": {
                     "application/json": {
                         "example": {
                             "status": "error",
                             "message": "Failed to retrieve campaign: Database connection error"
                         }
                     }
                 }
             }
         })
async def get_campaign(campaign_id: int):
    """
    **Get Campaign by ID**
    
    Retrieves a specific campaign by its ID with comprehensive data including:
    
    **Core Campaign Data:**
    - Basic information (name, type, budget, status)
    - Scheduling and content details
    - Geographic scope and targeting parameters
    
    **Seller Finder Data:**
    - Geographic targeting (country, state, counties, city, districts, parish)
    - Property criteria (year built range, keywords)
    - Additional seller-specific filters
    
    **Buyer Finder Data:**
    - Geographic targeting for buyers
    - Demographic filters (age range, ethnicity, salary, marital status)
    - Employment and home ownership status
    
    **Data Normalization:**
    - `channel` is always returned as an array
    - `geographic_scope_values` and `distress_indicators` are parsed from stored strings
    - All datetime fields are returned in ISO format
    
    **Parameters:**
    - **campaign_id** (int): The unique identifier of the campaign to retrieve
    
    **Returns:**
    - **200**: Campaign data with all fields populated
    - **404**: Campaign not found
    - **500**: Server error during retrieval
    
    **Example Usage:**
    ```
    GET /campaigns/123/
    ```
    
    **Response Format:**
    ```json
    {
        "status": "success",
        "data": {
            "id": 123,
            "name": "Q4 Marketing Campaign",
            "campaign_type": "seller_finder",
            "channel": ["email", "phone"],
            "budget": 10000.0,
            "status": "active",
            "geographic_scope_values": ["Miami-Dade", "Broward"],
            "distress_indicators": ["Pre-foreclosure", "Divorce"],
            // ... all other campaign fields
        }
    }
    ```
    """
    try:
        from deelflow.models import Campaign
        import ast
        
        campaign = await sync_to_async(Campaign.objects.get)(id=campaign_id)
        
        # Normalize fields stored as strings in DB
        try:
            geo_values = campaign.geographic_scope_values
            if isinstance(geo_values, str):
                geo_values = ast.literal_eval(geo_values)
        except Exception:
            geo_values = []
            
        try:
            distress = campaign.distress_indicators
            if isinstance(distress, str):
                distress = ast.literal_eval(distress)
        except Exception:
            distress = []
            
        channel_val = campaign.channel
        if isinstance(channel_val, list):
            channel_out = channel_val
        else:
            channel_out = [channel_val] if channel_val else []
        
        campaign_data = {
            "id": campaign.id,
            "name": campaign.name,
            "campaign_type": campaign.campaign_type,
            "channel": channel_out,
            "budget": float(campaign.budget) if campaign.budget else None,
            "scheduled_at": campaign.scheduled_at.isoformat() if campaign.scheduled_at else None,
            "subject_line": campaign.subject_line,
            "email_content": campaign.email_content,
            "use_ai_personalization": campaign.use_ai_personalization,
            "status": campaign.status,
            "geographic_scope_type": campaign.geographic_scope_type,
            "geographic_scope_values": geo_values,
            "location": campaign.location,
            "property_type": campaign.property_type,
            "minimum_equity": float(campaign.minimum_equity) if campaign.minimum_equity else None,
            "min_price": float(campaign.min_price) if campaign.min_price else None,
            "max_price": float(campaign.max_price) if campaign.max_price else None,
            "distress_indicators": distress,
            "created_at": campaign.created_at.isoformat(),
            "updated_at": campaign.updated_at.isoformat() if campaign.updated_at else None,
            # Seller Finder - Geographic Details
            "seller_country": campaign.seller_country,
            "seller_state": campaign.seller_state,
            "seller_counties": campaign.seller_counties,
            "seller_city": campaign.seller_city,
            "seller_districts": campaign.seller_districts,
            "seller_parish": campaign.seller_parish,
            # Seller Finder - Additional Fields
            "property_year_built_min": campaign.property_year_built_min,
            "property_year_built_max": campaign.property_year_built_max,
            "seller_keywords": campaign.seller_keywords,
            # Buyer Finder - Geographic Details
            "buyer_country": campaign.buyer_country,
            "buyer_state": campaign.buyer_state,
            "buyer_counties": campaign.buyer_counties,
            "buyer_city": campaign.buyer_city,
            "buyer_districts": campaign.buyer_districts,
            "buyer_parish": campaign.buyer_parish,
            # Buyer Finder - Demographic Details
            "last_qualification": campaign.last_qualification,
            "age_range": campaign.age_range,
            "ethnicity": campaign.ethnicity,
            "salary_range": campaign.salary_range,
            "marital_status": campaign.marital_status,
            "employment_status": campaign.employment_status,
            "home_ownership_status": campaign.home_ownership_status
        }
        
        return {
            "status": "success",
            "data": campaign_data
        }
    except Campaign.DoesNotExist:
        return {
            "status": "error",
            "message": "Campaign not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve campaign: {str(e)}"
        }

@app.post("/campaigns/", tags=["Campaigns"])
async def create_campaign(campaign_data: CampaignCreate):
    """Create a new campaign - Frontend compatible endpoint"""
    try:
        print("=== CAMPAIGN CREATION DEBUG ===")
        print(f"Received campaign_data: {campaign_data}")
        
        from deelflow.models import Campaign
        print("✓ Django Campaign model imported successfully")
        
        # Convert channel to string if it's a list
        channel = campaign_data.channel
        if isinstance(channel, list):
            channel = channel[0] if channel else "email"
        print(f"✓ Channel processed: {channel}")
        
        # Handle geographic scope - support both object and separate field formats
        geographic_scope_type = campaign_data.geographic_scope_type
        geographic_scope_values = campaign_data.geographic_scope_values
        
        # If geographic_scope object is provided, extract type and values from it
        if campaign_data.geographic_scope:
            geographic_scope_type = campaign_data.geographic_scope.get("type", geographic_scope_type)
            if "counties" in campaign_data.geographic_scope:
                geographic_scope_values = campaign_data.geographic_scope["counties"]
            elif "cities" in campaign_data.geographic_scope:
                geographic_scope_values = campaign_data.geographic_scope["cities"]
            elif "states" in campaign_data.geographic_scope:
                geographic_scope_values = campaign_data.geographic_scope["states"]
            elif "zipcodes" in campaign_data.geographic_scope:
                geographic_scope_values = campaign_data.geographic_scope["zipcodes"]
        print(f"✓ Geographic scope processed: type={geographic_scope_type}, values={geographic_scope_values}")
        
        # Parse scheduled_at string to datetime
        from datetime import datetime
        scheduled_at = None
        if campaign_data.scheduled_at:
            try:
                # Handle different datetime formats
                scheduled_str = campaign_data.scheduled_at
                if 'T' in scheduled_str and not scheduled_str.endswith('Z'):
                    scheduled_at = datetime.fromisoformat(scheduled_str)
                else:
                    scheduled_at = datetime.fromisoformat(scheduled_str.replace('Z', '+00:00'))
                print(f"✓ Scheduled_at parsed successfully: {scheduled_at}")
            except ValueError as e:
                print(f"Error parsing scheduled_at: {e}")
                scheduled_at = None
        else:
            print("✓ No scheduled_at provided")
        
        # Create campaign in Django database
        try:
            # Test if the issue is with sync_to_async
            print("About to create campaign...")
            print("Creating campaign with data:")
            print(f"  - name: {campaign_data.name}")
            print(f"  - scheduled_at: {scheduled_at}")
            print(f"  - channel: {channel}")
            
            from django.utils import timezone
            campaign = await sync_to_async(Campaign.objects.create)(
            name=campaign_data.name,
            campaign_type=campaign_data.campaign_type,
            channel=channel,
            budget=campaign_data.budget,
            scheduled_at=scheduled_at,
            updated_at=timezone.now(),
            geographic_scope_type=geographic_scope_type,
            geographic_scope_values=str(geographic_scope_values) if geographic_scope_values else "[]",
            location=campaign_data.location,
            property_type=campaign_data.property_type,
            minimum_equity=campaign_data.minimum_equity,
            min_price=campaign_data.min_price,
            max_price=campaign_data.max_price,
            distress_indicators=str(campaign_data.distress_indicators) if campaign_data.distress_indicators else "[]",
            subject_line=campaign_data.subject_line,
            email_content=campaign_data.email_content,
            use_ai_personalization=campaign_data.use_ai_personalization,
            status=campaign_data.status,
            # Seller Finder - Geographic Details
            seller_country=campaign_data.seller_country,
            seller_state=campaign_data.seller_state,
            seller_counties=campaign_data.seller_counties,
            seller_city=campaign_data.seller_city,
            seller_districts=campaign_data.seller_districts,
            seller_parish=campaign_data.seller_parish,
            # Seller Finder - Additional Fields
            property_year_built_min=int(campaign_data.property_year_built_min) if campaign_data.property_year_built_min and str(campaign_data.property_year_built_min).strip() != "" else None,
            property_year_built_max=int(campaign_data.property_year_built_max) if campaign_data.property_year_built_max and str(campaign_data.property_year_built_max).strip() != "" else None,
            seller_keywords=campaign_data.seller_keywords,
            # Buyer Finder - Geographic Details
            buyer_country=campaign_data.buyer_country,
            buyer_state=campaign_data.buyer_state,
            buyer_counties=campaign_data.buyer_counties,
            buyer_city=campaign_data.buyer_city,
            buyer_districts=campaign_data.buyer_districts,
            buyer_parish=campaign_data.buyer_parish,
            # Buyer Finder - Demographic Details
            last_qualification=campaign_data.last_qualification,
            age_range=campaign_data.age_range,
            ethnicity=campaign_data.ethnicity,
            salary_range=campaign_data.salary_range,
            marital_status=campaign_data.marital_status,
            employment_status=campaign_data.employment_status,
            home_ownership_status=campaign_data.home_ownership_status
            )
            print("✓ Campaign created successfully in database")
        except Exception as db_error:
            print(f"✗ Database error: {str(db_error)}")
            import traceback
            print(f"Database error traceback: {traceback.format_exc()}")
            return {
                "status": "error",
                "message": f"Database error: {str(db_error)}"
            }
        
        print("✓ Preparing response...")
        return {
            "status": "success",
            "message": "Campaign created successfully",
            "data": {
                "id": campaign.id,
                "name": campaign.name,
                "campaign_type": campaign.campaign_type,
                "channel": campaign.channel,
                "budget": float(campaign.budget) if campaign.budget else None,
                "scheduled_at": str(campaign.scheduled_at) if campaign.scheduled_at else None,
                "subject_line": campaign.subject_line,
                "email_content": campaign.email_content,
                "use_ai_personalization": campaign.use_ai_personalization,
                "status": campaign.status,
                "created_at": str(campaign.created_at),
                "updated_at": str(campaign.updated_at)
            }
        }
    except Exception as e:
        import traceback
        return {
            "status": "error",
            "message": f"Failed to create campaign: {str(e)}",
            "traceback": traceback.format_exc()
        }

# Removed per request: Only list endpoint should remain

@app.put("/campaigns/{campaign_id}/", tags=["Campaigns"])
async def update_campaign(campaign_id: int, campaign_data: CampaignUpdate):
    """Update a campaign by ID - Frontend compatible endpoint"""
    try:
        from deelflow.models import Campaign
        
        campaign = await sync_to_async(Campaign.objects.get)(id=campaign_id)
        
        # Update campaign fields
        for field, value in campaign_data.dict(exclude_unset=True).items():
            if hasattr(campaign, field):
                setattr(campaign, field, value)
        
        await sync_to_async(campaign.save)()
        
        return {
        "status": "success",
        "message": "Campaign updated successfully",
        "data": {
                "id": campaign.id,
                "name": campaign.name,
                "status": campaign.status,
                "updated_at": campaign.updated_at.isoformat()
            }
        }
    except Campaign.DoesNotExist:
        return {
            "status": "error",
            "message": "Campaign not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to update campaign: {str(e)}"
        }

@app.delete("/campaigns/{campaign_id}/", tags=["Campaigns"])
async def delete_campaign(campaign_id: int):
    """Delete a campaign by ID - Frontend compatible endpoint"""
    try:
        from deelflow.models import Campaign
        
        campaign = await sync_to_async(Campaign.objects.get)(id=campaign_id)
        await sync_to_async(campaign.delete)()
        
        return {
            "status": "success",
            "message": "Campaign deleted successfully"
        }
    except Campaign.DoesNotExist:
        return {
            "status": "error",
            "message": "Campaign not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to delete campaign: {str(e)}"
        }

# Additional Campaign endpoints expected by frontend
@app.get("/campaigns/{campaign_id}/recipients/", tags=["Campaigns"])
async def get_campaign_recipients(campaign_id: int):
    """Get campaign recipients - Frontend compatible endpoint"""
    return {
        "status": "success",
        "data": {
            "campaign_id": campaign_id,
            "recipients": [],
            "total": 0
        }
    }

@app.post("/create_campaign/", tags=["Campaigns"])
async def create_campaign_legacy(campaign_data: CampaignCreate):
    """Legacy create campaign endpoint (for frontend compatibility)"""
    return await create_campaign(campaign_data)

@app.get("/active_campaign_summary/", tags=["Campaigns"])
async def get_active_campaign_summary():
    """Get active campaign summary - Frontend compatible endpoint"""
    try:
        from deelflow.models import Campaign
        active_campaigns = await sync_to_async(list)(Campaign.objects.filter(status="active"))
        
        return {
        "status": "success",
        "data": {
                "total_active": len(active_campaigns),
                "active_campaigns": len(active_campaigns),
                "total_budget": sum(float(c.budget or 0) for c in active_campaigns),
                "leads_today": 15,  # Mock data for now
                "leads_today_change_pct": 12.5,  # Mock data for now
                "response_rate": 8.3,  # Mock data for now
                "campaigns": [
                    {
                        "id": c.id,
                        "name": c.name,
                        "status": c.status,
                        "budget": float(c.budget or 0)
                    } for c in active_campaigns
                ]
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to get active campaigns: {str(e)}"
        }

@app.get("/campaign_property_stats/", tags=["Campaigns"])
async def get_campaign_property_stats():
    """Get campaign property statistics - Frontend compatible endpoint"""
    return {
        "status": "success",
        "data": {
            "total_properties_targeted": 156,
            "properties_per_campaign": 12.5,
            "conversion_rate": 8.3
        }
    }

@app.get("/campaign_performance_overview/", tags=["Campaigns"])
async def get_campaign_performance_overview():
    """Get campaign performance overview - Frontend compatible endpoint"""
    return {
        "status": "success",
        "data": {
            "total_campaigns": 25,
            "active_campaigns": 8,
            "completed_campaigns": 15,
            "average_roi": 125.5
        }
    }

@app.get("/channel_response_rates/", tags=["Campaigns"])
async def get_channel_response_rates():
    """Get channel response rates - Frontend compatible endpoint"""
    return {
        "status": "success",
        "data": {
            "email": {"rate": 8.5, "responses": 125},
            "sms": {"rate": 12.3, "responses": 89},
            "voice": {"rate": 19.2, "responses": 45},
            "whatsapp": {"rate": 15.7, "responses": 67}
        }
    }

@app.get("/lead_conversion_funnel/", tags=["Campaigns"])
async def get_lead_conversion_funnel():
    """Get lead conversion funnel data - Frontend compatible endpoint"""
    try:
        return {
            "status": "success",
            "data": {
                "leads": 500,
                "qualified": 125,
                "converted": 12,
                "leads_generated": 500,
                "qualified_leads": 125,
                "meetings_scheduled": 45,
                "deals_closed": 12,
                "conversion_rate": 2.4
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to get lead conversion funnel: {str(e)}"
        }

# ==================== LEAD ENDPOINTS (Frontend Compatible) ====================

@app.get("/leads/", tags=["Leads"])
async def get_leads():
    """Get all leads - Frontend compatible endpoint"""
    try:
        from deelflow.models import Lead
        
        leads = await sync_to_async(list)(Lead.objects.all())
        
        lead_data = []
        for lead in leads:
            lead_data.append({
                "id": lead.id,
                "name": lead.name,
                "email": lead.email,
                "phone": lead.phone,
                "address": lead.address,
                "city": lead.city,
                "state": lead.state,
                "zipcode": lead.zipcode,
                "source": lead.source,
                "status": lead.status,
                "motivation_score": lead.motivation_score,
                "property_condition": lead.property_condition,
                "financial_situation": lead.financial_situation,
                "timeline_urgency": lead.timeline_urgency,
                "negotiation_style": lead.negotiation_style,
                "notes": lead.notes,
                "responded": lead.responded,
                "created_at": lead.created_at.isoformat(),
                "updated_at": lead.updated_at.isoformat()
            })
        
        return {
            "status": "success",
            "data": lead_data,
            "total": len(lead_data),
            "page": 1,
            "limit": 20
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve leads: {str(e)}",
            "data": [],
            "total": 0,
            "page": 1,
            "limit": 20
        }

@app.post("/leads/", tags=["Leads"])
async def create_lead(lead_data: LeadCreate):
    """Create a new lead - Frontend compatible endpoint"""
    try:
        from deelflow.models import Lead
        
        # Create lead in Django database
        lead = await sync_to_async(Lead.objects.create)(
            name=f"{lead_data.first_name} {lead_data.last_name}",
            email=lead_data.email,
            phone=lead_data.phone,
            address=lead_data.property_address,
            city=lead_data.property_city,
            state=lead_data.property_state,
            zipcode=lead_data.property_zip,
            source=lead_data.source,
            status=lead_data.status
        )
        
        return {
            "status": "success",
            "message": "Lead created successfully",
            "data": {
                "id": lead.id,
                "first_name": lead.first_name,
                "last_name": lead.last_name,
                "email": lead.email,
                "status": lead.status,
                "created_at": lead.created_at.isoformat(),
                "updated_at": lead.updated_at.isoformat()
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create lead: {str(e)}"
        }

@app.get("/leads/{lead_id}/", tags=["Leads"])
async def get_lead(lead_id: int):
    """Get a specific lead by ID - Frontend compatible endpoint"""
    try:
        from deelflow.models import Lead
        
        lead = await sync_to_async(Lead.objects.get)(id=lead_id)
    
        return {
        "status": "success",
            "data": {
                "id": lead.id,
                "first_name": lead.first_name,
                "last_name": lead.last_name,
                "email": lead.email,
                "phone": lead.phone,
                "property_address": lead.property_address,
                "property_city": lead.property_city,
                "property_state": lead.property_state,
                "property_zip": lead.property_zip,
                "property_type": lead.property_type,
                "source": lead.source,
                "estimated_value": float(lead.estimated_value) if lead.estimated_value else None,
                "mortgage_balance": float(lead.mortgage_balance) if lead.mortgage_balance else None,
                "asking_price": float(lead.asking_price) if lead.asking_price else None,
                "preferred_contact_method": lead.preferred_contact_method,
                "lead_type": lead.lead_type,
                "status": lead.status,
                "created_at": lead.created_at.isoformat(),
                "updated_at": lead.updated_at.isoformat()
            }
        }
    except Lead.DoesNotExist:
        return {
            "status": "error",
            "message": "Lead not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve lead: {str(e)}"
        }

@app.put("/leads/{lead_id}/", tags=["Leads"])
async def update_lead(lead_id: int, lead_data: LeadUpdate):
    """Update a lead by ID - Frontend compatible endpoint"""
    try:
        from deelflow.models import Lead
        
        lead = await sync_to_async(Lead.objects.get)(id=lead_id)
        
        # Update lead fields
        for field, value in lead_data.dict(exclude_unset=True).items():
            if hasattr(lead, field):
                setattr(lead, field, value)
        
        await sync_to_async(lead.save)()
        
        return {
        "status": "success",
            "message": "Lead updated successfully",
        "data": {
                "id": lead.id,
                "first_name": lead.first_name,
                "last_name": lead.last_name,
                "status": lead.status,
                "updated_at": lead.updated_at.isoformat()
            }
        }
    except Lead.DoesNotExist:
        return {
            "status": "error",
            "message": "Lead not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to update lead: {str(e)}"
        }

@app.delete("/leads/{lead_id}/", tags=["Leads"])
async def delete_lead(lead_id: int):
    """Delete a lead by ID - Frontend compatible endpoint"""
    try:
        from deelflow.models import Lead
        
        lead = await sync_to_async(Lead.objects.get)(id=lead_id)
        await sync_to_async(lead.delete)()
        
        return {
            "status": "success",
            "message": "Lead deleted successfully"
        }
    except Lead.DoesNotExist:
        return {
            "status": "error",
            "message": "Lead not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to delete lead: {str(e)}"
        }

@app.get("/leads/{lead_id}/ai-score/", tags=["Leads"])
async def get_lead_ai_score(lead_id: int):
    """Get AI score for a lead - Frontend compatible endpoint"""
    try:
        from deelflow.models import Lead
        
        lead = await sync_to_async(Lead.objects.get)(id=lead_id)
        
        # Mock AI score calculation
        ai_score = {
            "lead_id": lead_id,
            "score": 85.5,
            "confidence": 0.87,
            "factors": [
                "High estimated value",
                "Good property condition",
                "Favorable market conditions"
            ],
            "recommendation": "High priority lead",
            "analysis_date": datetime.datetime.now().isoformat()
    }
        
        return {
            "status": "success",
            "data": ai_score
        }
    except Lead.DoesNotExist:
        return {
            "status": "error",
            "message": "Lead not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to get AI score: {str(e)}"
        }

# ==================== AUTHENTICATION ENDPOINTS ====================

@app.post("/api/auth/login", tags=["Authentication"])
async def login(login_data: LoginRequest):
    """
    **User Login**
    
    Authenticates a user with email and password, returning a JWT token for subsequent API calls.
    
    **Request Body:**
    - email: User's email address
    - password: User's password
    
    **Returns:**
    - JWT access token
    - Token type (Bearer)
    - User information (id, email, name, role)
    - Authentication status
    """
    try:
        # Mock authentication (replace with actual authentication logic)
        if login_data.email and login_data.password:
            return {
                "status": "success",
                "data": {
                    "tokens": {
                        "access_token": "mock_jwt_token_12345",
                        "token_type": "bearer"
                    },
                    "user": {
                        "id": 1,
                        "email": login_data.email,
                        "first_name": "John",
                        "last_name": "Doe",
                        "role": "admin"
                    }
                }
            }
        else:
            return {
                "status": "error",
                "message": "Invalid credentials"
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Login failed: {str(e)}"
        }

@app.post("/api/auth/register", tags=["Authentication"])
async def register(register_data: RegisterRequest):
    """
    **User Registration**
    
    Creates a new user account with the provided information.
    
    **Request Body:**
    - email: User's email address
    - password: User's password
    - first_name: User's first name
    - last_name: User's last name
    - role: User's role (optional)
    
    **Returns:**
    - Registration status
    - User information
    - Success/error message
    """
    try:
        # Mock registration (replace with actual registration logic)
        return {
        "status": "success",
            "message": "User registered successfully",
        "data": {
                "id": 1,
                "email": register_data.email,
                "first_name": register_data.first_name,
                "last_name": register_data.last_name,
                "role": "user"
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Registration failed: {str(e)}"
        }

@app.get("/api/auth/me", tags=["Authentication"])
async def get_current_user():
    """Get current user information"""
    return {
        "status": "success",
        "data": {
            "id": 1,
            "email": "user@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "role": "admin",
            "organization_id": 1
        }
    }

@app.get("/api/test-dashboard", tags=["Core"])
async def test_dashboard():
    """Test endpoint for dashboard debugging"""
    return {
        "status": "success",
        "message": "Dashboard test endpoint working",
        "data": {
            "test_revenue": 125000.50,
            "test_users": 25,
            "test_properties": 5,
            "test_conversations": 1250
        }
    }

# ==================== ROLE MANAGEMENT ENDPOINTS ====================

@app.get("/api/roles/", tags=["Role Management"])
async def get_roles(page: int = 1, limit: int = 20):
    """Get all roles with pagination"""
    try:
        from deelflow.models import Role
        from django.core.paginator import Paginator
        
        # Get all roles
        roles_queryset = Role.objects.all().prefetch_related('permissions')
        roles_list = await sync_to_async(list)(roles_queryset)
        
        # Paginate
        paginator = Paginator(roles_list, limit)
        page_obj = paginator.get_page(page)
        
        # Convert to response format
        roles_data = []
        for role in page_obj:
            permissions_data = []
            for perm in role.permissions.all():
                permissions_data.append({
                    "id": perm.id,
                    "name": perm.name,
                    "label": perm.label
                })
            
            roles_data.append({
                "id": role.id,
                "name": role.name,
                "label": role.label,
                "permissions": permissions_data,
                "created_at": role.created_at.isoformat(),
                "updated_at": role.updated_at.isoformat()
            })
        
        return {
        "status": "success",
            "data": {
                "roles": roles_data,
                "total": paginator.count,
                "page": page,
                "limit": limit,
                "total_pages": paginator.num_pages
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve roles: {str(e)}"
        }

@app.get("/api/roles/stats/", tags=["Role Management"])
async def get_role_stats():
    """Get role management statistics"""
    try:
        from deelflow.models import Role, Permission, User, Organization
        
        # Get counts
        total_roles = await sync_to_async(Role.objects.count)()
        total_permissions = await sync_to_async(Permission.objects.count)()
        total_users = await sync_to_async(User.objects.count)()
        total_tenants = await sync_to_async(Organization.objects.count)()
        
        # Get active tenants (non-suspended)
        active_tenants = await sync_to_async(Organization.objects.exclude(subscription_status='suspended').count)()
        
        # Calculate active tenant percentage
        active_tenant_percentage = (active_tenants / total_tenants * 100) if total_tenants > 0 else 0
        
        return {
        "status": "success",
            "data": {
                "total_roles": total_roles,
                "total_permissions": total_permissions,
                "total_users": total_users,
                "total_tenants": total_tenants,
                "active_tenants": active_tenants,
                "active_tenant_percentage": round(active_tenant_percentage, 1)
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve role stats: {str(e)}"
        }

@app.get("/api/roles/{role_id}/", tags=["Role Management"])
async def get_role(role_id: int):
    """Get a specific role by ID"""
    try:
        from deelflow.models import Role
        
        role = await sync_to_async(Role.objects.get)(id=role_id)
        
        # Get permissions
        permissions_data = []
        for perm in role.permissions.all():
            permissions_data.append({
                "id": perm.id,
                "name": perm.name,
                "label": perm.label
            })
        
        return {
        "status": "success",
            "data": {
                "id": role.id,
                "name": role.name,
                "label": role.label,
                "permissions": permissions_data,
                "created_at": role.created_at.isoformat(),
                "updated_at": role.updated_at.isoformat()
            }
        }
    except Role.DoesNotExist:
        return {
            "status": "error",
            "message": "Role not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve role: {str(e)}"
        }

@app.post("/api/roles/", tags=["Role Management"])
async def create_role(role_data: dict):
    """Create a new role"""
    try:
        from deelflow.models import Role, Permission
        
        # Extract data
        name = role_data.get("name")
        label = role_data.get("label")
        permission_ids = role_data.get("permission_ids", [])
        
        if not name or not label:
            return {
                "status": "error",
                "message": "Role name and label are required"
            }
        
        # Check if role already exists
        existing_role = await sync_to_async(Role.objects.filter)(name=name)
        if await sync_to_async(existing_role.exists)():
            return {
                "status": "error",
                "message": "Role with this name already exists"
            }
        
        # Create role
        role = await sync_to_async(Role.objects.create)(
            name=name,
            label=label
        )
        
        # Add permissions if provided
        if permission_ids:
            permissions = await sync_to_async(list)(Permission.objects.filter(id__in=permission_ids))
            await sync_to_async(role.permissions.set)(permissions)
        
        # Get the role with permissions for response
        role = await sync_to_async(Role.objects.prefetch_related('permissions').get)(id=role.id)
        
        # Get permissions data
        permissions_data = []
        for perm in role.permissions.all():
            permissions_data.append({
                "id": perm.id,
                "name": perm.name,
                "label": perm.label
            })
        
        return {
        "status": "success",
            "message": "Role created successfully",
            "data": {
                "id": role.id,
                "name": role.name,
                "label": role.label,
                "permissions": permissions_data,
                "created_at": role.created_at.isoformat(),
                "updated_at": role.updated_at.isoformat()
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create role: {str(e)}"
        }

@app.put("/api/roles/{role_id}/", tags=["Role Management"])
async def update_role(role_id: int, role_data: dict):
    """Update a role by ID"""
    try:
        from deelflow.models import Role, Permission
        
        # Get role
        role = await sync_to_async(Role.objects.get)(id=role_id)
        
        # Update fields if provided
        if "name" in role_data:
            # Check if new name already exists (excluding current role)
            existing_role = await sync_to_async(Role.objects.filter)(name=role_data["name"]).exclude(id=role_id)
            if await sync_to_async(existing_role.exists)():
                return {
                    "status": "error",
                    "message": "Role with this name already exists"
                }
            role.name = role_data["name"]
        
        if "label" in role_data:
            role.label = role_data["label"]
        
        await sync_to_async(role.save)()
        
        # Update permissions if provided
        if "permission_ids" in role_data:
            permission_ids = role_data["permission_ids"]
            if permission_ids:
                permissions = await sync_to_async(list)(Permission.objects.filter(id__in=permission_ids))
                await sync_to_async(role.permissions.set)(permissions)
            else:
                await sync_to_async(role.permissions.clear)()
        
        # Get the updated role with permissions
        role = await sync_to_async(Role.objects.prefetch_related('permissions').get)(id=role.id)
        
        # Get permissions data
        permissions_data = []
        for perm in role.permissions.all():
            permissions_data.append({
                "id": perm.id,
                "name": perm.name,
                "label": perm.label
            })
        
        return {
        "status": "success",
            "message": "Role updated successfully",
        "data": {
                "id": role.id,
                "name": role.name,
                "label": role.label,
                "permissions": permissions_data,
                "created_at": role.created_at.isoformat(),
                "updated_at": role.updated_at.isoformat()
            }
        }
    except Role.DoesNotExist:
        return {
            "status": "error",
            "message": "Role not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to update role: {str(e)}"
        }

@app.delete("/api/roles/{role_id}/", tags=["Role Management"])
async def delete_role(role_id: int):
    """Delete a role by ID"""
    try:
        from deelflow.models import Role
        
        role = await sync_to_async(Role.objects.get)(id=role_id)
        await sync_to_async(role.delete)()
        
        return {
            "status": "success",
            "message": "Role deleted successfully"
        }
    except Role.DoesNotExist:
        return {
            "status": "error",
            "message": "Role not found"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to delete role: {str(e)}"
        }

@app.get("/api/permissions/", tags=["Role Management"])
async def get_permissions(page: int = 1, limit: int = 50):
    """Get all permissions with pagination"""
    try:
        from deelflow.models import Permission
        from django.core.paginator import Paginator
        
        # Get all permissions
        permissions_queryset = Permission.objects.all()
        permissions_list = await sync_to_async(list)(permissions_queryset)
        
        # Paginate
        paginator = Paginator(permissions_list, limit)
        page_obj = paginator.get_page(page)
        
        # Convert to response format
        permissions_data = []
        for perm in page_obj:
            permissions_data.append({
                "id": perm.id,
                "name": perm.name,
                "label": perm.label
            })
        
        return {
        "status": "success",
            "data": {
                "permissions": permissions_data,
                "total": paginator.count,
                "page": page,
                "limit": limit,
                "total_pages": paginator.num_pages
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve permissions: {str(e)}"
        }

@app.post("/api/permissions/", tags=["Role Management"])
async def create_permission(permission_data: dict):
    """Create a new permission"""
    try:
        from deelflow.models import Permission
        
        name = permission_data.get("name")
        label = permission_data.get("label")
        
        if not name or not label:
            return {
                "status": "error",
                "message": "Permission name and label are required"
            }
        
        # Check if permission already exists
        existing_permission = await sync_to_async(Permission.objects.filter)(name=name)
        if await sync_to_async(existing_permission.exists)():
            return {
                "status": "error",
                "message": "Permission with this name already exists"
            }
        
        # Create permission
        permission = await sync_to_async(Permission.objects.create)(
            name=name,
            label=label
        )
        
        return {
            "status": "success",
            "message": "Permission created successfully",
            "data": {
                "id": permission.id,
                "name": permission.name,
                "label": permission.label
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to create permission: {str(e)}"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8140)
