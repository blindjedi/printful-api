import requests
from utils import load_access_token

def get_print_files(product_id, store_id):
    access_token = load_access_token()
    printfiles_url = f'https://api.printful.com/mockup-generator/printfiles/361834414'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-PF-Store-Id': store_id
    }
    response = requests.get(printfiles_url, headers=headers)
    if response.status_code == 200:
        print("Print files:", response.json())
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.json()}")
        return None

# Example usage
if __name__ == "__main__":
    product_id = 361834414  # Replace with your actual product ID
    store_id = "14468233"  # Replace with your actual store ID
    get_print_files(product_id, store_id)