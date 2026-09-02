"""Warmup 2 - Read a CSV with DictReader.

Reads ../data/students.csv and prints each student's name and score.
"""

import csv

with open("../data/students.csv", "r") as f:
    # DictReader reads the first row as the header and turns every later row
    # into a dict keyed by those headers. So instead of row[0] and row[2] -
    # which break the moment a column moves - I get row["name"] and
    # row["score"].
    reader = csv.DictReader(f)

    for row in reader:
        # Both values come back as STRINGS, even score. That's fine here
        # because I'm only printing them. The mini-project has to convert
        # amount with float() before doing maths on it.
        print(f"{row['name']}: {row['score']}")
