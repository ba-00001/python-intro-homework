"""Warmup 3 - Loop Through a JSON List.

Fetches the countries in one World Bank region and prints the first ten names.

The assignment originally pointed at restcountries.com. That API was deprecated
mid-course - it now answers with HTTP 200 and an error envelope rather than a
list - and its v5 replacement requires an API key. The World Bank API is
keyless and returns the same kind of nested JSON, so it stands in here. See the
README for the full note.
"""

import requests

# region=ECS is the World Bank's code for Europe & Central Asia. Passing it as
# a query parameter means the server does the filtering and sends back less
# data, rather than me downloading everything and throwing most of it away.
URL = "https://api.worldbank.org/v2/country?format=json&region=ECS&per_page=100"

response = requests.get(URL, timeout=30)
payload = response.json()

# This API wraps its results: the top level is a two-item list where [0] is
# pagination metadata and [1] is the actual list of countries. So the data I
# want is one level deeper than it first looks - exactly the "dicts inside
# lists inside dicts" navigation this week is about.
metadata = payload[0]
countries = payload[1]

print(f"Region has {metadata['total']} countries. First 10:")

# [:10] slices the first ten. Slicing past the end is safe - if the region had
# only 4 countries this would quietly give 4 rather than raising IndexError.
for country in countries[:10]:
    # Each item is a dict. The name is a plain string here; region is itself a
    # nested dict, which is why it would be country["region"]["value"].
    print(country["name"])
