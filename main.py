import requests, json, tabulate
def main():
    # Get API URL
    r = requests.get("https://6988ea18780e8375a6897173.mockapi.io/devices")
    devices = r.json()
    
    # Convert dictionary to JSON string
    json_string = json.dumps(devices, indent=4)
    print(json_string)
    
    
    
if __name__ == "__main__":
    main()