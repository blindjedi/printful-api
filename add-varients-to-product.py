import requests
from utils import load_access_token


def add_variants_to_product(product_id, store_id, file_id):
    """
    Adds specific variants to an existing product on Printful.

    :param product_id: The ID of the existing product
    :param store_id: The ID of the store
    :param file_id: The ID of the design file to apply to the product
    :return: Response from the API
    """
    # Load access token from environment
    access_token = load_access_token()

    # API endpoint for updating the product with new variants
    url = f'https://api.printful.com/store/products/{product_id}'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-PF-Store-Id': store_id
    }

    # Example variant IDs for Black, S, M, L sizes
    selected_variants = [
        {"variant_id": 4012, "size": "S"},  # Black S
        {"variant_id": 4013, "size": "M"},  # Black M
        {"variant_id": 4014, "size": "L"}  # Black L
    ]

    # Prepare sync variants for the API
    sync_variants = [
        {
            "variant_id": variant['variant_id'],  # Use the variant ID for Black S, M, L
            "retail_price": "25.00",  # Example price
            "files": [
                {
                    "id": file_id,  # The uploaded image ID
                    "placement": "front"  # Place the design on the front of the shirt
                }
            ]
        } for variant in selected_variants
    ]

    # Payload for adding variants to the product
    payload = {
        "sync_variants": sync_variants
    }

    # Send the PUT request to update the product with the new variants
    response = requests.put(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Variants added successfully:", response.json())
    else:
        print(f"Failed to add variants: {response.status_code}, {response.json()}")


# Example usage
if __name__ == "__main__":
    product_id = 361828771  # The existing product ID
    store_id = "14468233"  # Your store ID
    file_id = 746398768  # The file ID of your uploaded image

    add_variants_to_product(product_id, store_id, file_id)