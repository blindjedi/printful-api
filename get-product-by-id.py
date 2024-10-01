import requests
from utils import load_access_token

def get_sync_product_by_id(product_id, store_id):
    """
    Fetches the sync status of a product from Printful and extracts variant IDs.

    :param product_id: The ID of the product
    :param store_id: The ID of the store
    :return: Sync product details and variant IDs if successful, None otherwise
    """
    # Load access token from environment
    access_token = load_access_token()

    # API endpoint for fetching sync product details
    sync_product_url = f'https://api.printful.com/store/products/{product_id}'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-PF-Store-Id': store_id
    }

    # Send the GET request to retrieve the product details
    response = requests.get(sync_product_url, headers=headers)

    if response.status_code == 200:
        product = response.json()['result']
        print(f"Sync Product Details: {product}")

        # Extract variant IDs from the product
        variants = product.get('sync_variants', [])
        variant_ids = [variant['id'] for variant in variants]

        if variant_ids:
            print(f"Variant IDs: {variant_ids}")
        else:
            print("No variants found for this product.")

        return variant_ids
    else:
        print(f"Failed to fetch sync product: {response.status_code}, {response.json()}")
        return None

# Example usage
if __name__ == "__main__":
    product_id = 361834414  # Product ID from the store
    store_id = "14468233"  # Your store ID

    # Fetch and display the sync product details and variant IDs
    variant_ids = get_sync_product_by_id(product_id, store_id)