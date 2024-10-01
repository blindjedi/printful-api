import requests
from utils import load_access_token


def create_mockup_task(store_id, product_id, style_id, image_url, variant_ids):
    """
    Create a mockup generation task using the Printful API (v2).
    """
    access_token = load_access_token()

    mockup_task_url = "https://api.printful.com/v2/mockup-tasks"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-PF-Store-Id": store_id,
        "Content-Type": "application/json"
    }

    payload = {
        "format": "jpg",  # Or "png" for transparent background
        "products": [
            {
                "source": "catalog",
                "mockup_style_ids": [style_id],  # Use the correct style ID
                "catalog_product_id": product_id,
                "catalog_variant_ids": variant_ids,  # Use the variant IDs for the product
                "orientation": "vertical",
                "placements": [
                    {
                        "placement": "front",
                        "technique": "DTG",
                        "layers": [
                            {
                                "type": "file",
                                "url": image_url,  # Use your image file URL
                                "position": {
                                    "width": 10,
                                    "height": 4.93,
                                    "top": 0,
                                    "left": 0
                                }
                            }
                        ],
                        # "placement_options": [
                        #     {
                        #         "name": "unlimited_color",
                        #         "value": True
                        #     }
                        # ]
                    }
                ]
            }
        ]
    }

    response = requests.post(mockup_task_url, headers=headers, json=payload)

    if response.status_code == 200:
        task_id = response.json()['data'][0]['id']
        print(f"Mockup task created successfully. Task ID: {task_id}")
        return task_id
    else:
        print(f"Failed to create mockup task: {response.status_code}, {response.json()}")
        return None


# Example usage
if __name__ == "__main__":
    store_id = "14468233"  # Your store ID
    product_id = 71  # Bella + Canvas 3001
    # style_id = 1115  # Style ID for "Men's Front"
    style_id = 849
    image_url = "https://i.ibb.co/S7zxBkM/gaia-screenshot.png"  # Your image URL

    # Use a valid variant ID (e.g., Aqua / M, variant_id: 4022)
    variant_ids = [4018, 8925, 8497]

    # Create the mockup task
    task_id = create_mockup_task(store_id, product_id, style_id, image_url, variant_ids)