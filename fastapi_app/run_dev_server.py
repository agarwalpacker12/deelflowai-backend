#!/usr/bin/env python3
"""
Run DeelFlowAI Backend Server for dev.deelflowai.com:8000
"""

import uvicorn
import os
import sys
from pathlib import Path

# Add Django project to Python path
django_project_path = Path(__file__).parent.parent
sys.path.append(str(django_project_path))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deelflowAI.settings')

if __name__ == "__main__":
    print("🚀 Starting DeelFlowAI Backend Server...")
    print("📍 Server will be available at:")
    print("   - http://dev.deelflowai.com:8000")
    print("   - http://localhost:8000")
    print("   - http://127.0.0.1:8000")
    print("📚 API Documentation: http://dev.deelflowai.com:8000/docs")
    print("🔧 ReDoc: http://dev.deelflowai.com:8000/redoc")
    print("=" * 60)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # Bind to all interfaces
        port=8000,
        reload=True,
        log_level="info",
        access_log=True
    )
