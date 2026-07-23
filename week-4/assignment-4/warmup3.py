"""Warmup 3 - Set operations on two lists of programming languages.

A set is unordered and holds no duplicates. That second part is the useful
bit here - it's what makes "everything from both lists, no repeats" a single
operator instead of a loop with a check inside it.
"""

# Starting as lists, because that's the normal way to write a few items down.
# "Python" and "SQL" appear in both, which is what makes the overlap
# operations show anything interesting.
my_languages = ["Python", "JavaScript", "HTML", "SQL"]
teammate_languages = ["Python", "SQL", "Java", "Go"]

# set() converts a list into a set. Any duplicates inside a single list would
# silently collapse into one entry at this point.
my_set = set(my_languages)
teammate_set = set(teammate_languages)

# | is union - everything in either set, each listed once. Both copies of
# "Python" become the single entry.
print(f"Union: {my_set | teammate_set}")

# & is intersection - only the ones in both. Python and SQL.
print(f"Intersection: {my_set & teammate_set}")

# - is difference, and the order matters here in a way it doesn't for the
# other two. my_set - teammate_set is "mine that they don't have". Flipping it
# would give theirs that I don't have, which is a different answer.
print(f"Difference (only mine): {my_set - teammate_set}")

# One thing worth knowing when reading the output: sets have no order, so
# these can print in a different sequence each run. That isn't a bug.
