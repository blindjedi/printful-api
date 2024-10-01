import requests
from utils import load_access_token

access_token = load_access_token()

def fetch_variant_by_id(variant_id):
    """
    Fetch specific variant details by variant_id.
    """
    access_token = load_access_token()

    url = f"https://api.printful.com/v2/catalog-variants/{variant_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        variant = response.json().get('data', {})
        print(f"Variant ID: {variant['id']}, Name: {variant['name']}")
        print(variant)
        return variant
    else:
        print(f"Failed to fetch variant details: {response.status_code}, {response.json()}")
        return None

# Example usage
variant_id = 4018  # Example variant ID
fetch_variant_by_id(variant_id)