"""Mini-project - Country Explorer CLI.

An interactive menu over live country data: search by name, or list a region
sorted by population.

The assignment named restcountries.com. That API was deprecated mid-course -
it answers HTTP 200 with an error envelope instead of a list - and its v5
replacement needs an API key. The World Bank API is keyless and carries all
four required fields, so it stands in. The trade-off is that name, capital and
region come from one endpoint while population comes from another, so this
script fetches both and joins them.
"""

import requests

COUNTRY_URL = "https://api.worldbank.org/v2/country?format=json&per_page=400"
POPULATION_URL = (
    "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL"
    "?format=json&mrnev=1&per_page=400"
)


def fetch_json(url):
    """GET a URL and return the parsed JSON, or None if anything goes wrong."""
    try:
        response = requests.get(url, timeout=30)
    except requests.exceptions.RequestException:
        # Never reached the server - DNS failure, no connection, timeout.
        print("Error: could not reach the World Bank API. Check your connection.")
        return None

    # A response arriving is not the same as a response being useful. This is
    # the lesson the deprecated restcountries API taught the hard way: it
    # returned 200 with no data in it, so status alone is not enough.
    if response.status_code != 200:
        print(f"Error: API returned status {response.status_code}, expected 200.")
        return None

    payload = response.json()

    # This API wraps results as [metadata, [rows]]. A request that failed at
    # the application level comes back shaped differently, so check before
    # indexing rather than letting it raise IndexError or KeyError.
    if not isinstance(payload, list) or len(payload) < 2:
        print("Error: unexpected response shape from the API.")
        return None

    return payload[1]


def fetch_populations():
    """Return a dict of {country id: latest population}."""
    rows = fetch_json(POPULATION_URL)

    if rows is None:
        return None

    populations = {}

    for row in rows:
        # mrnev=1 asks for the most recent non-empty value, but a country with
        # no data at all still comes back with value None. .get() plus the None
        # check means one missing figure doesn't take out the whole dict.
        value = row.get("value")

        if value is None:
            continue

        # Keyed by ISO3 code, because that is what the OTHER endpoint calls
        # "id". The population rows also carry row["country"]["id"], but that
        # is a different World Bank code ("ZH", "1A"), so joining on it
        # silently matches nothing and every population comes out 0 - which is
        # exactly the bug I hit first time round.
        iso3 = row.get("countryiso3code")

        if not iso3:
            continue

        populations[iso3] = int(value)

    return populations


def fetch_countries():
    """Return a list of dicts with name, capital, region and population."""
    rows = fetch_json(COUNTRY_URL)

    if rows is None:
        return None

    populations = fetch_populations()

    if populations is None:
        return None

    countries = []

    for row in rows:
        # The World Bank list includes aggregate rows like "Arab World" and
        # "Euro area", which are not countries. They're all marked with the
        # region "Aggregates", so filtering on that leaves only real ones.
        region = row["region"]["value"].strip()

        if region == "Aggregates":
            continue

        # capitalCity is present but can be an empty string for a few
        # territories. Empty is falsy, so this catches both "" and a missing
        # key, and the display shows N/A rather than a blank column.
        capital = row.get("capitalCity") or "N/A"

        countries.append(
            {
                "name": row["name"],
                "capital": capital,
                "region": region,
                # .get() with a default, because a country present in the list
                # endpoint may have no population figure at all.
                "population": populations.get(row["id"], 0),
            }
        )

    return countries


def format_country(country):
    """Return one country as a single display line."""
    # :, inserts thousands separators, so 5530719 reads as 5,530,719.
    return (
        f"{country['name']} — Capital: {country['capital']} "
        f"| Region: {country['region']} "
        f"| Population: {country['population']:,}"
    )


def search_by_name(countries, term):
    """Return countries whose name contains term, ignoring case."""
    matches = []

    # Lowered once here rather than inside the loop - same result, but it makes
    # clear the comparison is case-insensitive on both sides.
    term = term.lower()

    for country in countries:
        # `in` on strings is a substring test, which is what makes this a
        # partial match: "land" finds Finland, Iceland, Ireland, Poland.
        if term in country["name"].lower():
            matches.append(country)

    return matches


def filter_by_region(countries, region_term):
    """Return countries in a region, largest population first."""
    region_term = region_term.lower()

    matches = []

    for country in countries:
        # Partial match here too, so "europe" finds "Europe & Central Asia"
        # without the user having to type the full World Bank region name.
        if region_term in country["region"].lower():
            matches.append(country)

    # sorted() returns a new list rather than reordering the caller's. key
    # picks which field to sort on; reverse=True puts the largest first.
    return sorted(matches, key=lambda c: c["population"], reverse=True)


def show_menu():
    """Print the menu and return the user's choice as a string."""
    print()
    print("=== Country Explorer ===")
    print("1. Search by name")
    print("2. Filter by region")
    print("3. Quit")
    return input("Choose an option (1-3): ").strip()


def print_results(matches):
    """Print a list of countries, or say there were none."""
    if not matches:
        print("No matches found.")
        return

    for country in matches:
        print(format_country(country))

    print(f"({len(matches)} result{'s' if len(matches) != 1 else ''})")


def main():
    print("Fetching country data from the World Bank API...")

    countries = fetch_countries()

    # fetch_countries already printed why it failed, so exit quietly rather
    # than carrying on with nothing to search.
    if countries is None:
        print("Cannot continue without data. Exiting.")
        return

    print(f"Loaded {len(countries)} countries.")

    running = True

    while running:
        choice = show_menu()

        if choice == "1":
            term = input("Search: ").strip()

            if not term:
                print("Please enter something to search for.")
            else:
                print_results(search_by_name(countries, term))

        elif choice == "2":
            region = input("Region: ").strip()

            if not region:
                print("Please enter a region name.")
            else:
                print_results(filter_by_region(countries, region))

        elif choice == "3":
            print("Goodbye!")
            running = False

        else:
            # Covers empty input and anything that isn't 1-3, so a stray
            # keystroke re-shows the menu instead of crashing.
            print("Please choose 1, 2 or 3.")


main()
