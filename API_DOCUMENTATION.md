# DeelFlowAI Backend API Documentation

## Overview

DeelFlowAI is a comprehensive real estate AI platform backend API built with FastAPI and Django. It provides endpoints for property management, lead generation, deal tracking, AI-powered analytics, and multi-channel campaign management.

## Base URL

```
http://localhost:8000
```

## Authentication

The API uses JWT (JSON Web Token) authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

## API Endpoints

### 1. Authentication Endpoints

#### POST /api/v1/auth/login
Login with email and password.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "role": "user",
    "is_active": true
  }
}
```

#### POST /api/v1/auth/register
Register a new user.

**Request Body:**
```json
{
  "email": "newuser@example.com",
  "password": "password123",
  "first_name": "Jane",
  "last_name": "Smith",
  "organization_id": 1
}
```

#### POST /api/v1/auth/refresh
Refresh access token using refresh token.

#### POST /api/v1/auth/logout
Logout user (invalidate token).

### 2. Property Management Endpoints

#### GET /api/v1/properties/
Get list of properties with filtering and pagination.

**Query Parameters:**
- `skip`: Number of records to skip (default: 0)
- `limit`: Number of records to return (default: 100)
- `search`: Search term for property address
- `property_type`: Filter by property type
- `min_price`: Minimum price filter
- `max_price`: Maximum price filter

**Response:**
```json
{
  "properties": [
    {
      "id": 1,
      "address": "123 Main St",
      "city": "Dallas",
      "state": "TX",
      "zipcode": "75201",
      "property_type": "residential",
      "price": 250000.00,
      "bedrooms": 3,
      "bathrooms": 2.5,
      "square_feet": 2000,
      "status": "active",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ],
  "total": 1,
  "page": 1,
  "limit": 100,
  "has_next": false,
  "has_prev": false
}
```

#### GET /api/v1/properties/{property_id}
Get specific property by ID.

#### POST /api/v1/properties/
Create a new property.

**Request Body:**
```json
{
  "address": "123 Main St",
  "city": "Dallas",
  "state": "TX",
  "zipcode": "75201",
  "property_type": "residential",
  "price": 250000.00,
  "bedrooms": 3,
  "bathrooms": 2.5,
  "square_feet": 2000,
  "description": "Beautiful family home"
}
```

#### PUT /api/v1/properties/{property_id}
Update an existing property.

#### DELETE /api/v1/properties/{property_id}
Delete a property.

#### GET /api/v1/properties/{property_id}/ai-analysis
Get AI analysis for a specific property.

### 3. Lead Management Endpoints

#### GET /api/v1/leads/
Get list of leads with filtering and pagination.

**Query Parameters:**
- `skip`: Number of records to skip (default: 0)
- `limit`: Number of records to return (default: 100)
- `search`: Search term for lead name or email
- `status`: Filter by lead status
- `source`: Filter by lead source

**Response:**
```json
{
  "leads": [
    {
      "id": 1,
      "name": "John Smith",
      "email": "john@example.com",
      "phone": "+1234567890",
      "address": "456 Oak Ave",
      "status": "new",
      "source": "manual",
      "motivation_score": 8.5,
      "created_at": "2024-01-01T00:00:00Z"
    }
  ],
  "total": 1,
  "page": 1,
  "limit": 100,
  "has_next": false,
  "has_prev": false
}
```

#### GET /api/v1/leads/{lead_id}
Get specific lead by ID.

#### POST /api/v1/leads/
Create a new lead.

#### PUT /api/v1/leads/{lead_id}
Update an existing lead.

#### DELETE /api/v1/leads/{lead_id}
Delete a lead.

#### GET /api/v1/leads/discovered/
Get discovered leads from various sources.

#### POST /api/v1/leads/{lead_id}/qualify
Qualify a lead.

#### POST /api/v1/leads/{lead_id}/convert
Convert a lead to a deal.

### 4. Deal Management Endpoints

#### GET /api/v1/deals/
Get list of deals with filtering and pagination.

**Query Parameters:**
- `skip`: Number of records to skip (default: 0)
- `limit`: Number of records to return (default: 100)
- `search`: Search term for deal
- `status`: Filter by deal status
- `deal_type`: Filter by deal type

**Response:**
```json
{
  "deals": [
    {
      "id": 1,
      "property_id": 1,
      "buyer_lead_id": 1,
      "seller_lead_id": 2,
      "deal_type": "purchase",
      "status": "pending",
      "offer_price": 250000.00,
      "final_price": null,
      "commission": 7500.00,
      "closing_date": null,
      "created_at": "2024-01-01T00:00:00Z"
    }
  ],
  "total": 1,
  "page": 1,
  "limit": 100,
  "has_next": false,
  "has_prev": false
}
```

#### GET /api/v1/deals/{deal_id}
Get specific deal by ID.

#### POST /api/v1/deals/
Create a new deal.

#### PUT /api/v1/deals/{deal_id}
Update an existing deal.

#### DELETE /api/v1/deals/{deal_id}
Delete a deal.

#### POST /api/v1/deals/{deal_id}/close
Close a deal.

#### GET /api/v1/deals/{deal_id}/milestones
Get deal milestones.

### 5. Campaign Management Endpoints

#### GET /api/v1/campaigns/
Get list of campaigns with filtering and pagination.

**Query Parameters:**
- `skip`: Number of records to skip (default: 0)
- `limit`: Number of records to return (default: 100)
- `search`: Search term for campaign name
- `status`: Filter by campaign status
- `channel`: Filter by campaign channel

**Response:**
```json
{
  "campaigns": [
    {
      "id": 1,
      "name": "Q1 2024 Email Campaign",
      "campaign_type": "new",
      "channel": "email",
      "budget": 5000.00,
      "status": "active",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ],
  "total": 1,
  "page": 1,
  "limit": 100,
  "has_next": false,
  "has_prev": false
}
```

#### GET /api/v1/campaigns/{campaign_id}
Get specific campaign by ID.

#### POST /api/v1/campaigns/
Create a new campaign.

#### PUT /api/v1/campaigns/{campaign_id}
Update an existing campaign.

#### DELETE /api/v1/campaigns/{campaign_id}
Delete a campaign.

#### POST /api/v1/campaigns/{campaign_id}/start
Start a campaign.

#### POST /api/v1/campaigns/{campaign_id}/pause
Pause a campaign.

#### GET /api/v1/campaigns/{campaign_id}/performance
Get campaign performance metrics.

### 6. AI Services Endpoints

#### POST /api/v1/ai/vision/analyze
Analyze property images using AI vision.

**Request Body:**
```json
{
  "image_url": "https://example.com/image.jpg",
  "analysis_type": "property_condition",
  "confidence_threshold": 0.7
}
```

**Response:**
```json
{
  "analysis_type": "property_condition",
  "result": {
    "condition": "good",
    "confidence": 0.85,
    "issues": ["minor_crack"],
    "recommendations": ["repair_crack"]
  },
  "confidence": 0.85,
  "processing_time": 1.2,
  "timestamp": "2024-01-01T00:00:00Z"
}
```

#### POST /api/v1/ai/nlp/process
Process text using NLP.

**Request Body:**
```json
{
  "text": "I'm interested in selling my house quickly",
  "analysis_type": "sentiment",
  "language": "en"
}
```

#### POST /api/v1/ai/voice/analyze
Analyze voice calls using AI.

#### GET /api/v1/ai/metrics/overall
Get overall AI performance metrics.

#### GET /api/v1/ai/metrics/vision
Get vision analysis metrics.

#### GET /api/v1/ai/metrics/nlp
Get NLP processing metrics.

#### GET /api/v1/ai/metrics/voice
Get voice AI metrics.

#### GET /api/v1/ai/metrics/blockchain
Get blockchain transaction metrics.

### 7. Analytics Endpoints

#### GET /api/v1/analytics/dashboard
Get dashboard metrics.

**Response:**
```json
{
  "total_revenue": 150000.00,
  "active_users": 25,
  "total_properties": 150,
  "total_leads": 300,
  "total_deals": 45,
  "monthly_profit": 45000.00,
  "voice_calls_count": 120,
  "ai_conversations": 250,
  "compliance_percentage": 98.5,
  "system_health": "healthy",
  "last_updated": "2024-01-01T00:00:00Z"
}
```

#### GET /api/v1/analytics/business
Get business metrics.

#### GET /api/v1/analytics/ai
Get AI analytics.

#### GET /api/v1/analytics/revenue
Get revenue metrics.

#### GET /api/v1/analytics/users
Get user metrics.

#### GET /api/v1/analytics/campaigns
Get campaign metrics.

#### GET /api/v1/analytics/leads
Get lead metrics.

#### GET /api/v1/analytics/deals
Get deal metrics.

#### GET /api/v1/analytics/activity
Get activity feed.

#### GET /api/v1/analytics/compliance
Get compliance status.

### 8. User Management Endpoints

#### GET /api/v1/users/
Get list of users.

#### GET /api/v1/users/{user_id}
Get specific user by ID.

#### POST /api/v1/users/
Create a new user.

#### PUT /api/v1/users/{user_id}
Update an existing user.

#### DELETE /api/v1/users/{user_id}
Delete a user.

#### GET /api/v1/users/{user_id}/roles
Get user roles.

#### POST /api/v1/users/{user_id}/assign-role
Assign role to user.

#### DELETE /api/v1/users/{user_id}/remove-role
Remove role from user.

### 9. Role and Permission Management Endpoints

#### GET /api/v1/roles/
Get list of roles.

#### GET /api/v1/roles/{role_id}
Get specific role by ID.

#### POST /api/v1/roles/
Create a new role.

#### PUT /api/v1/roles/{role_id}
Update an existing role.

#### DELETE /api/v1/roles/{role_id}
Delete a role.

#### GET /api/v1/roles/permissions/
Get all available permissions.

#### PUT /api/v1/roles/{role_id}/permissions
Update role permissions.

#### GET /api/v1/roles/{role_id}/permissions
Get permissions for a specific role.

### 10. WebSocket Endpoints

#### WS /api/v1/ws/live-activity
WebSocket for live activity feed.

#### WS /api/v1/ws/user/{user_id}
WebSocket for user-specific updates.

#### WS /api/v1/ws/notifications
WebSocket for notifications.

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Validation error message"
}
```

### 401 Unauthorized
```json
{
  "detail": "Could not validate credentials"
}
```

### 403 Forbidden
```json
{
  "detail": "Permission required"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

## Rate Limiting

The API implements rate limiting:
- 60 requests per minute per user
- Rate limit headers are included in responses

## WebSocket Events

### Live Activity Feed
```json
{
  "type": "activity_update",
  "data": {
    "user_id": 1,
    "action": "property_created",
    "description": "New property added",
    "timestamp": "2024-01-01T00:00:00Z"
  }
}
```

### User Notifications
```json
{
  "type": "notification",
  "data": {
    "title": "New Lead",
    "message": "A new lead has been discovered",
    "priority": "high",
    "timestamp": "2024-01-01T00:00:00Z"
  }
}
```

## Background Tasks

The API supports background task processing using Celery:

- Property AI analysis
- Lead discovery
- Campaign message sending
- Business metrics updates
- AI analysis processing

## Database Models

### Core Models
- **User**: User accounts and authentication
- **Organization**: Multi-tenant organization support
- **Property**: Real estate properties
- **Lead**: Potential customers
- **Deal**: Property transactions
- **Campaign**: Marketing campaigns
- **AIAnalysis**: AI analysis results
- **DealMilestone**: Deal progress tracking
- **SavedProperty**: User-saved properties

### AI Models
- **PropertyAIAnalysis**: Property-specific AI analysis
- **VisionAnalysisMetrics**: Vision AI performance
- **NLPProcessingMetrics**: NLP performance
- **VoiceAICallMetrics**: Voice AI performance
- **BlockchainTxnMetrics**: Blockchain transaction metrics

### Analytics Models
- **BusinessMetrics**: Business performance metrics
- **HistoricalMetrics**: Historical data tracking
- **ActivityFeed**: Real-time activity logging
- **ComplianceStatus**: System compliance tracking

## Getting Started

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

3. **Start the Server**
   ```bash
   python main.py
   ```

4. **Access API Documentation**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

5. **Test the API**
   ```bash
   python test_api.py
   ```

## Support

For API support and questions, please contact the development team or refer to the project documentation.
