"""Mini-project - Student Roster Analyzer.

The students list below is copied from week-4/data/roster.py, which I left
untouched as instructed.

This is nested data: a LIST of students, where each student is a DICTIONARY.
The list keeps them in order, the dictionary keeps each student's fields
labelled. Getting at a value takes two steps - students[0] is a whole
dictionary, and students[0]["name"] is the actual text.

Four separate loops rather than one loop doing everything. One combined loop
would work and would be faster, but with eight students that saves nothing
measurable and each section here is easier to follow and check on its own.
"""

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# --- Top scorer -----------------------------------------------------------
# The assignment says not to use max(), so this tracks it by hand.
#
# Two variables, held outside the loop so they survive between passes. The
# pair is the whole trick - tracking only the score would leave me knowing 95
# and not who got it, so both get updated together or neither does.
#
# top_score starts at -1 rather than 0 because no real score can be below it,
# which guarantees the first student always wins the first comparison. If I'd
# started at 0 and every score were somehow negative, nothing would ever
# match and top_name would stay empty.
top_name = ""
top_score = -1

for student in students:
    # student is one dictionary from the list, so student["score"] is a number.
    if student["score"] > top_score:
        top_score = student["score"]
        top_name = student["name"]

# --- Class average --------------------------------------------------------
# Accumulate first, divide once at the end. Dividing inside the loop would
# give a running average, which isn't the same number.
total_score = 0

for student in students:
    total_score = total_score + student["score"]

# len() gives the number of students, so this doesn't hardcode 8 and stays
# correct if the roster changes.
class_average = total_score / len(students)

# --- Unique subjects ------------------------------------------------------
# Starting from an empty set. A set throws away repeats on its own, so adding
# "Python" three times still leaves one entry - no "have I already got this?"
# check needed, which is exactly why a set is the right tool here rather than
# a list.
subjects = set()

for student in students:
    subjects.add(student["subject"])

# --- High scorers ---------------------------------------------------------
# A list this time, because I want every name that qualifies, in roster order.
high_scorers = []

for student in students:
    # Strictly above 75, so a 75 exactly would not make the cut.
    if student["score"] > 75:
        high_scorers.append(student["name"])

# --- Report ---------------------------------------------------------------
print(f"Top scorer: {top_name} ({top_score})")

# The real average is 650 / 8 = 81.25 exactly. .1f has to round a value
# sitting halfway, and Python rounds those to the nearest even digit, so this
# prints 81.2 rather than 81.3. Took me a while to work out that wasn't a bug.
print(f"Class average: {class_average:.1f}")

# Sets have no order, so the three subjects can print in a different sequence
# on different runs.
print(f"Subjects offered: {subjects}")
print(f"High scorers: {high_scorers}")
