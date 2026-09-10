"""Warmup 1 - Sum the integers from 1 to 100 with a for loop."""

# The running total has to exist BEFORE the loop starts. Creating it inside
# would reset it to 0 on every pass and the answer would come out as 100.
total = 0

# range(start, stop) includes the start and excludes the stop, so to get 1
# through 100 the stop has to be 101. Writing range(1, 100) is the obvious
# mistake and gives 4950 - only 50 short, so it looks plausible.
#
# This is a for loop rather than a while loop because the number of passes is
# known up front. It runs exactly 100 times and stops on its own.
for number in range(1, 101):
    total = total + number  # same as total += number

print(f"The sum of 1 to 100 is {total}.")
