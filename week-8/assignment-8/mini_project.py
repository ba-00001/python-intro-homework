"""Mini-project - Defensive CSV Reader.

Reads ../data/messy_data.csv, which deliberately contains broken rows, and
produces a clean summary instead of crashing on the first bad one.

The whole point is where the try/except sits. One try around the entire loop
would abandon every remaining row the moment one failed - a single bad cell on
line 3 would cost me the eleven good rows after it. Handling each row inside
the loop means one bad row costs exactly one row.
"""

import csv
import os

DATA_PATH = os.path.join("..", "data", "messy_data.csv")


def parse_row(row):
    """Turn one raw CSV row into a clean dict.

    Raises ValueError if amount isn't numeric, KeyError if a column is absent.
    """
    # row["amount"] raises KeyError if the header had no amount column at all.
    # That's the KeyError the assignment asks about - a row that's simply
    # blank in that column gives an empty string instead, which is a
    # ValueError, so the two failures are genuinely different problems.
    name = row["name"]
    category = row["category"]
    amount = row["amount"]

    # A missing trailing column comes back as None rather than "". float(None)
    # raises TypeError, not ValueError, so it would escape the except clauses
    # below. Converting it to a ValueError here keeps all the "bad amount"
    # cases in one place.
    if amount is None:
        raise ValueError("could not convert None to float")

    # float("") and float("fifteen") both raise ValueError. Re-raising with my
    # own wording gives the report a consistent message - Python's own text is
    # "could not convert string to float: ''", which reads oddly in a list.
    try:
        amount = float(amount)
    except ValueError:
        raise ValueError(f"could not convert '{amount}' to float")

    return {"name": name, "category": category, "amount": amount}


def read_csv_defensively(path):
    """Return (clean_rows, skipped_notes, attempted) for the file at path."""
    clean = []
    skipped = []
    attempted = 0

    # The assignment asks for try/except FileNotFoundError rather than an
    # os.path.exists() check. Both work; this one is better here because it
    # can't go stale - exists() answers a question a moment before you open the
    # file, and something could delete it in between. Trying and catching asks
    # the question and does the work at the same time.
    try:
        f = open(path, "r")
    except FileNotFoundError:
        print(f"Error: could not find {path}. Check the path and try again.")
        return [], [], 0

    with f:
        reader = csv.DictReader(f)

        # start=1 so the numbers match the data rows, not the header. Row 3 in
        # the report is the third row of actual data.
        for row_number, row in enumerate(reader, start=1):
            attempted += 1

            # Guard before the try, per the assignment hint. DictReader doesn't
            # raise on extra columns - it quietly files them under the key None.
            # So this is not an exception to catch, it's a shape to check for,
            # and it has to happen first because such a row may still parse
            # "successfully" and hide the fact that it was malformed.
            if None in row:
                skipped.append(f"Row {row_number}: extra column detected — skipped")
                continue

            try:
                clean.append(parse_row(row))
            except ValueError as e:
                # `as e` captures the exception so the report can quote the
                # actual reason instead of just "something went wrong".
                skipped.append(f"Row {row_number}: ValueError — {e}")
            except KeyError as e:
                # e is the missing key name here, hence the quotes in the output.
                skipped.append(f"Row {row_number}: KeyError — missing column {e}")

    return clean, skipped, attempted


def print_report(clean, skipped, attempted):
    """Print the counts, the skipped rows and the clean data."""
    print("=== CSV Report ===")
    # Padded to a fixed width so the numbers line up in a column.
    print(f"{'Rows attempted:':<16}{attempted:>3}")
    print(f"{'Rows parsed:':<16}{len(clean):>3}")
    print(f"{'Rows skipped:':<16}{len(skipped):>3}")

    if skipped:
        print()
        print("Skipped rows:")
        for note in skipped:
            print(f"  {note}")

    if clean:
        print()
        print("Clean data:")
        for row in clean:
            print(f"  {row['name']} | {row['category']} | ${row['amount']:.2f}")


def main():
    clean, skipped, attempted = read_csv_defensively(DATA_PATH)

    # attempted is 0 only when the file was missing - read_csv_defensively
    # already explained why, so there's nothing to add.
    if attempted == 0:
        return

    print_report(clean, skipped, attempted)


main()
