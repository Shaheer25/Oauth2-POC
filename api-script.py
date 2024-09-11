import requests
import time
import json

# Define the API endpoint
url = "https://api-dev.einstonlabs.com/api/v1/helper/location"
params = {
    'lat': 27.973126,
    'lon': 61.796085
}

def call_api_until_status_false():
    while True:
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data , sort_keys= True , indent=1)) 

            if 'status' in data and not data['status']:
                print("Status is false. Stopping the script.")
                break
        else:
            print(f"Failed to get a valid response. Status code: {response.status_code}")
            break
        
        time.sleep(1)
print(call_api_until_status_false())
