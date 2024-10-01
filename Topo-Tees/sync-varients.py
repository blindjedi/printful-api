import requests
from utils import load_access_token


def get_synced_product(store_id, product_id):
    """
    Fetches a synced product and its variants from Printful.

    :param store_id: The ID of the store
    :param product_id: The ID of the product
    :return: Synced product details if successful, None otherwise
    """
    # Load access token from environment
    access_token = load_access_token()

    # API endpoint for fetching the synced product
    url = f'https://api.printful.com/store/products/{product_id}'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-PF-Store-Id': store_id
    }

    # Send the GET request to retrieve the product details
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        product = response.json()['result']
        print(f"Found Product: {product['sync_product']['name']}, Product ID: {product['sync_product']['id']}")

        # Check if variants are available
        if 'sync_variants' in product:
            print("Variants found:")
            for variant in product['sync_variants']:
                print(f"Variant Name: {variant['name']}, Variant ID: {variant['id']}")
        else:
            print(f"No variants found for {product['sync_product']['name']}")

        return product
    else:
        print(f"Failed to fetch synced product: {response.status_code}, {response.json()}")
        return None


# Example usage
if __name__ == "__main__":
    store_id = "14468233"  # Your store ID
    product_id = 361828771  # The product ID from the creation response

    # Fetch and display the synced product details
    get_synced_product(store_id, product_id)