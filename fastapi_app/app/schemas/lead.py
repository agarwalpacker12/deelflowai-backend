"""
Lead-related Pydantic schemas
"""

from pydantic import BaseModel, validator
from typing import Optional, List, Dict, Any
from datetime import datetime
from decimal import Decimal

class LeadBase(BaseModel):
    """Base lead schema"""
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipcode: Optional[str] = None
    status: str = "new"
    source: str = "manual"
    motivation_score: float = 0.0
    property_condition: Optional[str] = None
    financial_situation: Optional[str] = None
    timeline_urgency: Optional[str] = None
    negotiation_style: Optional[str] = None
    notes: Optional[str] = None

class LeadCreate(LeadBase):
    """Lead creation schema"""
    campaign_id: Optional[int] = None

class LeadUpdate(BaseModel):
    """Lead update schema"""
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipcode: Optional[str] = None
    status: Optional[str] = None
    source: Optional[str] = None
    motivation_score: Optional[float] = None
    property_condition: Optional[str] = None
    financial_situation: Optional[str] = None
    timeline_urgency: Optional[str] = None
    negotiation_style: Optional[str] = None
    notes: Optional[str] = None

class LeadResponse(LeadBase):
    """Lead response schema"""
    id: int
    campaign_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class LeadListResponse(BaseModel):
    """Lead list response schema"""
    leads: List[LeadResponse]
    total: int
    page: int
    limit: int
    has_next: bool
    has_prev: bool

class LeadStats(BaseModel):
    """Lead statistics schema"""
    total_leads: int
    new_leads: int
    qualified_leads: int
    converted_leads: int
    leads_by_source: dict
    average_motivation_score: float
    top_cities: List[Dict[str, Any]]

class DiscoveredLeadBase(BaseModel):
    """Base discovered lead schema"""
    owner_name: Optional[str] = None
    address: str
    city: Optional[str] = None
    state: Optional[str] = None
    zipcode: Optional[str] = None
    source: str
    details: Optional[str] = None
    motivation_score: float = 0.0
    property_condition: Optional[str] = None
    financial_situation: Optional[str] = None
    timeline_urgency: Optional[str] = None
    negotiation_style: Optional[str] = None

class DiscoveredLeadResponse(DiscoveredLeadBase):
    """Discovered lead response schema"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
