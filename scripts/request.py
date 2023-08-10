from typing import Any, Dict, List

import requests
from helpers import time_it
from requests.exceptions import HTTPError


def get_user_info(user_id: int) -> Dict[str, Any] | None:
    """
    The function `get_user_info` makes a GET request to a local server to retrieve user information
    based on a given user ID, and returns the response as a JSON object if the request is successful.

    Args:
      user_id (int): The `user_id` parameter is an integer that represents the unique identifier of a
    user.

    Returns:
      a dictionary with user information if the request is successful (status code 200). If there is an
    HTTP error, it will print the error message and raise the exception. If the request is not
    successful, it will return None.
    """
    try:
        response = requests.get(f"https://localhost:8000/users/{user_id}").json()
        response.raise_for_status()

        if response.status_code == 200:
            return response.json()

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise http_err
