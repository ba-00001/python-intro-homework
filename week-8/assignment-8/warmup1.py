"""Warmup 1 - Validate Numeric Input.

Keeps asking until the user types something float() will accept.
"""

# Loop forever and break out on success. The alternative - a flag variable -
# works too, but there's only one way out of this loop so break says it more
# directly.
while True:
    raw = input("Enter a number: ")

    # The conversion goes INSIDE the try. Only the line that can actually raise
    # belongs in there - wrapping the input() call as well would hide a
    # different problem if one ever turned up on that line.
    try:
        number = float(raw)
    except ValueError:
        # float("hello") raises ValueError, which is exactly the case where the
        # right move is to ask again rather than crash.
        print("That's not a valid number. Try again.")
        continue  # skip the rest of the body and re-prompt

    # Only reachable when the conversion worked, so number definitely exists.
    print(f"You entered: {number}")
    break
