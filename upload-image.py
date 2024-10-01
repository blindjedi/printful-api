import requests
from utils import load_access_token


def add_file_by_url(file_url, store_id):
    """
    Adds a file to the Printful file library by providing a URL.

    :param file_url: The URL of the file to add
    :param store_id: The ID of the store where the file will be added
    :return: File ID if successful, None otherwise
    """
    # Load access token from environment
    access_token = load_access_token()

    # API endpoint for adding a file via URL
    add_file_url = 'https://api.printful.com/files'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-PF-Store-Id': store_id
    }

    # JSON payload for adding the file by URL
    data = {
        "url": file_url,  # URL of the file to download
        "type": "preview",  # Role of the file (you can change this to what suits your use case)
        "filename": "Brek-map.jpg",  # Optional: you can specify a custom filename
        "visible": True  # Whether the file should be visible in the Printful library
    }

    # Send the POST request
    response = requests.post(add_file_url, headers=headers, json=data)

    if response.status_code == 200:
        file_id = response.json()['result']['id']
        print(f"File added successfully. File ID: {file_id}")
        return file_id
    else:
        print(f"Failed to add file by URL: {response.status_code}, {response.json()}")
        return None


# Example usage
if __name__ == "__main__":
    file_url = "https://i.ibb.co/S7zxBkM/gaia-screenshot.png"  # The hosted image URL
    store_id = "14468233"  # Store ID for your store
    file_id = add_file_by_url(file_url, store_id)