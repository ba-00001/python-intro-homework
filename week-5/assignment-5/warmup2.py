"""Warmup 2 - Keep asking until the user enters a positive integer.

A while loop rather than a for loop, because I've no idea how many bad
answers someone will type. Could be none, could be five. There's no count to
give a for loop, only a condition to keep going on.

Two different kinds of invalid input need handling, and they fail in
different ways:
  "hello" - int() can't convert it at all, so it raises an error
  "-3"    - converts fine, but it's the wrong value
So there are two separate guards below, not one.
"""

# None is the "nothing here yet" value. Using it as the starting state means
# the loop condition reads as "keep going while I haven't got an answer".
# Starting at 0 wouldn't work, since 0 is itself an invalid answer I'd have to
# tell apart from "not asked yet".
number = None

while number is None:
    answer = input("Enter a positive integer: ")

    # try/except: run the risky line, and catch the error instead of letting
    # it stop the program. Without this, typing "hello" would crash out with a
    # traceback rather than asking again.
    try:
        value = int(answer)
    except ValueError:
        # int() raises ValueError when the text isn't a whole number, which
        # catches both "hello" and "3.5".
        print("That's not a positive integer. Try again.")
        continue  # jump back to the top and re-ask

    # Only reached if the conversion worked. Now check the value itself.
    # <= 0 rather than < 0, because zero isn't positive either.
    if value <= 0:
        print("That's not a positive integer. Try again.")
        continue

    # Got past both guards, so it's valid. Assigning it makes the while
    # condition false, which is what ends the loop.
    number = value

print(f"Got it: {number}")
