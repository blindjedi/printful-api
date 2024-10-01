import requests
from utils import load_access_token


def get_catalog_variants(product_id):
    """
    Fetches all catalog variants for the given product ID (Printful Catalog v2 API).

    :param product_id: The catalog product ID (e.g., 71 for Bella + Canvas 3001)
    :return: A list of all catalog variants if successful, None otherwise
    """
    access_token = load_access_token()
    url = f"https://api.printful.com/v2/catalog-products/{product_id}/catalog-variants"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    all_variants = []
    while url:  # Keep fetching until there's no 'next' link
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            variants = response_data['data']
            all_variants.extend(variants)

            # Check if there's a 'next' link to follow for more pages
            next_link = response_data.get('_links', {}).get('next', {}).get('href')
            url = next_link  # If 'next' exists, set it as the URL for the next request
        else:
            print(f"Failed to fetch catalog variants: {response.status_code}, {response.json()}")
            return None

    # Print and return the list of all fetched variants
    print(f"Successfully fetched {len(all_variants)} catalog variants for product ID {product_id}")
    for variant in all_variants:
        variant_id = variant['id']
        display_name = variant.get('name', 'No name')
        print(f"Variant Name: {display_name}, Variant ID: {variant_id}")

    return all_variants


# Example usage
if __name__ == "__main__":
    product_id = 71  # The catalog product ID for Bella + Canvas 3001
    get_catalog_variants(product_id)