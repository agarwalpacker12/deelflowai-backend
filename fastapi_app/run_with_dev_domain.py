#!/usr/bin/env python3
"""
Run DeelFlowAI Backend Server accessible via dev.deelflowai.com:8000
This script configures the server to work with the dev domain
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
    print("🚀 Starting DeelFlowAI Backend Server for dev.deelflowai.com:8140...")
    print("📍 Server will be available at:")
    print("   - http://dev.deelflowai.com:8140 (if hosts file configured)")
    print("   - http://localhost:8140")
    print("   - http://127.0.0.1:8140")
    print("📚 API Documentation: http://localhost:8140/docs")
    print("🔧 ReDoc: http://localhost:8140/redoc")
    print("=" * 60)
    print("⚠️  IMPORTANT: To use dev.deelflowai.com:8140, add this to your hosts file:")
    print("   127.0.0.1 dev.deelflowai.com")
    print("   (Run as Administrator: notepad C:\\Windows\\System32\\drivers\\etc\\hosts)")
    print("=" * 60)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # Bind to all interfaces
        port=8140,
        reload=True,
        log_level="info",
        access_log=True
    )
