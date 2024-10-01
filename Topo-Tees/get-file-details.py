import requests
from utils import load_access_token

def get_file_details(file_id, store_id):
    """
    Fetches file details from the Printful File Library.

    :param file_id: The ID of the file in Printful's file library
    :param store_id: Your Printful store ID
    :return: The file details, including the URL, if successful
    """
    access_token = load_access_token()

    # API endpoint to get file details
    url = f"https://api.printful.com/files/{file_id}"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-PF-Store-Id': store_id
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_details = response.json().get('result')
        file_url = file_details.get('url')
        print(f"File URL: {file_url}")
        return file_url
    else:
        print(f"Failed to fetch file details: {response.status_code}, {response.json()}")
        return None

# Example usage
if __name__ == "__main__":
    file_id = 746478538  # Replace this with the file ID you previously uploaded
    store_id = "14468233"  # Your store ID
    get_file_details(file_id, store_id)