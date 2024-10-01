import requests
from utils import load_access_token

def fetch_product_variants(product_id):
    """
    Fetch all catalog variants for the given product_id.
    """
    access_token = load_access_token()

    url = f"https://api.printful.com/v2/catalog-variants/{product_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        variants = response.json().get('data', [])
        print(f"Successfully fetched {len(variants)} catalog variants for product ID {product_id}")
        for variant in variants:
            print(f"Variant Name: {variant['name']}, Variant ID: {variant['id']}")
        return variants
    else:
        print(f"Failed to fetch catalog variants: {response.status_code}, {response.json()}")
        return None

# Example usage
product_id = 71  # Bella + Canvas 3001
fetch_product_variants(product_id)