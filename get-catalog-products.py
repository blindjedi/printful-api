import requests
from utils import load_access_token


def get_catalog_products():
    """
    Fetches a list of catalog products from Printful and filters for the 'Bella + Canvas 3001' T-shirt using 'display_name'.

    :return: The catalog product for Bella + Canvas 3001 if found, otherwise None.
    """
    access_token = load_access_token()

    url = "https://api.printful.com/catalog/products"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        products_data = response.json()  # Fetch the full response
        products = products_data['result']['products']  # Access the 'products' list within 'result'

        # Search for 'Unisex Staple T-Shirt | Bella + Canvas 3001'
        for product in products:
            # Check if 'display_name' exists in the product and it's not None
            display_name = product.get('display_name')
            if display_name and "Bella + Canvas 3001" in display_name:
                return product

        print("Bella + Canvas 3001 product not found.")
        return None
    else:
        print(f"Failed to fetch catalog products: {response.status_code}, {response.json()}")
        return None


# Example usage
if __name__ == "__main__":
    product = get_catalog_products()
    if product:
        print(f"Product found: {product['display_name']} (ID: {product['id']})")