"""Warmup 3 - Linear search written by hand.

No .index() and no `in` membership test - the loop does the work, which is
the point of the exercise. Linear just means it checks one item after another
from the start, with no shortcuts.
"""

names = ["Jazmine", "Luis", "Sara", "Marcus", "Priya", "Devon"]

target = input("Enter a name to search for: ")

# -1 is the "haven't found it" marker. It has to be a value no real index can
# ever be, and since positions start at 0 and go up, -1 is safe. Starting at 0
# would be a bug - I'd have no way to tell "found at the first position" from
# "never found it at all".
found_at = -1

# range(len(names)) gives 0, 1, 2 ... up to one less than the length, which is
# exactly the valid positions. I need the position and not just the value
# here, because the position is what gets printed.
for position in range(len(names)):
    if names[position] == target:
        found_at = position
        # break stops the loop immediately. Without it the loop would keep
        # walking the rest of the list for no reason, and if a name appeared
        # twice it would report the last one instead of the first.
        break

# Checking after the loop rather than printing inside it. Printing "not found"
# inside would fire once per non-matching name.
if found_at == -1:
    print(f'"{target}" was not found in the list.')
else:
    print(f'Found "{target}" at index {found_at}.')
