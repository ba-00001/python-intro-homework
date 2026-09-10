"""Warmup 4 - Read an error message, then fix the bug.

The bug is deliberate. I wrote the broken version first, ran it, read what
Python said, and then fixed it - rather than writing it correctly and
inventing an error afterwards.
"""

# The deliberate bug (commented out so this file still runs) was:
#
#     birth_year = input("What year were you born? ")
#     age = 2026 - birth_year
#     print(age)
#
# What the error message said:
#
#     Traceback (most recent call last):
#       File "warmup4.py", line 6, in <module>
#         age = 2026 - birth_year
#               ~~~~~^~~~~~~~~~~~
#     TypeError: unsupported operand type(s) for -: 'int' and 'str'
#
# How to read that, line by line:
#   - "Traceback (most recent call last)" just means an error report follows
#   - the File/line tells me exactly where to look: line 6 of warmup4.py
#   - the ~~~^~~~ underlines the part of the line that broke, so I don't have
#     to guess which bit of a long line is at fault
#   - the last line is the actual problem: TypeError, and it names both types
#     involved, 'int' and 'str'
#
# What caused it:
#     input() always hands back a string, even when digits get typed. So
#     birth_year was the text "1998", not the number 1998. Python has no rule
#     for subtracting text from a number, so it stopped rather than guessing
#     what I meant. That's a TypeError - the values are the wrong *type* for
#     the operation, as opposed to a ValueError where the type is right but
#     the contents aren't usable.
#
# How I fixed it:
#     Wrapped the input in int(), so "1998" becomes 1998 before the
#     subtraction runs. One function call in the right place.

birth_year = int(input("What year were you born? "))
age = 2026 - birth_year

print(f"You are approximately {age} years old.")
