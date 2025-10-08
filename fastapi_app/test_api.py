"""
Test script for DeelFlowAI API
"""

import requests
import json
import time

def test_api():
    base_url = "http://localhost:8000"
    
    print("Testing DeelFlowAI API...")
    
    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/")
        print(f"Root endpoint: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error testing root endpoint: {e}")
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Health endpoint: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error testing health endpoint: {e}")
    
    # Test API docs
    try:
        response = requests.get(f"{base_url}/docs")
        print(f"API docs: {response.status_code}")
    except Exception as e:
        print(f"Error testing API docs: {e}")
    
    # Test API v1 endpoints
    try:
        response = requests.get(f"{base_url}/api/v1/")
        print(f"API v1: {response.status_code}")
    except Exception as e:
        print(f"Error testing API v1: {e}")

if __name__ == "__main__":
    test_api()
