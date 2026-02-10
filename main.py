import requests
import json
import pandas as pd

# Function that fetches devices from API
def fetch_devices():
    return requests.get("https://6988ea18780e8375a6897173.mockapi.io/devices")

# Function that checks inventory for errors
def validate_inventory(devices):
    # Initialize empty errors list
    errors = []
    
    # Check for missing fields
    for device in devices:
        for field in ["hostname", "ip", "model"]:
            if field not in device:
                errors.append(f"Missing '{field}' in device: {device}")
    
    # Check for duplicate host names
    host_names = [device["hostname"] for device in devices]
    for name in set(host_names):
        if host_names.count(name) > 1:
            errors.append(f"Duplicate hostname found: {name}")
            
    return errors

def main():
    # Get data from API
    r = fetch_devices()
    
    # Error handling for unsuccessful data retrieval
    if r.status_code != 200:
        print("Error! Could not retrieve data. Exiting program...")
        return
    
    devices = r.json()
    
    # Call validate_inventory function and print if there are errors
    errors = validate_inventory(devices)
    if errors:
        print("Inventory Validation Errors")
        for error in errors:
            print("-", error)
    else: print("Inventory Validation passed with no issues.")
    
    # Create table using data from API request
    data_frame = pd.DataFrame(devices)
    print(data_frame)
    
    # Write to JSON file
    with open("baseline.json", 'w') as file:
        json.dump(devices, file, indent=4)
        
      
if __name__ == "__main__":
    print("\n######################")
    print("Network Inventory Tool")
    print("######################\n")
    main()