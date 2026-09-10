"""Warmup 4 - Handle Request Errors.

Two separate failures to guard against: never reaching the server at all, and
reaching it but getting a status that isn't 200.
"""

import requests

# A hostname that cannot resolve, so the request fails before any HTTP happens.
URL = "https://thisurldoesnotexist.example.com"

try:
    response = requests.get(URL, timeout=10)
except requests.exceptions.RequestException as e:
    # RequestException is the base class for requests' own errors, so this one
    # clause covers ConnectionError, Timeout, TooManyRedirects and the rest.
    # Catching the base class is right here because the user's next step is the
    # same for all of them: check the connection and retry.
    print("Error: Could not reach the server. Check your connection and try again.")
    # Keeping the technical detail available but out of the main message.
    print(f"(Details: {type(e).__name__})")
else:
    # Reached only if the request itself succeeded. A response arriving is not
    # the same as a response being useful - this is the second check.
    if response.status_code != 200:
        print(f"Error: server returned status {response.status_code}, expected 200.")
    else:
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.json()}")
