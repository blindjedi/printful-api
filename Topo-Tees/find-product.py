import requests
from utils import load_access_token

def get_created_products(store_id):
    """
    Fetches a list of products from Printful for the given store.

    :param store_id: The ID of the store
    :return: List of products if successful, None otherwise
    """
    # Load access token from environment
    access_token = load_access_token()

    # API endpoint for getting product sync information
    url = 'https://api.printful.com/store/products'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-PF-Store-Id': store_id
    }

    # Send the GET request to retrieve product details
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        products = response.json()['result']
        print("Products found:")
        return products
    else:
        print(f"Failed to fetch products: {response.status_code}, {response.json()}")
        return None

def find_product_by_name(target_product_name, store_id):
    """
    Finds and prints details of a product by name.

    :param target_product_name: The name of the product to find
    :param store_id: The ID of the store
    """
    # Fetch all products for the store
    products = get_created_products(store_id)

    if not products:
        print("No products found.")
        return

    # Search for the product by name
    for product in products:
        if target_product_name.lower() in product['name'].lower():
            print(f"Found Product: {product['name']}, Product ID: {product['id']}")

            # List the variants for the found product
            if 'sync_variants' in product:
                for variant in product['sync_variants']:
                    print(f"Variant Name: {variant['name']}, Variant ID: {variant['variant_id']}")
            else:
                print(f"No variants found for {product['name']}")

            return product  # Return the found product
    else:
        print(f"Product '{target_product_name}' not found.")
        return None

# Example usage
if __name__ == "__main__":
    target_product_name = "Custom Black Map T-Shirt"  # The name of the product you're looking for
    store_id = "14468233"  # Your store ID

    # Find the product by name and display its details
    found_product = find_product_by_name(target_product_name, store_id)

    if found_product:
        print(f"Product verified. Product ID: {found_product['id']}")
    else:
        print("Product not found or not created correctly.")