"""
Test specific API endpoints
"""

import requests
import json

def test_endpoints():
    base_url = "http://localhost:8000"
    
    print("Testing specific API endpoints...")
    
    # Test authentication endpoints
    print("\n=== Testing Authentication ===")
    try:
        # Test login endpoint
        login_data = {
            "email": "test@example.com",
            "password": "testpassword"
        }
        response = requests.post(f"{base_url}/api/v1/auth/login", json=login_data)
        print(f"Login endpoint: {response.status_code}")
        if response.status_code != 200:
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error testing login: {e}")
    
    # Test properties endpoints
    print("\n=== Testing Properties ===")
    try:
        response = requests.get(f"{base_url}/api/v1/properties/")
        print(f"Properties list: {response.status_code}")
        if response.status_code != 200:
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error testing properties: {e}")
    
    # Test leads endpoints
    print("\n=== Testing Leads ===")
    try:
        response = requests.get(f"{base_url}/api/v1/leads/")
        print(f"Leads list: {response.status_code}")
        if response.status_code != 200:
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error testing leads: {e}")
    
    # Test deals endpoints
    print("\n=== Testing Deals ===")
    try:
        response = requests.get(f"{base_url}/api/v1/deals/")
        print(f"Deals list: {response.status_code}")
        if response.status_code != 200:
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error testing deals: {e}")
    
    # Test campaigns endpoints
    print("\n=== Testing Campaigns ===")
    try:
        response = requests.get(f"{base_url}/api/v1/campaigns/")
        print(f"Campaigns list: {response.status_code}")
        if response.status_code != 200:
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error testing campaigns: {e}")
    
    # Test AI endpoints
    print("\n=== Testing AI Services ===")
    try:
        response = requests.get(f"{base_url}/api/v1/ai/metrics/overall")
        print(f"AI metrics: {response.status_code}")
        if response.status_code != 200:
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error testing AI metrics: {e}")
    
    # Test analytics endpoints
    print("\n=== Testing Analytics ===")
    try:
        response = requests.get(f"{base_url}/api/v1/analytics/dashboard")
        print(f"Analytics dashboard: {response.status_code}")
        if response.status_code != 200:
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error testing analytics: {e}")

if __name__ == "__main__":
    test_endpoints()
