#!/usr/bin/env python3
"""
Test script for all dashboard endpoints
"""

import requests
import json
import time

BASE_URL = "http://localhost:8140"

def test_endpoint(endpoint, expected_keys=None):
    """Test a single endpoint"""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ {endpoint}: {response.status_code}")
            if expected_keys:
                for key in expected_keys:
                    if key in data.get('data', {}):
                        print(f"   ✓ {key}: {data['data'][key]}")
                    else:
                        print(f"   ✗ Missing key: {key}")
            return True
        else:
            print(f"❌ {endpoint}: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ {endpoint}: Error - {str(e)}")
        return False

def main():
    """Test all dashboard endpoints"""
    print("🧪 Testing Dashboard Endpoints")
    print("=" * 50)
    
    # Wait for server to start
    print("⏳ Waiting for server to start...")
    time.sleep(3)
    
    # Test health first
    if not test_endpoint("/health"):
        print("❌ Server not running. Please start the server first.")
        return
    
    print("\n📊 Testing Dashboard Metrics:")
    print("-" * 30)
    
    endpoints = [
        ("/total-revenue/", ["total_revenue", "change_percentage"]),
        ("/active-users/", ["active_users", "change_percentage"]),
        ("/properties-listed/", ["properties_listed", "change_percentage"]),
        ("/ai-conversations/", ["ai_conversations", "avg_rate"]),
        ("/total-deals/", ["total_deals", "change_percentage"]),
        ("/monthly-profit/", ["monthly_profit", "change_percentage"]),
        ("/voice-calls-count/", ["voice_calls", "change_percentage"]),
        ("/compliance-status/", ["compliance_status", "improvement"]),
    ]
    
    success_count = 0
    for endpoint, keys in endpoints:
        if test_endpoint(endpoint, keys):
            success_count += 1
    
    print(f"\n📈 Testing AI Performance Metrics:")
    print("-" * 30)
    
    ai_endpoints = [
        ("/vision-analysis/", ["total", "accuracy", "processing_time"]),
        ("/nlp-processing/", ["total", "accuracy", "avg_response_time"]),
        ("/blockchain-txns/", ["total", "success_rate", "avg_processing_time"]),
        ("/ai-metrics/overall-accuracy/", ["ai_accuracy", "improvement"]),
    ]
    
    for endpoint, keys in ai_endpoints:
        if test_endpoint(endpoint, keys):
            success_count += 1
    
    print(f"\n🏢 Testing Tenant Management:")
    print("-" * 30)
    
    tenant_endpoints = [
        ("/tenant-management/stats/", ["activeTenants", "paymentOverdue", "suspended", "monthlyRevenue"]),
    ]
    
    for endpoint, keys in tenant_endpoints:
        if test_endpoint(endpoint, keys):
            success_count += 1
    
    print(f"\n📊 Testing Other Endpoints:")
    print("-" * 30)
    
    other_endpoints = [
        ("/live-activity-feed/", ["activities"]),
        ("/revenue-user-growth-chart-data/", ["revenue_growth", "user_growth"]),
        ("/market-alerts/recent/", ["alerts"]),
        ("/compliance-status/details/", ["overall_compliance"]),
        ("/deal-completions-scheduling/", ["scheduled_completions"]),
        ("/current-subscription/", ["plan", "features"]),
    ]
    
    for endpoint, keys in other_endpoints:
        if test_endpoint(endpoint, keys):
            success_count += 1
    
    total_endpoints = len(endpoints) + len(ai_endpoints) + len(tenant_endpoints) + len(other_endpoints)
    
    print(f"\n📋 Test Summary:")
    print("=" * 50)
    print(f"✅ Successful: {success_count}/{total_endpoints}")
    print(f"❌ Failed: {total_endpoints - success_count}/{total_endpoints}")
    print(f"📊 Success Rate: {(success_count/total_endpoints)*100:.1f}%")
    
    if success_count == total_endpoints:
        print("\n🎉 All endpoints are working correctly!")
    else:
        print(f"\n⚠️  {total_endpoints - success_count} endpoints need attention.")

if __name__ == "__main__":
    main()
