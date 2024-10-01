import requests
from utils import load_access_token


def create_product(file_id, selected_variants, store_id):
    """
    Creates a product on Printful with the given file and selected variants.

    :param file_id: The ID of the uploaded file (design)
    :param selected_variants: List of variants to apply the design to
    :param store_id: The ID of the store
    :return: Response from the API
    """
    # Load access token from environment
    access_token = load_access_token()

    # API endpoint for creating a product
    create_product_url = 'https://api.printful.com/store/products'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-PF-Store-Id': store_id
    }

    # Prepare sync variants for the API
    sync_variants = [
        {
            "variant_id": variant['id'],  # Use the variant ID for Black, S, M, L
            "retail_price": "25.00",  # Example price
            "files": [
                {
                    "id": file_id,  # The uploaded image ID
                    "placement": "front"  # Place the design on the front of the shirt
                }
            ]
        } for variant in selected_variants
    ]

    # Payload for creating the product
    payload = {
        "sync_product": {
            "name": "Custom Black Map T-Shirt",  # Customize the product name
            "thumbnail": None,  # Optional thumbnail URL
            # "external_id": "your_product_id"  # Optional external ID
        },
        "sync_variants": sync_variants
    }

    # Send the request to create the product
    response = requests.post(create_product_url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Product created successfully:", response.json())
    else:
        print(f"Failed to create product: {response.status_code}, {response.json()}")


# Example usage
if __name__ == "__main__":
    # Replace these with your file ID and selected variants
    file_id = 746398768  # File ID from the successful image upload
    store_id = "14468233"  # Your store ID

    # Example selected variants for Bella + Canvas 3001 in Black, S, M, L
    selected_variants = [
        {"id": 4012, "size": "S"},  # Example variant ID for Black S
        {"id": 4013, "size": "M"},  # Example variant ID for Black M
        {"id": 4014, "size": "L"}  # Example variant ID for Black L
    ]

    create_product(file_id, selected_variants, store_id)