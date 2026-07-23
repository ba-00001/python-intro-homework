"""Mini-project - Temperature converter (Fahrenheit to Celsius).

Does the conversion with the formula rather than a built-in converter, which
is what the assignment asked for.
"""

# float() not int(), because temperatures aren't whole numbers. Typing 98.6
# with int() would fail outright, and typing 72 with float() just gives 72.0,
# so float is the safer choice for both.
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

# The formula: subtract 32 first, then scale by 5/9.
# The brackets matter. Python does * and / before -, so without them this
# would calculate fahrenheit - (32 * 5 / 9), which is wrong. Checked with 72:
#   correct   -> (72 - 32) * 5 / 9 = 22.2
#   no bracket -> 72 - 17.8        = 54.2
celsius = (fahrenheit - 32) * 5 / 9

# :.1f rounds the display to one decimal place. It only changes how the number
# is printed - celsius itself still holds the full 22.22222... underneath.
print(f"{fahrenheit}°F is {celsius:.1f}°C.")
