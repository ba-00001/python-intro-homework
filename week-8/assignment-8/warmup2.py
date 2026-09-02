"""Warmup 2 - Safe Division.

Divides two numbers, catching the two things that can realistically go wrong.
"""

numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

try:
    # Both conversions and the division are in one block because any of the
    # three failing means the same thing to the user: I can't do this sum.
    a = float(numerator)
    b = float(denominator)
    result = a / b
except ZeroDivisionError:
    # Dividing by zero isn't a typo the user can be told to fix by retyping the
    # same thing - it has no answer. So it gets its own message.
    print("Can't divide by zero — please try a non-zero denominator.")
except ValueError:
    # Catching this separately, and second, because the fix is different: the
    # input wasn't a number at all.
    #
    # The order of except blocks matters when one exception is a subclass of
    # another. These two are siblings, so either order works here - but keeping
    # the most specific case first is the habit worth having.
    print("Both values need to be numbers.")
else:
    # Runs only when the try block raised nothing. Putting the success case in
    # else rather than at the end of try makes it obvious this line is not
    # itself being guarded.
    print(f"{a} ÷ {b} = {result}")
