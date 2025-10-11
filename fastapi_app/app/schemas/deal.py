"""
Deal-related Pydantic schemas
"""

from pydantic import BaseModel, validator
from typing import Optional, List, Dict, Any
from datetime import datetime
from decimal import Decimal

class DealResponse(BaseModel):
    """Deal response model"""
    property_id: int
    buyer_lead_id: int
    seller_lead_id: int
    deal_type: str
    status: str
    offer_price: str
    final_price: str
    commission: str
    closing_date: str
    notes: str
    id: int
    created_at: str
    updated_at: str

class DealCreateRequest(BaseModel):
    """Deal creation request model"""
    property_id: int
    buyer_lead_id: int
    seller_lead_id: int
    deal_type: str
    status: str = "pending"
    offer_price: int
    final_price: int
    commission: int
    closing_date: str
    notes: str

class DealUpdateRequest(BaseModel):
    """Deal update request model"""
    property_id: int
    buyer_lead_id: int
    seller_lead_id: int
    deal_type: str
    status: str
    offer_price: int
    final_price: int
    commission: int
    closing_date: str
    notes: str

class DealBase(BaseModel):
    """Base deal schema"""
    property_id: int
    buyer_lead_id: int
    seller_lead_id: int
    deal_type: str
    status: str = "pending"
    offer_price: Decimal
    final_price: Optional[Decimal] = None
    commission: Optional[Decimal] = None
    closing_date: Optional[datetime] = None
    notes: Optional[str] = None

class DealCreate(DealBase):
    """Deal creation schema"""
    pass

class DealUpdate(BaseModel):
    """Deal update schema"""
    property_id: Optional[int] = None
    buyer_lead_id: Optional[int] = None
    seller_lead_id: Optional[int] = None
    deal_type: Optional[str] = None
    status: Optional[str] = None
    offer_price: Optional[Decimal] = None
    final_price: Optional[Decimal] = None
    commission: Optional[Decimal] = None
    closing_date: Optional[datetime] = None
    notes: Optional[str] = None

class DealResponse(DealBase):
    """Deal response schema"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class DealListResponse(BaseModel):
    """Deal list response schema"""
    deals: List[DealResponse]
    total: int
    page: int
    limit: int
    has_next: bool
    has_prev: bool

class DealMilestone(BaseModel):
    """Deal milestone schema"""
    id: int
    deal_id: int
    title: str
    description: str
    status: str
    due_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

class DealStats(BaseModel):
    """Deal statistics schema"""
    total_deals: int
    pending_deals: int
    closed_deals: int
    total_value: Decimal
    average_deal_value: Decimal
    deals_by_type: Dict[str, int]
    deals_by_status: Dict[str, int]
    monthly_deals: List[Dict[str, Any]]
