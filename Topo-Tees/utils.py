from dotenv import load_dotenv
import os


def load_access_token():
    """
    Loads the Printful API access token from the .env file.

    :return: The access token as a string if found, raises an error if not found.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get the access token from the environment
    access_token = os.getenv('ACCESS_TOKEN')

    # Error handling if access token is not found
    if access_token is None:
        raise ValueError("Access token not found in environment variables!")

    return access_token
