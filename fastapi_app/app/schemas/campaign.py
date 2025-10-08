"""
Campaign-related Pydantic schemas
"""

from pydantic import BaseModel, validator
from typing import Optional, List, Dict, Any
from datetime import datetime
from decimal import Decimal

class CampaignBase(BaseModel):
    """Base campaign schema"""
    name: str
    campaign_type: str = "new"
    channel: str = "email"
    budget: Optional[Decimal] = None
    scheduled_at: Optional[datetime] = None
    geographic_scope_type: str = "zip"
    geographic_scope_values: List[str] = []
    location: Optional[str] = None
    property_type: Optional[str] = None
    minimum_equity: Optional[Decimal] = None
    min_price: Optional[Decimal] = None
    max_price: Optional[Decimal] = None
    distress_indicators: List[str] = []
    subject_line: Optional[str] = None
    email_content: Optional[str] = None
    use_ai_personalization: bool = False

class CampaignCreate(CampaignBase):
    """Campaign creation schema"""
    pass

class CampaignUpdate(BaseModel):
    """Campaign update schema"""
    name: Optional[str] = None
    campaign_type: Optional[str] = None
    channel: Optional[str] = None
    budget: Optional[Decimal] = None
    scheduled_at: Optional[datetime] = None
    geographic_scope_type: Optional[str] = None
    geographic_scope_values: Optional[List[str]] = None
    location: Optional[str] = None
    property_type: Optional[str] = None
    minimum_equity: Optional[Decimal] = None
    min_price: Optional[Decimal] = None
    max_price: Optional[Decimal] = None
    distress_indicators: Optional[List[str]] = None
    subject_line: Optional[str] = None
    email_content: Optional[str] = None
    use_ai_personalization: Optional[bool] = None

class CampaignResponse(CampaignBase):
    """Campaign response schema"""
    id: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class CampaignListResponse(BaseModel):
    """Campaign list response schema"""
    campaigns: List[CampaignResponse]
    total: int
    page: int
    limit: int
    has_next: bool
    has_prev: bool

class CampaignPerformance(BaseModel):
    """Campaign performance metrics schema"""
    campaign_id: int
    total_sent: int
    total_delivered: int
    total_opened: int
    total_clicked: int
    total_converted: int
    open_rate: float
    click_rate: float
    conversion_rate: float
    roi_percentage: float
    cost_per_lead: Decimal
    revenue_generated: Decimal

class CampaignStats(BaseModel):
    """Campaign statistics schema"""
    total_campaigns: int
    active_campaigns: int
    completed_campaigns: int
    total_leads_generated: int
    total_revenue: Decimal
    average_roi: float
    top_performing_channels: List[Dict[str, Any]]
