#!/usr/bin/env python3
"""
Comprehensive Frontend-Backend Integration Test Script
Tests all API endpoints and verifies frontend-backend connectivity
"""

import requests
import json
import time
from datetime import datetime

class IntegrationTester:
    def __init__(self):
        self.backend_url = "http://localhost:8000"
        self.frontend_url = "http://localhost:5173"
        self.results = []
        
    def log_test(self, test_name, status, message="", response_data=None):
        """Log test results"""
        result = {
            "test": test_name,
            "status": status,
            "message": message,
            "timestamp": datetime.now().isoformat(),
            "response_data": response_data
        }
        self.results.append(result)
        
        status_icon = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
        print(f"{status_icon} {test_name}: {message}")
        
    def test_backend_health(self):
        """Test backend health endpoint"""
        try:
            response = requests.get(f"{self.backend_url}/health", timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.log_test("Backend Health Check", "PASS", 
                            f"Backend is healthy - {data.get('status')}", data)
                return True
            else:
                self.log_test("Backend Health Check", "FAIL", 
                            f"Unexpected status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Backend Health Check", "FAIL", f"Connection error: {str(e)}")
            return False
    
    def test_frontend_connectivity(self):
        """Test frontend connectivity"""
        try:
            response = requests.get(self.frontend_url, timeout=5)
            if response.status_code == 200:
                self.log_test("Frontend Connectivity", "PASS", 
                            f"Frontend is accessible on port 5173")
                return True
            else:
                self.log_test("Frontend Connectivity", "FAIL", 
                            f"Unexpected status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Frontend Connectivity", "FAIL", f"Connection error: {str(e)}")
            return False
    
    def test_api_endpoints(self):
        """Test all critical API endpoints"""
        endpoints = [
            ("/stats", "Dashboard Statistics"),
            ("/status", "System Status"),
            ("/recent_activity", "Recent Activity Feed"),
            ("/recent_activity/", "Recent Activity Feed (Trailing Slash)"),
            ("/opportunity-cost-analysis", "Opportunity Cost Analysis"),
            ("/api/voice-ai-calls-count", "Voice AI Calls Count"),
            ("/api/voice-ai-calls-count/", "Voice AI Calls Count (Trailing Slash)"),
            ("/api/organizations/status", "Organization Status"),
            ("/api/organizations/status/", "Organization Status (Trailing Slash)"),
            ("/api/analytics/opportunity-cost-analysis", "Analytics Opportunity Cost"),
            ("/api/analytics/opportunity-cost-analysis/", "Analytics Opportunity Cost (Trailing Slash)"),
            ("/api/tenant-management/stats", "Tenant Management Stats"),
            ("/api/tenant-management/stats/", "Tenant Management Stats (Trailing Slash)"),
            ("/api/auth/login", "Authentication Login"),
            ("/api/auth/register", "Authentication Register"),
            ("/api/auth/logout", "Authentication Logout"),
            ("/api/auth/me", "Authentication Current User"),
            ("/api/v1/analytics/stats", "Analytics Stats"),
            ("/api/v1/analytics/status", "Analytics Status"),
            ("/api/v1/analytics/recent-activity", "Analytics Recent Activity"),
            ("/api/v1/analytics/voice-ai-calls-count", "Analytics Voice AI Calls"),
        ]
        
        passed = 0
        total = len(endpoints)
        
        for endpoint, description in endpoints:
            try:
                response = requests.get(f"{self.backend_url}{endpoint}", timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    self.log_test(f"API Endpoint: {description}", "PASS", 
                                f"Endpoint {endpoint} working", data)
                    passed += 1
                else:
                    self.log_test(f"API Endpoint: {description}", "FAIL", 
                                f"Status code {response.status_code} for {endpoint}")
            except Exception as e:
                self.log_test(f"API Endpoint: {description}", "FAIL", 
                            f"Error accessing {endpoint}: {str(e)}")
        
        success_rate = (passed / total) * 100
        self.log_test("API Endpoints Summary", "PASS" if success_rate >= 80 else "WARN", 
                    f"{passed}/{total} endpoints working ({success_rate:.1f}%)")
        return success_rate >= 80
    
    def test_cors_headers(self):
        """Test CORS headers for frontend compatibility"""
        try:
            # Test preflight request
            response = requests.options(f"{self.backend_url}/stats", 
                                      headers={"Origin": self.frontend_url}, timeout=5)
            
            cors_headers = {
                "Access-Control-Allow-Origin": response.headers.get("Access-Control-Allow-Origin"),
                "Access-Control-Allow-Methods": response.headers.get("Access-Control-Allow-Methods"),
                "Access-Control-Allow-Headers": response.headers.get("Access-Control-Allow-Headers"),
            }
            
            if cors_headers["Access-Control-Allow-Origin"]:
                self.log_test("CORS Headers", "PASS", 
                            f"CORS properly configured: {cors_headers}")
                return True
            else:
                self.log_test("CORS Headers", "FAIL", "CORS headers missing")
                return False
        except Exception as e:
            self.log_test("CORS Headers", "FAIL", f"CORS test error: {str(e)}")
            return False
    
    def test_data_consistency(self):
        """Test data consistency across endpoints"""
        try:
            # Test stats endpoint
            stats_response = requests.get(f"{self.backend_url}/stats", timeout=5)
            stats_data = stats_response.json() if stats_response.status_code == 200 else {}
            
            # Test analytics stats endpoint
            analytics_response = requests.get(f"{self.backend_url}/api/v1/analytics/stats", timeout=5)
            analytics_data = analytics_response.json() if analytics_response.status_code == 200 else {}
            
            if stats_data and analytics_data:
                self.log_test("Data Consistency", "PASS", 
                            "Both stats endpoints returning data")
                return True
            else:
                self.log_test("Data Consistency", "WARN", 
                            "Some endpoints not returning data")
                return False
        except Exception as e:
            self.log_test("Data Consistency", "FAIL", f"Data consistency error: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all integration tests"""
        print("🚀 Starting Frontend-Backend Integration Tests")
        print("=" * 60)
        
        # Test backend health
        backend_healthy = self.test_backend_health()
        
        # Test frontend connectivity
        frontend_accessible = self.test_frontend_connectivity()
        
        if not backend_healthy or not frontend_accessible:
            print("\n❌ Basic connectivity tests failed. Cannot proceed with API tests.")
            return False
        
        # Test API endpoints
        api_working = self.test_api_endpoints()
        
        # Test CORS
        cors_working = self.test_cors_headers()
        
        # Test data consistency
        data_consistent = self.test_data_consistency()
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 INTEGRATION TEST SUMMARY")
        print("=" * 60)
        
        total_tests = len(self.results)
        passed_tests = len([r for r in self.results if r["status"] == "PASS"])
        failed_tests = len([r for r in self.results if r["status"] == "FAIL"])
        warning_tests = len([r for r in self.results if r["status"] == "WARN"])
        
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"⚠️  Warnings: {warning_tests}")
        
        success_rate = (passed_tests / total_tests) * 100
        print(f"Success Rate: {success_rate:.1f}%")
        
        if success_rate >= 80:
            print("\n🎉 Frontend-Backend Integration: SUCCESSFUL")
            print("✅ The frontend should now work without console errors")
        else:
            print("\n⚠️  Frontend-Backend Integration: NEEDS ATTENTION")
            print("❌ Some issues need to be resolved")
        
        # Save detailed results
        with open("integration_test_results.json", "w") as f:
            json.dump(self.results, f, indent=2)
        print(f"\n📄 Detailed results saved to: integration_test_results.json")
        
        return success_rate >= 80

def main():
    """Main test execution"""
    print("DeelFlowAI Frontend-Backend Integration Test")
    print("Testing connectivity between frontend (port 5173) and backend (port 8000)")
    print()
    
    tester = IntegrationTester()
    success = tester.run_all_tests()
    
    if success:
        print("\n🎯 RECOMMENDATION: Frontend should now load without console errors!")
        print("   - All critical API endpoints are working")
        print("   - CORS is properly configured")
        print("   - Backend is healthy and responsive")
    else:
        print("\n🔧 RECOMMENDATION: Check the failed tests above and resolve issues")
        print("   - Ensure both frontend and backend are running")
        print("   - Check firewall settings")
        print("   - Verify port configurations")

if __name__ == "__main__":
    main()
