"""Warmup 1 - Letter grades with if/elif/else."""

score = 84

# Python checks these top to bottom and runs the FIRST one that's true, then
# skips the rest entirely - the later conditions never even get tested.
#
# Which is why the order has to run highest to lowest. If I'd put score >= 60
# first, an 84 would match it and come out as a D, because 84 really is >= 60.
# Going downwards means that by the time a condition is reached, everything
# above it has already been ruled out, so >= 80 here can only mean 80-89.
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    # else takes no condition. It catches anything that got this far, which
    # is everything under 60.
    grade = "F"

# Storing the letter and printing afterwards, rather than printing inside each
# branch, keeps the output in one place and the branches doing one job.
print(f"Score: {score}")
print(f"Grade: {grade}")
