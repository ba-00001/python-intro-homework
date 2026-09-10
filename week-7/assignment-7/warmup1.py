"""Warmup 1 - Read a Text File Line by Line.

Reads ../data/notes.txt and prints each line with its number.
"""

# The path is relative to where the script RUNS from, not where it lives, so
# this assumes I'm running it from inside assignment-7/. ".." steps up to
# week-7/, then into data/.
#
# "r" is read mode - the default, but writing it out makes the intent obvious
# next to the "w" modes used in the mini-project.
with open("../data/notes.txt", "r") as f:
    # `with` matters here: it closes the file automatically when the block
    # ends, including if something raises partway through. Without it I'd need
    # f.close() and it would get skipped on an error.
    #
    # Looping over the file object hands back one line at a time. It doesn't
    # load the whole file into memory, which is why this pattern still works on
    # a file too big to fit.
    #
    # enumerate(..., start=1) numbers the lines. Without start it would begin
    # at 0 and print "Line 0" for the first one.
    for line_number, line in enumerate(f, start=1):
        # Each line still carries the "\n" it ended with. print() adds its own
        # newline, so without .strip() every line would be double-spaced.
        print(f"Line {line_number}: {line.strip()}")
