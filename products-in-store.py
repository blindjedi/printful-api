import requests
from utils import load_access_token

def get_store_products(store_id):
    """
    Fetches the list of all products from the specified store.

    :param store_id: The ID of the store
    :return: List of products if successful, None otherwise
    """
    # Load access token from environment
    access_token = load_access_token()

    # API endpoint for fetching all products in the store
    store_products_url = 'https://api.printful.com/store/products'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-PF-Store-Id': store_id
    }

    # Send the GET request to retrieve all store products
    response = requests.get(store_products_url, headers=headers)

    if response.status_code == 200:
        products = response.json()['result']
        print(f"Products in store: {products}")
        return products
    else:
        print(f"Failed to fetch store products: {response.status_code}, {response.json()}")
        return None

# Example usage
if __name__ == "__main__":
    store_id = "14468233"  # Your store ID
    get_store_products(store_id)