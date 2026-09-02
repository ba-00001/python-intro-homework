"""Warmup 3 - Scope in Action.

Two examples of the same idea: a variable made inside a function does not
exist outside it, and return is how you get the value out.
"""

print("--- Example 1: the scope problem ---")


def make_secret():
    # secret is local to make_secret. It is created when the function runs and
    # thrown away when the function ends.
    secret = "I only exist inside this function"
    print(f"Inside the function, secret is: {secret}")


make_secret()

# Trying to read secret out here raises:
#   Traceback (most recent call last):
#     File "warmup3.py", line 22, in <module>
#       print(secret)
#   NameError: name 'secret' is not defined
#
# Commented out so the rest of the file can run. The error is accurate - by the
# time this line executes, make_secret has already finished and secret is gone.
# print(secret)

print("The function ran, but 'secret' is not available out here.")


print()
print("--- Example 2: return solves it ---")


def make_secret_properly():
    secret = "I was returned, so I survived"
    # Same local variable as before. The difference is that return sends a copy
    # of the value back to the caller before the local one disappears.
    return secret


# The returned value gets assigned to a name in this outer scope, so it sticks
# around. escaped_secret is a different variable that happens to hold the same
# string - the function's own `secret` is still gone.
escaped_secret = make_secret_properly()
print(f"Outside the function, escaped_secret is: {escaped_secret}")
