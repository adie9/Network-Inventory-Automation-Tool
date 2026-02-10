import requests
import json
import pandas as pd

def main():
    # Get data from API URL
    r = requests.get("https://6988ea18780e8375a6897173.mockapi.io/devices")
    
    # Error handling for unsuccessful data retrieval
    if r.status_code != 200:
        print("Error! Could not retrieve data. Exiting program...")
        return
    
    devices = r.json()
    
    # Create table using data from API request
    data_frame = pd.DataFrame(devices)
    print(data_frame)
    
    # Write to JSON file
    with open("baseline.json", 'w') as file:
        json.dump(devices, file, indent=4)
      
if __name__ == "__main__":
    main()