# DeelFlowAI Backend - Quick Start Guide

## 🚀 Quick Setup

### Prerequisites
- Python 3.11+
- PostgreSQL (optional, SQLite works for development)
- Redis (for background tasks)

### 1. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# For FastAPI app
cd fastapi_app
pip install -r requirements.txt
```

### 2. Database Setup

```bash
# Run Django migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 3. Start the Services

#### Option A: Django Development Server
```bash
python manage.py runserver
```
Access: http://localhost:8000

#### Option B: FastAPI Server (Recommended)
```bash
cd fastapi_app
python main.py
```
Access: http://localhost:8000

### 4. Test the API

```bash
# Test basic endpoints
python test_api.py

# Test specific endpoints
python test_endpoints.py
```

## 📚 API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Full Documentation**: See `API_DOCUMENTATION.md`

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the `fastapi_app` directory:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/deelflowai
REDIS_URL=redis://localhost:6379
OPENAI_API_KEY=your-openai-key
```

### Django Settings
Update `deelflowAI/settings.py` for production:
- Change `SECRET_KEY`
- Update `DATABASE` configuration
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`

## 🧪 Testing

### Run Tests
```bash
# Django tests
python manage.py test

# FastAPI tests
cd fastapi_app
python test_api.py
python test_endpoints.py
```

### Test Authentication
```bash
# Register a user
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123",
    "first_name": "Test",
    "last_name": "User"
  }'

# Login
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```

## 🔄 Background Tasks

### Start Celery Worker
```bash
# In the Django project root
celery -A deelflow worker --loglevel=info
```

### Start Celery Beat (Scheduler)
```bash
celery -A deelflow beat --loglevel=info
```

## 📊 Available Endpoints

### Core Endpoints
- `GET /` - API status
- `GET /health` - Health check
- `GET /docs` - API documentation

### Authentication
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/refresh` - Refresh token
- `POST /api/v1/auth/logout` - User logout

### Resources
- `GET /api/v1/properties/` - List properties
- `GET /api/v1/leads/` - List leads
- `GET /api/v1/deals/` - List deals
- `GET /api/v1/campaigns/` - List campaigns
- `GET /api/v1/users/` - List users
- `GET /api/v1/roles/` - List roles

### AI Services
- `POST /api/v1/ai/vision/analyze` - Analyze images
- `POST /api/v1/ai/nlp/process` - Process text
- `POST /api/v1/ai/voice/analyze` - Analyze voice
- `GET /api/v1/ai/metrics/overall` - AI metrics

### Analytics
- `GET /api/v1/analytics/dashboard` - Dashboard metrics
- `GET /api/v1/analytics/business` - Business metrics
- `GET /api/v1/analytics/ai` - AI analytics

### WebSocket
- `WS /api/v1/ws/live-activity` - Live activity feed
- `WS /api/v1/ws/user/{user_id}` - User updates
- `WS /api/v1/ws/notifications` - Notifications

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Make sure you're in the correct directory
   cd deelflowai-backend
   # or
   cd deelflowai-backend/fastapi_app
   ```

2. **Database Connection Issues**
   ```bash
   # Check if database is running
   # For SQLite, make sure the file exists
   # For PostgreSQL, check connection string
   ```

3. **Port Already in Use**
   ```bash
   # Kill process using port 8000
   netstat -ano | findstr :8000
   taskkill /PID <PID> /F
   ```

4. **Authentication Issues**
   - Make sure to include `Authorization: Bearer <token>` header
   - Check if user exists and is active
   - Verify token hasn't expired

### Logs
- Django logs: Check console output
- FastAPI logs: Check console output
- Celery logs: Check worker output

## 📈 Performance

### Optimization Tips
1. Use PostgreSQL for production
2. Enable Redis caching
3. Use connection pooling
4. Implement rate limiting
5. Monitor background tasks

### Monitoring
- Health check: `GET /health`
- Metrics: `GET /api/v1/analytics/dashboard`
- System status: Check logs

## 🔒 Security

### Best Practices
1. Use strong SECRET_KEY
2. Enable HTTPS in production
3. Implement rate limiting
4. Validate all inputs
5. Use environment variables for secrets
6. Regular security updates

## 📞 Support

- **Documentation**: See `API_DOCUMENTATION.md`
- **Issues**: Check logs and error messages
- **Development**: Follow the code structure in `/app` directory

## 🎯 Next Steps

1. **Set up production environment**
2. **Configure monitoring and logging**
3. **Implement additional AI services**
4. **Add more analytics features**
5. **Integrate with external services**

---

**Happy Coding! 🚀**
