import os
import json
import requests


import re

from email.utils import parseaddr
from typing import Optional, Dict, Any


def json_print(data):
    print(json.dumps(data, indent=2))


def sample_data_download(url):
    # Download the data
    resp = requests.get()
    data = json.loads(resp.text)  # Load data

    # Parse the JSON and preview it
    print(type(data), len(data))
    json_print(data[0])
    return data


def get_env_key(key, default=None) -> str:
    """Gets the API key from an environment variable."""
    env_key = os.getenv(key, default=default)
    if not env_key:
        print(f"{key} environment variable is not set.")
        # raise ValueError("Key environment variable is not set.")
    return env_key


# Use the json.loads() function.: This function will parse the JSON string and return a Python object. If the string
# is not valid JSON, it will throw a ValueError exception. You can use this exception to assert that the value is not
# a JSON.
def assert_is_json(string):
    try:
        json.loads(string)
    except ValueError:
        raise AssertionError("String is not a valid JSON")


def extract_and_validate_domain(email: str) -> Optional[str]:
    if email is None or email == '':
        return None
    # Parse the email address to get the domain
    parsed_email = parseaddr(email)[1]

    # Regular expression to validate the domain part of the email
    domain_regex = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    domain = parsed_email.split('@')[-1]

    if re.match(domain_regex, domain):
        return domain
    else:
        return None


def filter_none_values(data: dict) -> Dict[str, Any]:
    """
    Filters out keys with None values from the given dictionary.

    Args:
        data (FilterInputModel): A Pydantic model containing the input dictionary.

    Returns:
        Dict[str, Any]: A new dictionary without None values.
    """
    return {key: value for key, value in data.items() if value is not None}
