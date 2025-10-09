#!/usr/bin/env python3
"""
DeelFlowAI Authentication Test Script
Tests all authentication endpoints and flows
"""

import requests
import json
import time

# Configuration
BACKEND_URL = "http://localhost:8000"
FRONTEND_URL = "http://localhost:5173"

class AuthenticationTester:
    def __init__(self):
        self.session = requests.Session()
        self.test_results = []
        
    def log_test(self, test_name, status, details=""):
        """Log test results"""
        result = {
            "test": test_name,
            "status": status,
            "details": details,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.test_results.append(result)
        
        status_icon = "✅" if status == "PASS" else "❌"
        print(f"{status_icon} {test_name}: {details}")
        
    def test_backend_health(self):
        """Test backend health"""
        try:
            response = self.session.get(f"{BACKEND_URL}/health")
            if response.status_code == 200:
                self.log_test("Backend Health", "PASS", "Backend is running and healthy")
                return True
            else:
                self.log_test("Backend Health", "FAIL", f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Backend Health", "FAIL", f"Connection error: {str(e)}")
            return False
    
    def test_frontend_connectivity(self):
        """Test frontend connectivity"""
        try:
            response = self.session.get(FRONTEND_URL)
            if response.status_code == 200:
                self.log_test("Frontend Connectivity", "PASS", "Frontend is accessible")
                return True
            else:
                self.log_test("Frontend Connectivity", "FAIL", f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Frontend Connectivity", "FAIL", f"Connection error: {str(e)}")
            return False
    
    def test_authentication_endpoints(self):
        """Test all authentication endpoints"""
        auth_endpoints = [
            ("/api/auth/login", "POST", "User Login"),
            ("/api/auth/register", "POST", "User Registration"),
            ("/api/auth/logout", "POST", "User Logout"),
            ("/api/auth/me", "GET", "Current User Info"),
        ]
        
        passed = 0
        total = len(auth_endpoints)
        
        for endpoint, method, description in auth_endpoints:
            try:
                if method == "GET":
                    response = self.session.get(f"{BACKEND_URL}{endpoint}")
                elif method == "POST":
                    # Test with mock data
                    test_data = {
                        "email": "test@deelflowai.com",
                        "password": "testpassword123"
                    }
                    response = self.session.post(f"{BACKEND_URL}{endpoint}", json=test_data)
                else:
                    response = self.session.request(method, f"{BACKEND_URL}{endpoint}")
                
                if response.status_code in [200, 201]:
                    self.log_test(f"Auth Endpoint: {description}", "PASS", f"Status: {response.status_code}")
                    passed += 1
                else:
                    self.log_test(f"Auth Endpoint: {description}", "FAIL", f"Status: {response.status_code}, Response: {response.text[:100]}")
            except Exception as e:
                self.log_test(f"Auth Endpoint: {description}", "FAIL", f"Error: {str(e)}")
        
        success_rate = (passed / total) * 100
        self.log_test("Authentication Endpoints Summary", "PASS" if passed == total else "FAIL", 
                     f"{passed}/{total} endpoints working ({success_rate:.1f}%)")
        return passed == total
    
    def test_cors_headers(self):
        """Test CORS headers for authentication endpoints"""
        try:
            response = self.session.options(f"{BACKEND_URL}/api/auth/login")
            cors_headers = {
                "Access-Control-Allow-Origin": response.headers.get("Access-Control-Allow-Origin"),
                "Access-Control-Allow-Methods": response.headers.get("Access-Control-Allow-Methods"),
                "Access-Control-Allow-Headers": response.headers.get("Access-Control-Allow-Headers"),
            }
            
            if cors_headers["Access-Control-Allow-Origin"] == "*":
                self.log_test("CORS Headers", "PASS", f"CORS properly configured: {cors_headers}")
                return True
            else:
                self.log_test("CORS Headers", "FAIL", f"CORS configuration issue: {cors_headers}")
                return False
        except Exception as e:
            self.log_test("CORS Headers", "FAIL", f"Error checking CORS: {str(e)}")
            return False
    
    def test_login_flow(self):
        """Test complete login flow"""
        try:
            # Test login
            login_data = {
                "email": "admin@deelflowai.com",
                "password": "password123"
            }
            response = self.session.post(f"{BACKEND_URL}/api/auth/login", json=login_data)
            
            if response.status_code == 200:
                login_result = response.json()
                if "data" in login_result and "tokens" in login_result["data"]:
                    self.log_test("Login Flow", "PASS", "Login successful with tokens")
                    
                    # Test getting current user with token
                    access_token = login_result["data"]["tokens"]["access_token"]
                    headers = {"Authorization": f"Bearer {access_token}"}
                    
                    me_response = self.session.get(f"{BACKEND_URL}/api/auth/me", headers=headers)
                    if me_response.status_code == 200:
                        self.log_test("Token Validation", "PASS", "Access token valid")
                        return True
                    else:
                        self.log_test("Token Validation", "FAIL", f"Status: {me_response.status_code}")
                        return False
                else:
                    self.log_test("Login Flow", "FAIL", "No tokens in response")
                    return False
            else:
                self.log_test("Login Flow", "FAIL", f"Status: {response.status_code}, Response: {response.text}")
                return False
        except Exception as e:
            self.log_test("Login Flow", "FAIL", f"Error: {str(e)}")
            return False
    
    def test_registration_flow(self):
        """Test complete registration flow"""
        try:
            # Test registration
            register_data = {
                "email": "newuser@deelflowai.com",
                "password": "newpassword123",
                "name": "New User"
            }
            response = self.session.post(f"{BACKEND_URL}/api/auth/register", json=register_data)
            
            if response.status_code == 200:
                register_result = response.json()
                if "data" in register_result and "tokens" in register_result["data"]:
                    self.log_test("Registration Flow", "PASS", "Registration successful with tokens")
                    return True
                else:
                    self.log_test("Registration Flow", "FAIL", "No tokens in response")
                    return False
            else:
                self.log_test("Registration Flow", "FAIL", f"Status: {response.status_code}, Response: {response.text}")
                return False
        except Exception as e:
            self.log_test("Registration Flow", "FAIL", f"Error: {str(e)}")
            return False
    
    def test_logout_flow(self):
        """Test logout flow"""
        try:
            # First login to get a token
            login_data = {
                "email": "admin@deelflowai.com",
                "password": "password123"
            }
            login_response = self.session.post(f"{BACKEND_URL}/api/auth/login", json=login_data)
            
            if login_response.status_code == 200:
                # Test logout
                logout_response = self.session.post(f"{BACKEND_URL}/api/auth/logout")
                if logout_response.status_code == 200:
                    self.log_test("Logout Flow", "PASS", "Logout successful")
                    return True
                else:
                    self.log_test("Logout Flow", "FAIL", f"Status: {logout_response.status_code}")
                    return False
            else:
                self.log_test("Logout Flow", "FAIL", "Could not login first")
                return False
        except Exception as e:
            self.log_test("Logout Flow", "FAIL", f"Error: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all authentication tests"""
        print("🔐 DeelFlowAI Authentication Test Suite")
        print("=" * 50)
        
        # Basic connectivity tests
        backend_healthy = self.test_backend_health()
        frontend_accessible = self.test_frontend_connectivity()
        
        if not backend_healthy:
            print("\n❌ Backend is not running. Please start the backend server first.")
            return False
        
        # Authentication tests
        auth_endpoints_ok = self.test_authentication_endpoints()
        cors_ok = self.test_cors_headers()
        
        # Flow tests
        login_ok = self.test_login_flow()
        registration_ok = self.test_registration_flow()
        logout_ok = self.test_logout_flow()
        
        # Summary
        print("\n" + "=" * 50)
        print("📊 AUTHENTICATION TEST SUMMARY")
        print("=" * 50)
        
        total_tests = len(self.test_results)
        passed_tests = len([r for r in self.test_results if r["status"] == "PASS"])
        failed_tests = total_tests - passed_tests
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"Success Rate: {success_rate:.1f}%")
        
        if failed_tests == 0:
            print("\n🎉 Authentication System: FULLY FUNCTIONAL")
            print("✅ All authentication endpoints are working")
            print("✅ Login, registration, and logout flows are working")
            print("✅ CORS is properly configured")
            print("✅ Token-based authentication is working")
        else:
            print(f"\n❌ Authentication System: {failed_tests} issues found")
            print("Please review the failed tests above and address the issues.")
        
        # Save detailed results
        with open("authentication_test_results.json", "w") as f:
            json.dump(self.test_results, f, indent=4)
        print(f"\n📄 Detailed results saved to: authentication_test_results.json")
        
        return failed_tests == 0

if __name__ == "__main__":
    tester = AuthenticationTester()
    success = tester.run_all_tests()
    exit(0 if success else 1)
