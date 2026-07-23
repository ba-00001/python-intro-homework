"""Warmup 2 - Dictionary operations.

A dictionary stores labelled values, so I reach for one when a single thing
has several different attributes. Position means nothing here - asking for
"item 1" of a student wouldn't mean anything.
"""

# Each entry is key: value. Note the value of "subjects" is itself a list -
# a dictionary can hold any type, including another collection.
student = {
    "name": "Alex Rivera",
    "grade": 11,
    "subjects": ["Python", "Algebra", "Biology"],
}

# .items() hands back both the key and its value on each pass, which is why
# the loop takes two variables. Looping over the dictionary directly would
# only give the keys, and I'd have to look each value up separately.
for key, value in student.items():
    print(f"{key}: {value}")

# Assigning to a key that doesn't exist yet CREATES it. There's no .add() for
# dictionaries - the same syntax that changes an existing value also adds a
# new one, which surprised me. The new key goes on the end.
student["graduated"] = False

print()
# Printing the whole dictionary shows it as Python would write it, quotes and
# braces included, which is handy for confirming "graduated" really landed.
print(student)
