"""Warmup 4 - FizzBuzz from 1 to 30.

% is the modulo operator, giving the remainder after division. A remainder of
0 means it divides evenly, so number % 3 == 0 is how to ask "is this a
multiple of 3".
"""

# 1 to 30 inclusive, so the range has to stop at 31.
for number in range(1, 31):
    # Order is the whole exercise. The both-at-once case has to be tested
    # first, because 15 satisfies number % 3 == 0 as well - and since only the
    # first true branch runs, putting Fizz first means 15 prints "Fizz" and
    # FizzBuzz never appears at all. The most specific condition goes at the
    # top, the most general at the bottom.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        # Reaching here means it wasn't divisible by both, so it's 3 only.
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        # Not a multiple of either, so print the number itself. No quotes -
        # it's still an int here, not text.
        print(number)
