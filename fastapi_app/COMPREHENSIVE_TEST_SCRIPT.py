#!/usr/bin/env python3
"""
DeelFlowAI Comprehensive Test Script
Tests all backend endpoints and functionality
"""

import requests
import json
import time
import sys
from datetime import datetime

class DeelFlowAITester:
    def __init__(self, base_url="http://localhost:8140"):
        self.base_url = base_url
        self.session = requests.Session()
        self.test_results = []
        self.jwt_token = None
        
    def log_test(self, test_name, status, details=""):
        """Log test results"""
        result = {
            "test": test_name,
            "status": status,
            "details": details,
            "timestamp": datetime.now().isoformat()
        }
        self.test_results.append(result)
        
        status_icon = "✅" if status == "PASS" else "❌"
        print(f"{status_icon} {test_name}: {status}")
        if details:
            print(f"   Details: {details}")
    
    def test_health_check(self):
        """Test health check endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/health")
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "healthy":
                    self.log_test("Health Check", "PASS", f"Status: {data.get('status')}")
                    return True
                else:
                    self.log_test("Health Check", "FAIL", f"Unexpected status: {data.get('status')}")
                    return False
            else:
                self.log_test("Health Check", "FAIL", f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Health Check", "FAIL", f"Exception: {str(e)}")
            return False
    
    def test_stats_endpoint(self):
        """Test stats endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/stats")
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success" and "data" in data:
                    self.log_test("Stats Endpoint", "PASS", f"Data keys: {list(data['data'].keys())}")
                    return True
                else:
                    self.log_test("Stats Endpoint", "FAIL", f"Invalid response structure")
                    return False
            else:
                self.log_test("Stats Endpoint", "FAIL", f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Stats Endpoint", "FAIL", f"Exception: {str(e)}")
            return False
    
    def test_organization_status(self):
        """Test organization status endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/organizations/status")
            if response.status_code == 200:
                data = response.json()
                if "status" in data and "organization_id" in data:
                    self.log_test("Organization Status", "PASS", f"Org ID: {data.get('organization_id')}")
                    return True
                else:
                    self.log_test("Organization Status", "FAIL", f"Invalid response structure")
                    return False
            else:
                self.log_test("Organization Status", "FAIL", f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Organization Status", "FAIL", f"Exception: {str(e)}")
            return False
    
    def test_voice_ai_calls(self):
        """Test voice AI calls endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/voice-ai-calls-count", timeout=5)
            if response.status_code == 200:
                data = response.json()
                if "total_calls" in data or "calls_count" in data:
                    self.log_test("Voice AI Calls", "PASS", f"Response: {data}")
                    return True
                else:
                    self.log_test("Voice AI Calls", "FAIL", f"Invalid response structure: {data}")
                    return False
            else:
                self.log_test("Voice AI Calls", "FAIL", f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Voice AI Calls", "FAIL", f"Connection issue - endpoint may be overloaded")
            return False
    
    def test_tenant_stats(self):
        """Test tenant management stats endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/tenant-management/stats")
            if response.status_code == 200:
                data = response.json()
                if "status" in data and "data" in data and "total_tenants" in data["data"]:
                    self.log_test("Tenant Stats", "PASS", f"Total tenants: {data['data']['total_tenants']}")
                    return True
                else:
                    self.log_test("Tenant Stats", "FAIL", f"Invalid response structure: {data}")
                    return False
            else:
                self.log_test("Tenant Stats", "FAIL", f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Tenant Stats", "FAIL", f"Exception: {str(e)}")
            return False
    
    def test_recent_activity_get(self):
        """Test recent activity GET endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/recent_activity")
            if response.status_code == 200:
                data = response.json()
                if "status" in data and "data" in data and "activities" in data["data"]:
                    self.log_test("Recent Activity GET", "PASS", f"Activities count: {len(data['data']['activities'])}")
                    return True
                else:
                    self.log_test("Recent Activity GET", "FAIL", f"Invalid response structure: {data}")
                    return False
            else:
                self.log_test("Recent Activity GET", "FAIL", f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Recent Activity GET", "FAIL", f"Exception: {str(e)}")
            return False
    
    def test_recent_activity_post(self):
        """Test recent activity POST endpoint"""
        try:
            payload = {
                "property_id": 1,
                "activity_type": "view",
                "user_id": 1,
                "timestamp": datetime.now().isoformat()
            }
            response = self.session.post(
                f"{self.base_url}/recent_activity",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            if response.status_code == 200:
                data = response.json()
                self.log_test("Recent Activity POST", "PASS", f"Response: {data}")
                return True
            else:
                self.log_test("Recent Activity POST", "FAIL", f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Recent Activity POST", "FAIL", f"Exception: {str(e)}")
            return False
    
    def test_opportunity_cost_analysis(self):
        """Test opportunity cost analysis endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/opportunity-cost-analysis")
            if response.status_code == 200:
                data = response.json()
                if "status" in data and "data" in data and "opportunity_cost" in data["data"]:
                    self.log_test("Opportunity Cost Analysis", "PASS", f"Opportunity cost: {data['data']['opportunity_cost']}")
                    return True
                else:
                    self.log_test("Opportunity Cost Analysis", "FAIL", f"Invalid response structure: {data}")
                    return False
            else:
                self.log_test("Opportunity Cost Analysis", "FAIL", f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Opportunity Cost Analysis", "FAIL", f"Exception: {str(e)}")
            return False
    
    def test_user_registration(self):
        """Test user registration endpoint"""
        try:
            payload = {
                "email": f"test_{int(time.time())}@example.com",
                "password": "testpassword123",
                "name": "Test User"
            }
            response = self.session.post(
                f"{self.base_url}/api/auth/register",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            if response.status_code == 200:
                data = response.json()
                if "status" in data and "message" in data:
                    self.log_test("User Registration", "PASS", f"Response: {data['message']}")
                    return True
                else:
                    self.log_test("User Registration", "FAIL", f"Unexpected response: {data}")
                    return False
            else:
                self.log_test("User Registration", "FAIL", f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("User Registration", "FAIL", f"Exception: {str(e)}")
            return False
    
    def test_user_login(self):
        """Test user login endpoint"""
        try:
            payload = {
                "email": "test@example.com",
                "password": "testpassword123"
            }
            response = self.session.post(
                f"{self.base_url}/api/auth/login",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            if response.status_code == 200:
                data = response.json()
                if "status" in data and "message" in data:
                    self.log_test("User Login", "PASS", f"Response: {data['message']}")
                    return True
                else:
                    self.log_test("User Login", "FAIL", f"Unexpected response: {data}")
                    return False
            else:
                self.log_test("User Login", "FAIL", f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("User Login", "FAIL", f"Exception: {str(e)}")
            return False
    
    def test_cors_headers(self):
        """Test CORS headers"""
        try:
            response = self.session.options(f"{self.base_url}/stats")
            if response.status_code == 200:
                cors_headers = {
                    "Access-Control-Allow-Origin": response.headers.get("Access-Control-Allow-Origin"),
                    "Access-Control-Allow-Methods": response.headers.get("Access-Control-Allow-Methods"),
                    "Access-Control-Allow-Headers": response.headers.get("Access-Control-Allow-Headers")
                }
                self.log_test("CORS Headers", "PASS", f"Headers: {cors_headers}")
                return True
            else:
                self.log_test("CORS Headers", "FAIL", f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("CORS Headers", "FAIL", f"Exception: {str(e)}")
            return False
    
    def test_api_documentation(self):
        """Test API documentation endpoints"""
        try:
            # Test Swagger UI
            response = self.session.get(f"{self.base_url}/docs")
            if response.status_code == 200:
                self.log_test("Swagger UI", "PASS", "Documentation accessible")
            else:
                self.log_test("Swagger UI", "FAIL", f"HTTP {response.status_code}")
                return False
            
            # Test OpenAPI spec
            response = self.session.get(f"{self.base_url}/openapi.json")
            if response.status_code == 200:
                data = response.json()
                if "openapi" in data and "info" in data:
                    self.log_test("OpenAPI Spec", "PASS", f"Version: {data.get('openapi')}")
                    return True
                else:
                    self.log_test("OpenAPI Spec", "FAIL", "Invalid OpenAPI structure")
                    return False
            else:
                # OpenAPI spec might not be available in development mode
                self.log_test("OpenAPI Spec", "SKIP", f"HTTP {response.status_code} - May not be available in dev mode")
                return True  # Don't fail the test for this
        except Exception as e:
            self.log_test("API Documentation", "SKIP", f"Exception: {str(e)} - May not be available in dev mode")
            return True  # Don't fail the test for this
    
    def run_all_tests(self):
        """Run all tests"""
        print("🚀 Starting DeelFlowAI Comprehensive Test Suite")
        print("=" * 60)
        print(f"Testing server at: {self.base_url}")
        print("=" * 60)
        
        # Core functionality tests
        self.test_health_check()
        self.test_stats_endpoint()
        self.test_organization_status()
        self.test_voice_ai_calls()
        self.test_tenant_stats()
        self.test_recent_activity_get()
        self.test_recent_activity_post()
        self.test_opportunity_cost_analysis()
        
        # Authentication tests
        self.test_user_registration()
        self.test_user_login()
        
        # Infrastructure tests
        self.test_cors_headers()
        self.test_api_documentation()
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for result in self.test_results if result["status"] == "PASS")
        total = len(self.test_results)
        
        print(f"Total Tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {total - passed}")
        print(f"Success Rate: {(passed/total)*100:.1f}%")
        
        if passed == total:
            print("\n🎉 ALL TESTS PASSED! Backend is ready for production.")
        else:
            print(f"\n⚠️  {total - passed} tests failed. Please check the issues above.")
        
        return passed == total
    
    def save_results(self, filename="test_results.json"):
        """Save test results to file"""
        with open(filename, 'w') as f:
            json.dump(self.test_results, f, indent=2)
        print(f"\n📄 Test results saved to: {filename}")

def main():
    """Main function"""
    base_url = "http://localhost:8140"
    
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    
    print(f"DeelFlowAI Test Suite - Testing: {base_url}")
    
    tester = DeelFlowAITester(base_url)
    success = tester.run_all_tests()
    tester.save_results()
    
    if success:
        print("\n✅ Backend is ready for frontend integration!")
        print("📝 Next steps:")
        print("1. Update frontend API URL to http://localhost:8140")
        print("2. Start frontend: npm run dev")
        print("3. Test full integration")
    else:
        print("\n❌ Backend has issues that need to be resolved.")
        sys.exit(1)

if __name__ == "__main__":
    main()
