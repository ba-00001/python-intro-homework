"""Mini-project - Expense Report Generator.

Reads ../data/expenses.csv, filters it to one category, and writes a formatted
report to a text file.

Written as build_report(category) rather than hardcoding "Food", which also
covers the optional extension - calling it with "Transport" writes
transport_report.txt in the same format. The graded run is the "Food" one at
the bottom.
"""

import csv
import os
from datetime import datetime

# Built with os.path.join so the separator is correct on any platform, rather
# than hardcoding "../data/expenses.csv".
DATA_PATH = os.path.join("..", "data", "expenses.csv")


def load_expenses(path):
    """Read the CSV into a list of dicts, with amount converted to float.

    Returns an empty list if the file isn't there.
    """
    # Step 1 of the assignment: check before opening. Without this guard,
    # open() on a missing file raises FileNotFoundError and the program dies
    # with a traceback instead of a message a person can act on.
    if not os.path.exists(path):
        print(f"Error: could not find {path}")
        return []

    expenses = []

    with open(path, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Everything DictReader returns is a string, including amount.
            # "54.30" + "35.00" would concatenate into "54.3035.00" rather than
            # adding, so the conversion has to happen before any maths.
            row["amount"] = float(row["amount"])
            expenses.append(row)

    return expenses


def filter_by_category(expenses, category):
    """Return only the rows whose category matches, ignoring case."""
    matches = []

    for expense in expenses:
        # .lower() on both sides so "food", "Food" and "FOOD" all match. The
        # data is consistently capitalised, but the comparison shouldn't depend
        # on that staying true.
        if expense["category"].lower() == category.lower():
            matches.append(expense)

    return matches


def total_amount(expenses):
    """Add up the amount field across a list of expense dicts."""
    total = 0.0

    for expense in expenses:
        total += expense["amount"]

    return total


def today_formatted():
    """Return today's date as 'Month DD, YYYY'."""
    today = datetime.now()
    # .day rather than the %d code, so the 2nd reads "September 2" and not
    # "September 02".
    return today.strftime(f"%B {today.day}, %Y")


def write_report(category, expenses, total, filename):
    """Write the report file: header line, one line per expense, total."""
    # "w" truncates the file and starts fresh. "a" would append, so re-running
    # the program would stack a second report underneath the first.
    with open(filename, "w") as f:
        f.write(f"{category} Expense Report — generated {today_formatted()}\n")

        for expense in expenses:
            # :.2f keeps money to two decimal places, so 35.0 writes as 35.00
            # instead of looking wrong.
            f.write(f"{expense['date']}: ${expense['amount']:.2f}\n")

        f.write(f"Total: ${total:.2f}\n")


def build_report(category):
    """Load, filter, total and write the report for one category."""
    expenses = load_expenses(DATA_PATH)

    # load_expenses already printed the reason, so just stop.
    if not expenses:
        return

    matches = filter_by_category(expenses, category)

    if not matches:
        print(f"No expenses found in category '{category}'.")
        return

    total = total_amount(matches)

    # "Food" -> "food_report.txt". Built from the category so the extension
    # works without a second filename to keep in sync.
    filename = f"{category.lower()}_report.txt"
    write_report(category, matches, total, filename)

    print(f"Wrote {filename} — {len(matches)} {category} expenses, ${total:.2f} total.")


build_report("Food")
