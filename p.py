import requests

# Constants for the API
url = 'https://api2.fflow.app.lghive.com/api/v1/forms/d015ef20-be11-45c5-abdb-03f6df1d5cd2/duplicate?type=forms_and_settings'
headers = {
    'accept': 'application/json',
    'sub-tenant-id': 'BSN10404719064601a01',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ0b2tlbklkIjoiVE9LMDUwODA3NjQxNTliN2VkMTAiLCJ0ZW5hbnRJZCI6IlROVDA5NDI0OTIxMDEzZjg0ZTUxIiwidXNlclJvbGUiOlsiUk9MMDgwOTM5NjUyYjQ0YTZiMWMiXSwidXNlcklkIjoiVVNSMDcwMDQzMDc5N2U3MWQwZTEiLCJkZXZpY2VJZCI6IjEwOjIxMzQ6U0QiLCJwbGF0Zm9ybSI6IndlYiIsInVzZXJuYW1lIjoiZGl0dXNlciIsInN1YiI6IlVTUjA3MDA0MzA3OTdlNzFkMGUxIiwiaWF0IjoxNzI1OTQ0ODg3LCJleHAiOjE3MjU5NzcyODd9.AERMxblEGYlnZ9yZwgwkg0yCmHR5bjq_gTnmWI0FCYQ'
}

# List to store IDs
ids_list = []

# Loop to make 100 API calls
for i in range(75):
    try:
        response = requests.put(url, headers=headers)
        response.raise_for_status()  # Ensure the request was successful
        data_id = response.json().get('data', {}).get('id')
        if data_id:
            ids_list.append(data_id)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Print or use the list of IDs as needed
print(ids_list)
