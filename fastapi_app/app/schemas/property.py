"""
Property-related Pydantic schemas
"""

from pydantic import BaseModel, validator
from typing import Optional, List, Dict, Any
from datetime import datetime
from decimal import Decimal

class PropertyBase(BaseModel):
    """Base property schema"""
    address: str
    city: str
    state: str
    zipcode: str
    property_type: str
    price: Decimal
    bedrooms: Optional[int] = None
    bathrooms: Optional[float] = None
    square_feet: Optional[int] = None
    lot_size: Optional[float] = None
    year_built: Optional[int] = None
    description: Optional[str] = None
    images: List[str] = []

class PropertyCreate(PropertyBase):
    """Property creation schema"""
    pass

class PropertyUpdate(BaseModel):
    """Property update schema"""
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipcode: Optional[str] = None
    property_type: Optional[str] = None
    price: Optional[Decimal] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[float] = None
    square_feet: Optional[int] = None
    lot_size: Optional[float] = None
    year_built: Optional[int] = None
    description: Optional[str] = None
    images: Optional[List[str]] = None

class PropertyResponse(PropertyBase):
    """Property response schema"""
    id: int
    status: str
    ai_analysis: Optional[Dict[str, Any]] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class PropertyListResponse(BaseModel):
    """Property list response schema"""
    properties: List[PropertyResponse]
    total: int
    page: int
    limit: int
    has_next: bool
    has_prev: bool

class PropertyAIAnalysis(BaseModel):
    """Property AI analysis schema"""
    property_id: int
    ai_confidence: float
    distress_level: float
    motivation: str
    timeline: str
    roi_percent: float
    cap_rate: float
    cash_flow: float
    market_stability_score: float
    comparables_confidence: float
    analysis_date: datetime

class PropertyStats(BaseModel):
    """Property statistics schema"""
    total_properties: int
    active_properties: int
    sold_properties: int
    average_price: Decimal
    price_range: Dict[str, Decimal]
    properties_by_type: Dict[str, int]
    top_cities: List[Dict[str, Any]]
