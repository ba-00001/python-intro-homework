"""Warmup 3 - Use the os Module.

Three things the os module does: tell me where I am, check whether a file
exists, and build a path safely.
"""

import os

# 1. Where is Python actually running from? This is the answer to why
#    "../data/notes.txt" works from one folder and not another - relative paths
#    are resolved from HERE, not from wherever the .py file is saved.
print(f"Current working directory: {os.getcwd()}")

# 2. Check before opening. os.path.exists() returns a plain True/False and
#    never raises, so it's a cheap guard against FileNotFoundError. The
#    mini-project uses exactly this before it tries to read the CSV.
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# 3. Build the path from its parts instead of typing the separators. os.path.join
#    inserts the right separator for the operating system - "/" here, "\" on
#    Windows - so the same code works on a machine that isn't mine. Gluing
#    strings together with "/" would only ever be right on one platform.
path = os.path.join("..", "data", "expenses.csv")
print(f"Joined path: {path}")
