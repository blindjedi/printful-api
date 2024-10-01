import requests
from utils import load_access_token


def get_mockup_styles(product_id):
    """
    Fetches mockup styles for the given product ID (Printful Catalog v2 API).

    :param product_id: The catalog product ID (e.g., 71 for Bella + Canvas 3001)
    :return: A list of mockup styles if successful, None otherwise
    """
    access_token = load_access_token()

    # API endpoint for retrieving mockup styles in the new v2-beta API
    url = f"https://api.printful.com/v2/catalog-products/{product_id}/mockup-styles"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    # Send GET request to retrieve mockup styles
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"Successfully fetched mockup styles for product ID {product_id}")
        styles = response.json()['data']

        for style in styles:
            print(f"Placement: {style.get('placement', 'N/A')}")
            print(f"Display Name: {style.get('display_name', 'N/A')}")
            print(f"Technique: {style.get('technique', 'N/A')}")
            print(f"Print Area (Width x Height): {style.get('print_area_width', 'N/A')} x {style.get('print_area_height', 'N/A')}")

            for mockup_style in style.get('mockup_styles', []):
                print(f"Style ID: {mockup_style.get('id', 'N/A')}")
                print(f"View Name: {mockup_style.get('view_name', 'N/A')}")
    else:
        print(f"Failed to fetch mockup styles: {response.status_code}, {response.json()}")
        return None


# Example usage
if __name__ == "__main__":
    product_id = 71  # The catalog product ID for Bella + Canvas 3001
    get_mockup_styles(product_id)