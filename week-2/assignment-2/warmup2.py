"""Warmup 2 - Navigate with the CLI, then echo the user's date back.

Getting here without touching Finder was the actual exercise. The script
itself is just input() and an f-string.
"""

# Navigation commands I used:
# cd python-intro-homework     <- move into the repo folder
# ls                           <- list what's here, to see the week folders
# cd week-2/assignment-2       <- two levels at once, separated by /
# pwd                          <- print where I am, to confirm before making files
#
# cd .. goes back up one level, which is what I used when I overshot.

today = input("What is today's date? ")

# No conversion needed here. The date stays as text, and text is what input()
# already gives back - nothing to int() or float().
print(f"You said today is {today}.")
