#!/usr/bin/env python3
"""
Example client to demonstrate how to send requests to the Calculator API
"""

import requests
import json

# Base URL of your API
BASE_URL = "http://localhost:8000"

def test_calculator_api():
    """Test all calculator endpoints"""
    
    print("🧮 Calculator API Client Example\n")
    
    # Test addition
    print("➕ Testing Addition:")
    response = requests.post(f"{BASE_URL}/calc/add", 
                           json={"a": 5, "b": 3})
    print(f"5 + 3 = {response.json()['result']}")
    print(f"Full response: {response.json()}\n")
    
    # Test subtraction
    print("➖ Testing Subtraction:")
    response = requests.post(f"{BASE_URL}/calc/subtract", 
                           json={"a": 10, "b": 4})
    print(f"10 - 4 = {response.json()['result']}")
    print(f"Full response: {response.json()}\n")
    
    # Test multiplication
    print("✖️ Testing Multiplication:")
    response = requests.post(f"{BASE_URL}/calc/multiply", 
                           json={"a": 6, "b": 7})
    print(f"6 × 7 = {response.json()['result']}")
    print(f"Full response: {response.json()}\n")
    
    # Test division
    print("➗ Testing Division:")
    response = requests.post(f"{BASE_URL}/calc/divide", 
                           json={"a": 15, "b": 3})
    print(f"15 ÷ 3 = {response.json()['result']}")
    print(f"Full response: {response.json()}\n")
    
    # Test division by zero (error case)
    print("⚠️ Testing Division by Zero:")
    try:
        response = requests.post(f"{BASE_URL}/calc/divide", 
                               json={"a": 10, "b": 0})
        if response.status_code == 400:
            print(f"Error (as expected): {response.json()['detail']}")
        else:
            print(f"Unexpected response: {response.json()}")
    except Exception as e:
        print(f"Request failed: {e}")
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    test_calculator_api()