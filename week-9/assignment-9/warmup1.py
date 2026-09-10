"""Warmup 1 - Make Your First API Request.

Fetches a name-to-age prediction from the Agify API and prints the raw
response.
"""

import requests

URL = "https://api.agify.io/?name=michael"

# requests.get() sends an HTTP GET and waits for the reply. timeout is not in
# the assignment, but without it a server that never answers hangs the script
# forever rather than raising something I can catch.
response = requests.get(URL, timeout=10)

# 200 means OK. Worth printing separately from the body because a request can
# come back "successfully" with a status that says the data isn't there - 404,
# 500 - and .json() on that gives you an error body, not your data.
print(f"Status code: {response.status_code}")

# .json() parses the JSON text into Python objects. A JSON object becomes a
# dict, a JSON array becomes a list, so from here on it's the same data
# structures as the past few weeks.
data = response.json()
print(f"Response: {data}")

# The count and age move as the API's dataset grows, so these numbers won't
# match the assignment's sample exactly - that's live data rather than a bug.
