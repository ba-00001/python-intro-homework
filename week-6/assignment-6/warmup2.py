"""Warmup 2 - Functions that Return Values.

Two conversions in both directions. These functions return their answer
instead of printing it, which is what lets me drop the result into an f-string
at the call site.
"""


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    # return hands the number back to whoever called this. If I used print()
    # here the function would show the number but evaluate to None, and
    # f"{celsius_to_fahrenheit(0)}" would print "None".
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    # Brackets matter: (f - 32) has to happen before multiplying by 5/9.
    # f - 32 * 5 / 9 would subtract about 17.8 instead.
    return (f - 32) * 5 / 9


# Because the functions return values, the maths happens inside the {} and the
# :.1f rounds the result for display.
print(f"0°C = {celsius_to_fahrenheit(0):.1f}°F")
print(f"100°C = {celsius_to_fahrenheit(100):.1f}°F")
print(f"72°F = {fahrenheit_to_celsius(72):.1f}°C")
