"""Warmup 1 - List operations, no loops.

All four answers come from indexing and slicing, so nothing here loops.
Positions in a list start at 0, not 1, which is the thing I keep having to
remind myself of.
"""

# Eight numbers, so the valid positions are 0 through 7.
numbers = [42, 17, 83, 5, 61, 29, 74, 40]

# Position 0 is the first item.
print(f"First: {numbers[0]}")

# Negative indexes count back from the end, so -1 is the last item. Better
# than numbers[7] because it keeps working if the list length changes.
print(f"Last: {numbers[-1]}")

# Slicing is [start:stop], and the stop is NOT included. So 2:6 gives
# positions 2, 3, 4 and 5 - four items, stopping just before 6. Getting caught
# out by that exclusive end is why my first attempt returned three numbers.
# With 8 items, the middle four are positions 2 to 5.
print(f"Middle: {numbers[2:6]}")

# [::-1] is [start:stop:step] with start and stop left blank, meaning the
# whole list, and a step of -1, meaning walk it backwards. It builds a new
# list rather than reordering this one, so `numbers` is untouched afterwards.
print(f"Reversed: {numbers[::-1]}")
