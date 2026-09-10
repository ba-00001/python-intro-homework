"""Warmup 3 - Boolean expression practice.

Working these out on paper first and then running the file to check was the
useful part. The two I got wrong were both about precedence - which operator
Python resolves before the others.

Precedence here, highest first: not, then and, then or.
"""

# not applies to True on its own, not to the whole expression, so this reads
# as (not True) and False.
print(not True and False)  # not True is False; False and False is False

# The one that catches people out. and is resolved before or.
# If it went strictly left to right it would be (True or False) and False,
# which would give False instead of True.
print(True or False and False)  # and binds first: False and False is False; True or False is True

# Brackets are evaluated first, then not flips the result.
print(not (5 > 3))  # 5 > 3 is True; not True is False

# == tests equality, != tests "not equal". 4 != 4 is False because 4 IS 4.
print(10 == 10 and 4 != 4)  # 10 == 10 is True, but 4 != 4 is False; True and False is False

# or only needs one side to be true. The left side already is, so Python stops
# there and never bothers evaluating the right side.
print(not False or not True)  # not False is True; True or anything is True, so the right side never decides it
