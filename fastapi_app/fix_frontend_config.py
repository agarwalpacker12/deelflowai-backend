#!/usr/bin/env python3
"""
Frontend Configuration Fix Script
This script helps identify and fix frontend configuration issues
"""

import os
import json
import re
from pathlib import Path

class FrontendConfigFixer:
    def __init__(self):
        self.project_root = Path("D:/ASUS/AI Alpha Tech/projects/deelflowAI Software")
        self.frontend_path = self.project_root / "deelflowai-frontend"
        self.backend_path = self.project_root / "deelflowai-backend"
        
    def find_api_config_files(self):
        """Find all files that might contain API configuration"""
        config_files = []
        
        # Common API configuration files
        api_patterns = [
            "**/api.js",
            "**/config.js",
            "**/config.ts",
            "**/.env*",
            "**/vite.config.js",
            "**/vite.config.ts",
            "**/package.json",
            "**/src/config/**",
            "**/src/utils/**",
            "**/src/services/**"
        ]
        
        for pattern in api_patterns:
            files = list(self.frontend_path.glob(pattern))
            config_files.extend(files)
        
        return config_files
    
    def check_api_urls(self, file_path):
        """Check if file contains hardcoded API URLs"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for hardcoded URLs
            patterns = [
                r'dev\.deelflowai\.com:8000',
                r'https?://[^/]+:8000',
                r'localhost:8000',
                r'127\.0\.0\.1:8000',
                r'VITE_API_URL',
                r'REACT_APP_API_URL',
                r'API_BASE_URL',
                r'baseURL',
                r'apiUrl'
            ]
            
            matches = []
            for pattern in patterns:
                found = re.findall(pattern, content, re.IGNORECASE)
                if found:
                    matches.extend(found)
            
            return matches if matches else None
            
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None
    
    def analyze_frontend_config(self):
        """Analyze frontend configuration"""
        print("🔍 Analyzing Frontend Configuration...")
        print("=" * 50)
        
        config_files = self.find_api_config_files()
        issues_found = []
        
        for file_path in config_files:
            if file_path.exists():
                matches = self.check_api_urls(file_path)
                if matches:
                    issues_found.append({
                        'file': str(file_path.relative_to(self.project_root)),
                        'matches': matches
                    })
                    print(f"📁 {file_path.relative_to(self.project_root)}")
                    for match in matches:
                        print(f"   🔍 Found: {match}")
                    print()
        
        return issues_found
    
    def create_env_file(self):
        """Create proper .env file for frontend"""
        env_content = """# DeelFlowAI Frontend Environment Variables
# Backend API Configuration
VITE_API_URL=http://localhost:8000
VITE_API_PORT=8000
VITE_API_BASE_URL=http://localhost:8000

# Development Configuration
NODE_ENV=development
VITE_DEV_MODE=true

# WebSocket Configuration (for Vite HMR)
VITE_WS_URL=ws://localhost:5173

# Feature Flags
VITE_ENABLE_ANALYTICS=true
VITE_ENABLE_DEBUG=true
"""
        
        env_file = self.frontend_path / ".env.local"
        try:
            with open(env_file, 'w') as f:
                f.write(env_content)
            print(f"✅ Created .env.local file: {env_file}")
            return True
        except Exception as e:
            print(f"❌ Error creating .env.local: {e}")
            return False
    
    def check_vite_config(self):
        """Check and fix Vite configuration"""
        vite_config = self.frontend_path / "vite.config.js"
        
        if not vite_config.exists():
            print(f"❌ Vite config not found: {vite_config}")
            return False
        
        try:
            with open(vite_config, 'r') as f:
                content = f.read()
            
            print(f"📁 Current Vite config: {vite_config}")
            print("Current content:")
            print("-" * 30)
            print(content)
            print("-" * 30)
            
            # Check for problematic configurations
            issues = []
            if "0.0.0.0" in content:
                issues.append("Using 0.0.0.0 instead of localhost")
            if "clientPort" not in content:
                issues.append("Missing clientPort configuration")
            
            if issues:
                print("⚠️  Issues found in Vite config:")
                for issue in issues:
                    print(f"   - {issue}")
            else:
                print("✅ Vite config looks good")
            
            return len(issues) == 0
            
        except Exception as e:
            print(f"❌ Error reading Vite config: {e}")
            return False
    
    def create_fix_recommendations(self, issues):
        """Create fix recommendations"""
        print("\n🔧 Fix Recommendations:")
        print("=" * 50)
        
        if not issues:
            print("✅ No configuration issues found!")
            return
        
        print("1. Update API Base URL:")
        print("   - Change all instances of 'dev.deelflowai.com:8000' to 'localhost:8000'")
        print("   - Or use environment variables: process.env.VITE_API_URL")
        
        print("\n2. Create .env.local file:")
        print("   - Add VITE_API_URL=http://localhost:8000")
        print("   - Add VITE_API_PORT=8000")
        
        print("\n3. Fix Vite HMR WebSocket:")
        print("   - Update vite.config.js to use 'localhost' instead of '0.0.0.0'")
        print("   - Add clientPort: 5173")
        
        print("\n4. Update API calls in frontend:")
        print("   - Replace hardcoded URLs with environment variables")
        print("   - Use: import.meta.env.VITE_API_URL")
    
    def run_analysis(self):
        """Run complete frontend configuration analysis"""
        print("🚀 DeelFlowAI Frontend Configuration Analysis")
        print("=" * 60)
        
        # Check if frontend directory exists
        if not self.frontend_path.exists():
            print(f"❌ Frontend directory not found: {self.frontend_path}")
            return False
        
        # Analyze configuration
        issues = self.analyze_frontend_config()
        
        # Check Vite config
        vite_ok = self.check_vite_config()
        
        # Create .env file
        env_created = self.create_env_file()
        
        # Create recommendations
        self.create_fix_recommendations(issues)
        
        # Summary
        print("\n📊 Analysis Summary:")
        print("=" * 30)
        print(f"Configuration files checked: {len(self.find_api_config_files())}")
        print(f"Issues found: {len(issues)}")
        print(f"Vite config OK: {'✅' if vite_ok else '❌'}")
        print(f"Environment file created: {'✅' if env_created else '❌'}")
        
        if len(issues) == 0 and vite_ok and env_created:
            print("\n🎉 Frontend configuration is ready!")
            print("✅ All issues have been addressed")
        else:
            print(f"\n⚠️  {len(issues)} configuration issues need manual fixing")
            print("Please follow the recommendations above")
        
        return len(issues) == 0 and vite_ok and env_created

if __name__ == "__main__":
    fixer = FrontendConfigFixer()
    success = fixer.run_analysis()
    exit(0 if success else 1)
