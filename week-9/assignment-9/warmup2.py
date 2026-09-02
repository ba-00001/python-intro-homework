"""Warmup 2 - Access Specific JSON Fields.

Same endpoint as Warmup 1, but pulling out individual fields - including one
that doesn't exist.
"""

import requests

URL = "https://api.agify.io/?name=michael"

response = requests.get(URL, timeout=10)
data = response.json()

# Square brackets are fine for keys I know are there.
print(f"Name: {data['name']}")
print(f"Predicted age: {data['age']}")

# data["birthday"] would raise:
#   KeyError: 'birthday'
# because the API never returns that field. .get() returns the second argument
# instead of raising when the key is absent, which is what makes it the right
# tool for API data - I don't control this response, and a field being missing
# is a normal thing rather than a bug in my code.
print(f"Birthday: {data.get('birthday', 'Not available')}")
