"""Warmup 4 - Validation Function.

A function that answers one yes/no question and returns the answer, so the
decision about what to print stays out of it.
"""


def is_valid_score(score):
    """Return True if score is an int from 0 to 100 inclusive."""
    # Two separate things to check. isinstance catches the case where score
    # isn't a whole number at all - the string "85" or the float 85.5 both fail
    # here, which is what the assignment asked for.
    if not isinstance(score, int):
        return False

    # Chained comparison: reads as 0 <= score AND score <= 100. Inclusive at
    # both ends, so 0 and 100 are both valid.
    return 0 <= score <= 100


raw_score = input("Enter a score (0-100): ")

# input() always returns a string, and is_valid_score rejects strings on
# purpose. So I convert first - but only when the text is actually digits,
# otherwise int() would raise ValueError before my function got a look in.
# .lstrip("-") lets a negative like "-5" through to be converted and then
# correctly rejected as out of range.
if raw_score.lstrip("-").isdigit():
    score = int(raw_score)
else:
    # Not a number at all. Hand the raw text over and let isinstance reject it.
    score = raw_score

# The function returns True or False, so it can go straight into the if with no
# == True comparison needed.
if is_valid_score(score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")
