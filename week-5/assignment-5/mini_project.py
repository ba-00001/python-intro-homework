"""Mini-project - Number Cruncher.

A menu-driven program. The numbers list below is copied from
week-5/data/numbers.py, which I left untouched.

Minimum, maximum, search and sort are all written by hand - no min(), max(),
sorted() or .sort() - which is the point of the assignment. Writing them out
makes visible what those built-ins are doing internally.
"""

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

# Flag controlling the menu loop. Setting it False on quit is what ends the
# program, rather than break - either works, this just reads more clearly next
# to a menu.
running = True

while running:
    print()
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    # .strip() so a stray space doesn't stop "1 " from matching. Comparing
    # against the STRING "1", because input() gives back text and no int()
    # conversion happens here - that way typing "abc" hits the else instead of
    # crashing.
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        # Start from the first item rather than some arbitrary big number.
        # That guarantees the answer is a value actually in the list, and it
        # avoids having to guess a starting number bigger than anything here.
        smallest = numbers[0]
        for number in numbers:
            # Keep whichever is smaller. Nothing to do when it isn't.
            if number < smallest:
                smallest = number
        print(f"Minimum: {smallest}")

    elif choice == "2":
        # Same idea, comparison flipped.
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        print(f"Maximum: {largest}")

    elif choice == "3":
        answer = input("Enter a number to search for: ").strip()
        # The list holds ints, so the input has to be converted before
        # comparing - "42" == 42 is False, and the search would silently never
        # match. try/except catches text that won't convert.
        try:
            target = int(answer)
        except ValueError:
            print("That's not a whole number.")
            continue  # back to the menu

        # Same linear search as warmup3, with -1 as the not-found marker.
        found_at = -1
        for position in range(len(numbers)):
            if numbers[position] == target:
                found_at = position
                break

        if found_at == -1:
            print(f"{target} was not found in the list.")
        else:
            print(f"Found {target} at index {found_at}.")

    elif choice == "4":
        # [:] is a full slice, which makes a COPY. Sorting the original would
        # mean the list stayed sorted for every later menu choice, and the
        # program would quietly stop working on the data it was given.
        working = numbers[:]

        # Bubble sort. It compares neighbouring pairs and swaps them if
        # they're the wrong way round. After one full pass the largest value
        # has been carried to the end - it "bubbles" up, hence the name.
        #
        # swapped starts True purely so the while loop runs at least once.
        swapped = True
        while swapped:
            # Reset before each pass. If this pass makes no swaps at all, the
            # flag stays False, the while ends, and that's the signal the list
            # is sorted - every neighbour is already in order. Nothing counts
            # the passes; the data decides when it's done.
            swapped = False

            # len - 1 because the comparison looks at i AND i + 1. Without the
            # -1, the last i would make i + 1 point past the end:
            #   IndexError: list index out of range
            # 20 numbers only have 19 neighbouring pairs.
            for i in range(len(working) - 1):
                if working[i] > working[i + 1]:
                    # Python swaps both sides at once, so no temporary
                    # variable is needed. The right-hand side is evaluated
                    # before either assignment happens.
                    working[i], working[i + 1] = working[i + 1], working[i]
                    swapped = True

        print(f"Sorted: {working}")

    elif choice == "5":
        print("Goodbye!")
        running = False  # ends the while loop

    else:
        # Anything that isn't 1-5, including empty input.
        print("Please choose a number from 1 to 5.")
