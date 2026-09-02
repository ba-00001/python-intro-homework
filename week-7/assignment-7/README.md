# Assignment 7 — Text Data & Modules

Week 7 of Python Intro 26.3. Everything required for this assignment lives in
this folder.

## Submission links

| Field | Link |
|-------|------|
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/6 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Mindset Response** | [see below](#mindset-response--debugging) |

## Required files

| File | What it does |
|------|--------------|
| [warmup1.py](warmup1.py) | Reads `../data/notes.txt` in a `with` block, numbering lines with `enumerate`, `.strip()` on each |
| [warmup2.py](warmup2.py) | `csv.DictReader` over `../data/students.csv`, printing name and score by header name |
| [warmup3.py](warmup3.py) | `os.getcwd()`, `os.path.exists()` guard, and `os.path.join()` |
| [warmup4.py](warmup4.py) | `datetime.now()` + `.strftime()` formatted as `Month D, YYYY` |
| [mini_project.py](mini_project.py) | Expense Report Generator — guard, `DictReader`, `float()` conversion, filter, total, file write |
| [food_report.txt](food_report.txt) | The output produced by `mini_project.py` |

## Data source

Read from [`week-7/data/`](../data/) via `../data/<filename>`, as the
assignment specifies. Those files are untouched — the program only reads them,
and writes its output into this folder.

## How to run

From this folder (the relative paths assume it):

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
Line 1: Python is great for working with files.
Line 2: You can read, write, and append text.
Line 3: The 'with' statement keeps things clean.
Line 4: Always close your files when you're done.

$ python3 warmup2.py
Jazmine: 88
Luis: 74
Sara: 91
Marcus: 83
Priya: 95

$ python3 warmup3.py
Current working directory: /Users/.../week-7/assignment-7
expenses.csv found.
Joined path: ../data/expenses.csv

$ python3 warmup4.py
Today is September 2, 2026.

$ python3 mini_project.py
Wrote food_report.txt — 5 Food expenses, $185.65 total.
```

`food_report.txt`:

```
Food Expense Report — generated September 2, 2026
2024-03-01: $54.30
2024-03-03: $8.75
2024-03-05: $42.00
2024-03-07: $67.20
2024-03-09: $13.40
Total: $185.65
```

## Optional extension

The mini-project is written as `build_report(category)` rather than with
`"Food"` hardcoded, so the optional extension is covered by the same code. The
filename is derived from the category, so there is no second name to keep in
sync:

```python
build_report("Transport")   # writes transport_report.txt
```

```
Transport Expense Report — generated September 2, 2026
2024-03-02: $35.00
2024-03-06: $18.50
Total: $53.50
```

Only `food_report.txt` is committed, since that's the graded output.

## Requirements checklist

- [x] Warmup 1 — `with` block, line-by-line, numbered, `.strip()` applied
- [x] Warmup 2 — `csv.DictReader`, fields accessed by header name
- [x] Warmup 3 — all three parts: `os.getcwd()`, `os.path.exists()`, `os.path.join()`
- [x] Warmup 4 — `datetime.now()` and `.strftime()`
- [x] Mini-project — `os.path.exists()` checked before opening; prints an error and stops if missing
- [x] Mini-project — read with `csv.DictReader` into a list of dicts
- [x] Mini-project — `amount` converted with `float()` before any maths
- [x] Mini-project — filtered to `category == "Food"`
- [x] Mini-project — total calculated
- [x] Mini-project — report written with header line, one line per expense, and total to 2dp
- [x] `food_report.txt` committed to show the output
- [x] Optional extension — works for any category
- [ ] Video reflection recorded and linked above
- [x] Mindset response written

## Mindset Response — Debugging

> *"Debugging is twice as hard as writing the code in the first place."*
> — Brian Kernighan

### 1. When asked to think about debugging, what are the first 3 adjectives that jump to mind?

**Humbling. Repetitive. Clarifying.**

Humbling because the bug is nearly always mine, and it's usually not clever. I
have lost hours to a comparison against a string when the value was an int. The
computer was right and I was wrong, every time so far.

Repetitive because most of my bugs are the same three bugs. Wrong type, wrong
scope, wrong path. Almost every problem I've had in this course has been one of
those wearing a different hat. The `TypeError` in Week 2 and the `NameError` I
deliberately triggered in Week 6 are the same mistake at different addresses:
assuming a value is something it isn't.

Clarifying because a bug is the only time the code tells you what it actually
does rather than what you meant. Everything I properly understand about
`input()` I learned from it breaking, not from reading that it returns a string.

### 2. What are some debugging practices you've already found helpful and one or two you would like to try when you next encounter bugs in your code?

Helpful so far:

**Reading the whole traceback, bottom line first.** For a while I skimmed for
red text and started guessing. The last line names the error type and the lines
above it say which file and which line. `unsupported operand type(s) for -: 'int'
and 'str'` is not a complaint, it's the answer.

**Printing the type, not just the value.** `print(x)` shows `42`. `print(type(x))`
shows `<class 'str'>`, which is the actual bug. Assignment 1 had me printing
types next to values and at the time it felt like busywork. It's now the first
thing I do.

**Writing the question out.** I've fixed two bugs while drafting the message
asking about them. Stating what I was trying to do separately from what
happened put the mismatch right next to itself.

**Shrinking it.** Cutting the file down until the bug either disappears — which
tells me where it lives — or is the only thing left.

Two I want to try:

**An actual debugger, with breakpoints.** I debug entirely with `print()`, which
means adding lines, re-running, and deleting them again. Stepping through and
inspecting variables at a paused line would tell me more, and I'd stop leaving
stray prints behind. `breakpoint()` is in the standard library and I have no
excuse.

**Writing the hypothesis down before testing it.** Right now, when I'm stuck I
speed up — change something, re-run, change something else. That's how I lose an
hour without learning anything. One line first: *I think X is happening; if so,
Y will be true.* Then check Y. It's slower per attempt and I suspect much faster
overall, which is the same lesson the metronome taught me about guitar.
## All assignments

| # | Topic | Submission README | Pull request |
| --- | --- | --- | --- |
| 1 | Python Basics | [assignment-1](https://github.com/ba-00001/brian-bazurto-python/blob/assignment-1/assignment-1/README.md) | [brian-bazurto-python#1](https://github.com/ba-00001/brian-bazurto-python/pull/1) |
| 2 | CLI & Professional Environment | [week-2/assignment-2](https://github.com/ba-00001/python-intro-homework/blob/assignment-2/week-2/assignment-2/README.md) | [python-intro-homework#1](https://github.com/ba-00001/python-intro-homework/pull/1) |
| 3 | Control Flow | [week-3/assignment-3](https://github.com/ba-00001/python-intro-homework/blob/assignment-3/week-3/assignment-3/README.md) | [python-intro-homework#2](https://github.com/ba-00001/python-intro-homework/pull/2) |
| 4 | Core Data Structures | [week-4/assignment-4](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/README.md) | [python-intro-homework#3](https://github.com/ba-00001/python-intro-homework/pull/3) |
| 5 | Iteration & Algorithms | [week-5/assignment-5](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/README.md) | [python-intro-homework#4](https://github.com/ba-00001/python-intro-homework/pull/4) |
| 6 | Functions & Scope | [week-6/assignment-6](https://github.com/ba-00001/python-intro-homework/blob/assignment-6/week-6/assignment-6/README.md) | [python-intro-homework#5](https://github.com/ba-00001/python-intro-homework/pull/5) |
| 7 | Text Data & Modules | [week-7/assignment-7](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/README.md) | [python-intro-homework#6](https://github.com/ba-00001/python-intro-homework/pull/6) |
| 8 | Errors & Debugging | [week-8/assignment-8](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/README.md) | [python-intro-homework#7](https://github.com/ba-00001/python-intro-homework/pull/7) |
| 9 | External Libraries & APIs | [week-9/assignment-9](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/README.md) | [python-intro-homework#8](https://github.com/ba-00001/python-intro-homework/pull/8) |
| 10 | Final Project I | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
| 11 | Final Project II | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
