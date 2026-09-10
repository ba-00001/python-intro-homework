"""Warmup 2 - Age categories, using `and` to check ranges."""

# int() straight away, because comparing text wouldn't do what I want. Strings
# compare alphabetically, so "9" > "17" is actually True - that wouldn't crash,
# it would just quietly hand back the wrong category, which is worse.
age = int(input("Enter your age: "))

# Each range needs both ends checked, which is what `and` is for - true only
# when the left side and the right side are both true. age >= 13 on its own
# would match a 40 year old as well.
if age >= 0 and age <= 12:
    category = "Child"
elif age >= 13 and age <= 17:
    category = "Teen"
elif age >= 18 and age <= 64:
    category = "Adult"
else:
    # 65 and up. No upper end to check, so no `and` needed here.
    category = "Senior"

print(f"You are a {category}.")
