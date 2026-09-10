# Assignment 5 — Iteration & Algorithms

Week 5 of Python Intro 26.3. Everything required for this assignment lives in
this folder.

## Submission links

| Field | Link |
|-------|------|
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/4 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Mindset Response** | [see below](#mindset-response--comfort-with-the-unknown) |

## Required files

| File | What it does |
|------|--------------|
| [warmup1.py](warmup1.py) | Sums 1 to 100 with a `for` loop over `range()` → 5050 |
| [warmup2.py](warmup2.py) | `while` loop that re-asks until the user enters a positive integer, using `try`/`except` |
| [warmup3.py](warmup3.py) | Linear search written by hand — no `.index()`, no membership operator |
| [warmup4.py](warmup4.py) | FizzBuzz from 1 to 30, combined case checked first |
| [mini_project.py](mini_project.py) | Number Cruncher — menu loop with hand-written min, max, linear search, and bubble sort |

## Data source

The `numbers` list in `mini_project.py` is copied verbatim from
[`week-5/data/numbers.py`](../data/numbers.py). The file in `data/` is untouched.

## How to run

From this folder:

```bash
python3 warmup1.py
python3 warmup2.py
python3 warmup3.py
python3 warmup4.py
python3 mini_project.py
```

## Sample output

```
$ python3 warmup1.py
The sum of 1 to 100 is 5050.

$ python3 warmup2.py
Enter a positive integer: -3
That's not a positive integer. Try again.
Enter a positive integer: hello
That's not a positive integer. Try again.
Enter a positive integer: 7
Got it: 7

$ python3 mini_project.py
=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit
Choose an option (1-5): 4
Sorted: [3, 5, 8, 14, 17, 22, 29, 31, 40, 42, 47, 55, 59, 61, 66, 74, 78, 83, 86, 93]
```

## Requirements checklist

- [x] Warmup 1 — `for` loop over `range()`, prints 5050
- [x] Warmup 2 — `while` loop re-asks on negatives, zero, and non-numeric input
- [x] Warmup 3 — search implemented with a loop; `.index()` and `in` not used
- [x] Warmup 4 — FizzBuzz 1–30, divisible-by-both checked before the single cases
- [x] Mini-project — minimum found with a tracking loop, **not** `min()`
- [x] Mini-project — maximum found with a tracking loop, **not** `max()`
- [x] Mini-project — linear search loop with a not-found message
- [x] Mini-project — bubble sort with a `swapped` flag; `sorted()` and `.sort()` not used
- [x] Mini-project — menu redisplays until the user chooses Quit
- [ ] Video reflection recorded and linked above
- [x] Mindset response written

## Mindset Response — Comfort with the Unknown

> *"An entrepreneur is someone who jumps off a cliff and builds a plane on the
> way down."* — Reid Hoffman

### 1. So far in class, have you had any "aha" moments? What have you enjoyed the most? What has been the hardest?

The clearest one was small. `input()` always gives you text back, even when the
person typed a number. I got `TypeError: unsupported operand type(s) for -:
'int' and 'str'` and sat there annoyed, because I *had* typed a number. When it
landed, a lot of other things landed with it. Types are a real thing and not a
technicality, and the error was an accurate description of what I'd asked for
rather than Python being difficult about it.

The other one was the `swapped` flag in bubble sort. I got the swapping straight
away and the stopping part not at all, until it clicked that the algorithm works
out for itself when it's finished. A whole pass with no swaps is what sorted
means. Nothing is counting the passes. That's the first bit of code that struck
me as clever rather than just working.

Enjoyed most: the mini-projects, and particularly the menu loop in the Number
Cruncher. Watching a program keep going, take an instruction, do it and come
back for the next one was the first thing I'd written that behaved like an
actual program instead of something that prints and quits.

Hardest, by a distance, was not the Python. It was Git and GitHub. I lost real
time to not understanding that Assignment 2 moves into a fork of the class repo
rather than the personal one from Week 1, and went hunting for folders in a
repository that never had them. The language has been fine. It's everything
around the language I've struggled with.

### 2. What were you excited/worried about before class started?

Excited about finally getting some foundation under things I'd been building by
copying. I've put projects together out of examples before and they hold up
right until they don't, and I wanted to stop being stranded at that point.

Worried about time more than anything. Not whether I'd understand the material,
but whether I'd reliably find the hours for it. That turned out to be the right
thing to worry about — I fell behind in Weeks 2 and 3 and handed both in late.
Not because they were hard. Because catching up takes longer than keeping up,
which is obvious now and apparently needed learning the hard way.

I was also a bit worried about being the slowest person in the cohort. I've
mostly stopped keeping score on that. It never once helped.

### 3. How do you feel about what's still to come in this class and in your journey ahead?

Alright, with the caveat that the later weeks build on the earlier ones and I've
already shown I can slip. Functions and scope is next, and I can see from my own
code — the same block copied three times in the Number Cruncher — that I'm about
to be handed the fix for something I could already tell was wrong. That's a good
way to learn something.

What's changed most is how not knowing something feels. Early on, hitting
something I didn't understand felt like proof I shouldn't be here. Now it mostly
just feels like the job. The thing I don't get today is the same shape as the
thing I didn't get a couple of weeks ago and do now.

Further out I'm not planning much on purpose. Finish this properly, get one of
my own projects actually done rather than abandoned, and see what that opens up.
Building the plane on the way down is a slightly dramatic way to put it, but it
isn't far off, and I'd rather be doing that than still stood on the edge working
out whether to.

## All assignments

| # | Topic | Submission README | Pull request |
| --- | --- | --- | --- |
| 1 | Python Basics | [assignment-1](https://github.com/ba-00001/brian-bazurto-python/blob/assignment-1/assignment-1/README.md) | [brian-bazurto-python#1](https://github.com/ba-00001/brian-bazurto-python/pull/1) |
| 2 | CLI & Professional Environment | [week-2/assignment-2](https://github.com/ba-00001/python-intro-homework/blob/assignment-2/week-2/assignment-2/README.md) | [python-intro-homework#1](https://github.com/ba-00001/python-intro-homework/pull/1) |
| 3 | Control Flow | [week-3/assignment-3](https://github.com/ba-00001/python-intro-homework/blob/assignment-3/week-3/assignment-3/README.md) | [python-intro-homework#2](https://github.com/ba-00001/python-intro-homework/pull/2) |
| 4 | Core Data Structures | [week-4/assignment-4](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/README.md) | [python-intro-homework#3](https://github.com/ba-00001/python-intro-homework/pull/3) |
| 5 | Iteration & Algorithms | this page | [python-intro-homework#4](https://github.com/ba-00001/python-intro-homework/pull/4) |
