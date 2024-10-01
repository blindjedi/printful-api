import requests
from utils import load_access_token

# Load access token from environment variables
access_token = load_access_token()

# Product ID for "Unisex Staple T-Shirt | Bella + Canvas 3001"
product_id = 71  # Product ID found earlier

# Fetch details for this specific product
product_url = f'https://api.printful.com/products/{product_id}'
headers = {
    'Authorization': f'Bearer {access_token}'
}

product_response = requests.get(product_url, headers=headers)

if product_response.status_code == 200:
    product_data = product_response.json()['result']
    print(f"Product Details for: {product_data['product']['title']}")
    print(f"Description: {product_data['product'].get('description', 'No description available')}")

    # Display only black variants for sizes S, M, L
    print("\nSelected Variants (Black, S, M, L):")
    selected_variants = []
    for variant in product_data['variants']:
        if variant['color'].lower() == 'black' and variant['size'] in ['S', 'M', 'L']:
            selected_variants.append(variant)
            print(f"- Variant Name: {variant['name']}, Variant ID: {variant['id']}, Size: {variant['size']}")
else:
    print(f"Failed to fetch details for product ID {product_id}:",
          product_response.status_code, product_response.json())

# You now have the selected variants in `selected_variants`, which can be used to apply the image.