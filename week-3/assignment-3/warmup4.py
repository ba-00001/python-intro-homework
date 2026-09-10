"""Warmup 4 - Sign and parity, decided in two separate if/elif/else blocks.

Two blocks rather than one, because these are two independent questions about
the same number. A single if/elif chain can only ever run one branch, so it
could print the sign or the parity but not both.
"""

number = int(input("Enter a number: "))

# Block one: sign.
# Zero gets its own case because it's neither positive nor negative. Leaving
# it to fall into the negative branch would be wrong, and it's exactly the
# kind of edge case that's easy to miss when testing with 7 and -7 only.
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    # Nothing left but zero.
    print(f"{number} is zero.")

# Block two: parity.
# % is the modulo operator - it gives the remainder after division. 8 % 2 is
# 0, and 7 % 2 is 1, so a remainder of 0 means the number divides evenly.
# This works for negatives too: -7 % 2 is 1 in Python, so -7 comes out odd,
# which is what I wanted.
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
