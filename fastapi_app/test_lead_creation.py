#!/usr/bin/env python3
import requests
import json

# Test lead creation
payload = {
    "first_name": "test",
    "last_name": "test",
    "email": "piya4@gmail.com",
    "phone": "1234567890",
    "property_address": "Kolkata",
    "property_city": "Kolkata",
    "property_state": "AZ",
    "property_zip": "712123",
    "property_type": "single_family",
    "source": "referral",
    "estimated_value": "300",
    "mortgage_balance": "43",
    "asking_price": "350",
    "preferred_contact_method": "email",
    "lead_type": "buyer",
    "status": "new"
}

print("Testing POST /leads/ endpoint...")
print(f"Payload: {json.dumps(payload, indent=2)}")
print()

try:
    response = requests.post("http://localhost:8140/leads/", json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 200:
        print("\n✅ SUCCESS: Lead created successfully!")
    else:
        print("\n❌ FAILED: Lead creation failed")
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
