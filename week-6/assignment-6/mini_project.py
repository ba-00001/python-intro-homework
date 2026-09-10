"""Mini-project - Number Cruncher, refactored into functions.

Same program as Assignment 5, reorganised so each operation is its own
function. The Week 5 file is untouched - this is a new file, so the git history
now holds both versions.

The algorithms themselves are unchanged: minimum, maximum, search and sort are
still written by hand, no min(), max(), sorted() or .sort(). What changed is
where they live. In Week 5 the search logic sat inside an elif branch and could
only ever be used by that branch. Now it is a function with a name, and the
menu just calls it.

The numbers list below is copied from week-5/data/numbers.py, which I left
untouched.
"""

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def find_min(numbers):
    """Return the smallest value in numbers, without using min()."""
    # Starting from numbers[0] rather than a guessed-large number guarantees
    # the answer is a value actually in the list.
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    # return, not print. The caller decides how to display it - which is what
    # lets find_min be reused somewhere that doesn't want output at all.
    return smallest


def find_max(numbers):
    """Return the largest value in numbers, without using max()."""
    # Identical to find_min with the comparison flipped.
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


def search(numbers, target):
    """Return the index of target in numbers, or -1 if it isn't there."""
    # Linear search: walk the positions and compare. -1 is the not-found
    # marker because it is never a valid index into a list I'm reading
    # forwards.
    for position in range(len(numbers)):
        if numbers[position] == target:
            return position  # return exits immediately, so no break needed
    # Only reached if the loop finished without returning.
    return -1


def bubble_sort(numbers):
    """Return a new sorted list, leaving the original untouched."""
    # [:] is a full slice, which copies. Sorting in place would mean the
    # caller's list came back reordered as a side effect, so every later menu
    # choice would be working on different data than it was given. The
    # assignment asks for a new list, and this is why that's the better shape.
    working = numbers[:]

    # Compare neighbouring pairs and swap the ones in the wrong order. After
    # one pass the largest value has been carried to the end - it "bubbles" up.
    #
    # swapped starts True only so the while runs at least once.
    swapped = True
    while swapped:
        # Reset before each pass. A whole pass with no swaps means every
        # neighbour is already in order, which is what sorted means - so the
        # flag stays False and the loop ends. Nothing counts the passes; the
        # data decides when it's done.
        swapped = False

        # len - 1 because the comparison reads i AND i + 1. Without the -1 the
        # last i would point past the end:
        #   IndexError: list index out of range
        for i in range(len(working) - 1):
            if working[i] > working[i + 1]:
                # Python evaluates the right-hand side first, so both values
                # move at once and no temporary variable is needed.
                working[i], working[i + 1] = working[i + 1], working[i]
                swapped = True

    return working


def show_menu():
    """Print the menu and return the user's raw choice as a string."""
    print()
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    # Returns text, not an int. Comparing against "1" means typing "abc" falls
    # through to the else instead of crashing on int(). .strip() so a stray
    # space doesn't stop "1 " from matching.
    return input("Choose an option (1-5): ").strip()


def main():
    """Run the menu loop, dispatching each choice to the right function."""
    running = True

    while running:
        choice = show_menu()

        if choice == "1":
            print(f"Minimum: {find_min(numbers)}")

        elif choice == "2":
            print(f"Maximum: {find_max(numbers)}")

        elif choice == "3":
            answer = input("Enter a number to search for: ").strip()
            # The list holds ints, so the input has to be converted before
            # comparing - "42" == 42 is False and the search would silently
            # never match.
            try:
                target = int(answer)
            except ValueError:
                print("That's not a whole number.")
                continue  # back to the menu

            found_at = search(numbers, target)

            # The printing lives here, not in search(). search() answers one
            # question - where is it - and main() decides what that means to
            # the user. That split is why search() could be reused by
            # something that wants to act on the index rather than print it.
            if found_at == -1:
                print("Not found")
            else:
                print(f"Found at index {found_at}")

        elif choice == "4":
            print(f"Sorted: {bubble_sort(numbers)}")
            # Proof the original survived - bubble_sort worked on a copy.
            print(f"Original is unchanged: {numbers}")

        elif choice == "5":
            print("Goodbye!")
            running = False

        else:
            print("Please choose a number from 1 to 5.")


# Nothing above this line ran anything except defining names. This is the one
# call that starts the program.
main()
