# Assignment 8 — Errors & Debugging

Week 8 of Python Intro 26.3. Everything required for this assignment lives in
this folder.

## Submission links

| Field | Link |
|-------|------|
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/7 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Video script** | [VIDEO-SCRIPT.md](VIDEO-SCRIPT.md) |
| **Mindset Response** | [see below](#mindset-response--problem-solving) |

## Required files

| File | What it does |
|------|--------------|
| [warmup1.py](warmup1.py) | `while` loop re-asking until `float()` succeeds, catching `ValueError` |
| [warmup2.py](warmup2.py) | Division guarded by `except ZeroDivisionError` and `except ValueError`, success in `else` |
| [warmup3.py](warmup3.py) | `except FileNotFoundError` on a file that doesn't exist, with the traceback quoted in a comment |
| [warmup4.py](warmup4.py) | Imports `requests` from the venv and prints its version; `requirements.txt` pasted at the top |
| [requirements.txt](requirements.txt) | `pip freeze` output — `requests` plus its four dependencies |
| [mini_project.py](mini_project.py) | Defensive CSV Reader — per-row `try`/`except`, extra-column guard, summary report |

`.venv/` is gitignored — the environment is reproduced from `requirements.txt`
rather than committed.

## Virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests
pip freeze > requirements.txt
```

`requirements.txt` as generated:

```
certifi==2026.7.22
charset-normalizer==3.5.1
idna==3.19
requests==2.34.2
urllib3==2.7.0
```

Only `requests` was installed by hand. The other four came in as its
dependencies — which is the argument for committing the file instead of a note
saying "needs requests": it pins the whole tree at versions that actually ran.

## How to run

From this folder. Warmup 4 needs the venv active; the rest run on plain
`python3`:

```bash
python3 warmup1.py
python3 warmup2.py
python3 warmup3.py
python3 mini_project.py

source .venv/bin/activate
python3 warmup4.py
```

## Sample output

```
$ python3 warmup1.py
Enter a number: hello
That's not a valid number. Try again.
Enter a number: abc
That's not a valid number. Try again.
Enter a number: 42
You entered: 42.0

$ python3 warmup2.py
Enter the numerator: 10
Enter the denominator: 0
Can't divide by zero — please try a non-zero denominator.

$ python3 warmup2.py
Enter the numerator: 10
Enter the denominator: 4
10.0 ÷ 4.0 = 2.5

$ python3 warmup3.py
Error: "missing.txt" was not found. Please check the file path and try again.

$ python3 warmup4.py
requests version: 2.34.2

$ python3 mini_project.py
=== CSV Report ===
Rows attempted:  14
Rows parsed:      9
Rows skipped:     5

Skipped rows:
  Row 3: ValueError — could not convert '' to float
  Row 5: ValueError — could not convert 'not_a_number' to float
  Row 7: extra column detected — skipped
  Row 11: ValueError — could not convert '' to float
  Row 13: ValueError — could not convert 'fifteen' to float

Clean data:
  Alice | Food | $12.50
  Bob | Transport | $8.75
  David | Utilities | $45.00
  Frank | Transport | $22.30
  Hana | Utilities | $88.00
  Ivan | Food | $6.40
  Jess | Transport | $14.20
  Lena | Food | $9.80
  Nina | Utilities | $33.60
```

## Notes on the mini-project

**Why the `try` is inside the loop.** One `try` around the whole loop would
abandon every remaining row the moment one failed — a bad cell on row 3 would
cost the eleven good rows after it. Per-row handling means one bad row costs
exactly one row. That's the difference between crashing and degrading
gracefully.

**Why the extra-column check is a guard, not an `except`.** `csv.DictReader`
does not raise on a row with too many fields — it quietly files the surplus
under the key `None`. So there is no exception to catch. It has to be checked
for as a *shape* (`if None in row`) before the `try`, because such a row can
otherwise parse "successfully" and hide that it was malformed.

**Why `None` is converted to a `ValueError`.** A row missing its trailing
column yields `None`, and `float(None)` raises `TypeError` — which would slip
past `except ValueError` entirely. Raising it as a `ValueError` keeps every
"bad amount" case in one place.

## Requirements checklist

- [x] Warmup 1 — loop re-asks, `ValueError` caught, stops on a valid number
- [x] Warmup 2 — `ZeroDivisionError` caught with a friendly message instead of a crash
- [x] Warmup 3 — `FileNotFoundError` caught; helpful message, no traceback
- [x] Warmup 4 — venv created, `requests` installed, `requirements.txt` generated and pasted as a comment
- [x] Warmup 4 — prints the real installed version (`2.34.2`)
- [x] Mini-project — `try`/`except FileNotFoundError` before reading; prints an error and stops
- [x] Mini-project — read with `csv.DictReader`
- [x] Mini-project — each row processed in its own `try`/`except`
- [x] Mini-project — `ValueError` caught for non-numeric `amount`
- [x] Mini-project — `KeyError` caught for a missing column
- [x] Mini-project — extra-column rows guarded with `if None in row` before the `try`
- [x] Mini-project — successful rows collected into a list of dicts
- [x] Mini-project — summary prints attempted / parsed / skipped, the skipped reasons, and the clean data
- [ ] Video reflection recorded and linked above
- [x] Mindset response written

## Mindset Response — Problem Solving

> *"The most dangerous phrase is: 'We've always done it this way.'"*
> — Grace Hopper

### 1. Do you already have a problem solving process in place that you've found effective? If so, tell us about it!

I have one that works and one I actually do under pressure, and they aren't the
same. Worth being honest about that.

The one that works, when I hold myself to it:

**Reproduce it reliably first.** If I can't make it happen on demand I don't
understand it yet, and anything I "fix" is a guess I can't check.

**Say what I expected versus what happened**, in two sentences, out loud or
written down. The gap between those two sentences is nearly always the bug. This
is the step I skip most and the one that pays best — I've fixed two things this
course while writing them down, before running anything.

**Cut it down.** Delete or comment out until the bug vanishes or is the only
thing left. The mini-project this week was built this way: I got one row parsing,
then fed it a bad row on purpose, then the whole file.

**Change one thing at a time.** Two changes at once and a working program tells
me nothing about which mattered.

What I actually do when I'm frustrated is speed up — change something, re-run,
change something else, without a hypothesis. It feels like effort. It's how I
lose an hour and learn nothing, and it's the habit I'm trying to break by
writing the guess down first.

The other thing I've started doing is deciding what "handled" means before I
write the handler. This week that was a real decision: a bad row could stop the
program, or be silently dropped, or be counted and reported. Only the third one
tells the user their data has holes in it. Answering that before writing the
`except` was quicker than discovering it afterwards.

### 2. Have you observed others in the class solving problems differently than you do? What have you learned from their problem solving techniques?

The biggest difference I've noticed is how much slower other people are at the
start, in a way that turns out to be faster.

I go to the keyboard almost immediately. I've watched people in the Slack
channel and on screen shares who read the whole problem first, say out loud what
the program has to do, and only then start typing. My instinct treats that as
delay. It obviously isn't — they write less code and throw less of it away,
because they aren't discovering the requirements by bumping into them.

Two other things I've picked up:

**Asking in public, unfinished.** People post half-formed questions with the
error pasted in and get answers in minutes. I sit on mine until I can present it
tidily, which is exactly the behaviour that made Weeks 2 and 3 go in late. The
lesson isn't that they're braver. It's that a scruffy question early beats a
polished one three days later, and nobody thinks less of the scruffy one.

**Reading the docs before the search results.** I default to a search and land
on a blog post for a different Python version. Watching someone go to the actual
`csv` documentation first was mildly embarrassing — it's right there, it's
correct, and it's for the version I'm running. I used the standard library docs
directly for `csv.DictReader` and `os.path.join` this week and it was faster
than what I'd been doing.

The general shape of what I've learned from other people is the same in every
case: slow down at the start, be willing to look unfinished in front of others,
and go to the source. None of that is a technique so much as a temperament, and
mine is the impatient one, so it needs the practice.
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
