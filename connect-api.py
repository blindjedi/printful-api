import requests
from utils import load_access_token

access_token = load_access_token()

# url = 'https://api.printful.com/store'
#
# headers = {
#     'Authorization': f'Bearer {access_token}'
# }
#
# response = requests.get(url, headers=headers)
#
# if response.status_code == 200:
#     print("Access token is working!")
#     print(response.json())  # Print the store information
# else:
#     print("Failed to connect:", response.status_code, response.json())

# Store ID: 14468233

url = 'https://api.printful.com/stores'
headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    store_data = response.json()
    store_id = store_data['result'][0]['id']  # Assuming you have only one store
    print("Store ID:", store_id)
else:
    print("Failed to get store ID:", response.status_code, response.json())