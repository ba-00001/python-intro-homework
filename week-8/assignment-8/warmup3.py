"""Warmup 3 - Handle a Missing File.

../data/missing.txt does not exist. This catches that instead of showing a
traceback.
"""

FILENAME = "../data/missing.txt"

try:
    with open(FILENAME, "r") as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    # Without this, Python prints:
    #   Traceback (most recent call last):
    #     File "warmup3.py", line 10, in <module>
    #       with open(FILENAME, "r") as f:
    #   FileNotFoundError: [Errno 2] No such file or directory: '../data/missing.txt'
    #
    # That's accurate but it's aimed at me, not at whoever is running the
    # program. Catching it lets me say the same thing in a way that suggests
    # what to do about it.
    print('Error: "missing.txt" was not found. Please check the file path and try again.')
