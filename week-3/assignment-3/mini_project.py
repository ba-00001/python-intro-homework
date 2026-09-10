"""Mini-project - Day Planner.

Asks for a day of the week and a time of day, then suggests an activity.
Covers three days times three times of day, which is nine combinations, and
falls back to a friendly message when either answer isn't recognised.
"""

# Pulled out as constants so the wording lives in one place. If I add a day to
# the checks below I only have to update this string once, instead of hunting
# for it inside a print.
KNOWN_DAYS = "Monday, Tuesday, Wednesday..."
KNOWN_TIMES = "morning, afternoon, or evening"

# Both questions get asked before anything is checked, which matches the
# example output - it asks for the day and the time, then complains.
day = input("What day is it? ")
time_of_day = input("What time of day? ")

# Normalising the input so capitalisation doesn't matter.
#   .strip() removes spaces at either end, in case of a stray space
#   .lower() makes it all lowercase, so "Monday", "monday" and "MONDAY" match
# They chain because .strip() hands back a new string, which .lower() then
# works on. Everything below only ever has to compare against lowercase.
day = day.strip().lower()
time_of_day = time_of_day.strip().lower()

# The two unrecognised cases are checked FIRST, before any real combination.
# Doing it this way means the nine branches below can assume both answers are
# valid, instead of every single one needing its own else for bad input.
if day not in ("monday", "tuesday", "saturday"):
    print(f"Sorry, I don't recognize that day. Try: {KNOWN_DAYS}")
elif time_of_day not in ("morning", "afternoon", "evening"):
    print(f"Sorry, I don't recognize that time of day. Try: {KNOWN_TIMES}")

# From here down the day is definitely one of the three I handle. The outer
# chain picks the day, and the inner chain picks the time within that day -
# three days times three times is the nine combinations required.
elif day == "monday":
    if time_of_day == "morning":
        print("Suggestion: Plan the week — write down your three biggest tasks.")
    elif time_of_day == "afternoon":
        print("Suggestion: Clear your inbox while your focus is still fresh.")
    else:
        # Only "evening" can reach here, since anything else was caught above.
        print("Suggestion: Read one chapter of the Python textbook and stop early.")
elif day == "tuesday":
    if time_of_day == "morning":
        print("Suggestion: Morning Python class — great time to focus!")
    elif time_of_day == "afternoon":
        print("Suggestion: Rework the exercises you got wrong in class.")
    else:
        print("Suggestion: Study group — explain one concept out loud to someone.")
else:
    # Same reasoning - the only day left is Saturday.
    if time_of_day == "morning":
        print("Suggestion: Long walk before the day fills up.")
    elif time_of_day == "afternoon":
        print("Suggestion: Build something small just for fun — no deadline.")
    else:
        print("Suggestion: Perfect night for a movie or trying a new recipe.")
