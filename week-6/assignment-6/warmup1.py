"""Warmup 1 - Default Parameters.

One function, called three different ways, to see what a default parameter
actually buys you.
"""


# greeting has a default, so callers can leave it out. name does not, so it is
# always required. Defaults have to come after the non-default parameters -
# def greet(greeting="Hello", name) is a SyntaxError.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


# 1. Name only. greeting falls back to "Hello" because I never passed one.
greet("Alex")

# 2. Both arguments, positionally. The second value lands in greeting and
#    overrides the default.
greet("Alex", "Good morning")

# 3. Greeting passed by keyword. Same result as leaving it out here, but the
#    point is that naming the parameter means I don't have to remember the
#    order - greet(greeting="Hello", name="Alex") would work too.
greet("Alex", greeting="Hello")
