# Assignment 3 — Control Flow

Week 3 of Python Intro 26.3. Everything required for this assignment lives in
this folder.

## Submission links

| Field | Link |
|-------|------|
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/2 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Mindset Response** | [see below](#mindset-response--motivation-and-mindset) |

## Required files

| File | What it does |
|------|--------------|
| [warmup1.py](warmup1.py) | Hardcoded score → letter grade with `if`/`elif`/`else` |
| [warmup2.py](warmup2.py) | Age from `input()` → Child / Teen / Adult / Senior, ranges checked with `and` |
| [warmup3.py](warmup3.py) | Five Boolean expressions, each with a comment explaining the result |
| [warmup4.py](warmup4.py) | Two separate `if`/`elif`/`else` blocks — one for sign (zero handled on its own), one for parity |
| [mini_project.py](mini_project.py) | Day Planner: 3 days × 3 times = 9 suggestions, case-insensitive, friendly fallbacks |

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
Score: 84
Grade: B

$ python3 warmup4.py
Enter a number: -7
-7 is negative.
-7 is odd.

$ python3 mini_project.py
What day is it? Saturday
What time of day? evening
Suggestion: Perfect night for a movie or trying a new recipe.

$ python3 mini_project.py
What day is it? blah
What time of day? morning
Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...
```

## Requirements checklist

- [x] Warmup 1 — all five grade bands covered
- [x] Warmup 2 — `int()` conversion, ranges checked with `and`
- [x] Warmup 3 — all five expressions printed, each line commented with the reason
- [x] Warmup 4 — sign and parity in two separate blocks, zero handled as its own case
- [x] Mini-project — 9 distinct suggestions, unknown day *and* unknown time handled, input normalised with `.strip().lower()`
- [ ] Video reflection recorded and linked above
- [x] Mindset response written

## Mindset Response — Motivation and Mindset

> *"Becoming is better than being."* — Carol Dweck

### 1. Why do you want to be a software developer/data engineer?

Because I've been making things for a while without really knowing how any of it
works, and I've got tired of that. I've got a handful of side projects — a
couple of small tools, a language learning thing I keep coming back to. They
mostly work. But they work the way something works when you've copied it
together out of examples, and the second something breaks in a way the example
didn't cover, I'm stuck, because I never had a picture in my head of what it was
doing.

I want to fix that. Not so I can write more code faster, but so that when it
goes wrong I'm working it out instead of guessing.

The other reason is that I like the work itself. There's a moment where it goes
from not working to working and you know exactly which side of it you're on.
Not many things are like that.

### 2. What do you plan to do with your skills after the class ends?

Short term, finish one of my own projects instead of leaving it at the 80% where
side projects usually die. Actually done, actually documented, not just working
on my machine.

Longer term I want to do this for a living. Python because the automation and
data side keeps throwing up problems I'd like to be able to solve, and because
it's a decent thing to build on rather than a dead end.

I'm aware that finishing a course isn't the same as being hireable, and that
eleven weeks is a start. What I want out of it is the fundamentals and the
habits — version control, reading errors properly, asking decent questions —
because those are what make the next year of teaching myself actually work
instead of going in circles.

### 3. Can you think of a time when a growth mindset helped you learn or achieve something new?

Guitar. Specifically the point about a year in where I nearly stopped.

I'd made quick progress at first and then flatlined. Chord changes I was messing
up in month three I was still messing up in month eleven. What I told myself was
that I'd found my ceiling — some people have an ear for it and I don't, and this
is as good as I get. Textbook fixed mindset, though at the time it just felt
like being realistic.

What changed it was being told to slow down. Not to run it more times, but to
play it with a metronome at a speed that was almost boring, get it clean, and
only then speed up. It felt like going backwards and I didn't enjoy it. A few
weeks later changes I'd been failing at for months were fine.

The useful part wasn't really about guitar. "I can't do this" turned out to mean
"I can't do this yet, at this speed, doing it this way", and all three of those
were things I could change. I've tried to bring that into this course. When
something isn't going in, I try to ask what's wrong with how I'm approaching it
rather than what's wrong with me.

## All assignments

| # | Topic | Submission README | Pull request |
| --- | --- | --- | --- |
| 1 | Python Basics | [assignment-1](https://github.com/ba-00001/brian-bazurto-python/blob/assignment-1/assignment-1/README.md) | [brian-bazurto-python#1](https://github.com/ba-00001/brian-bazurto-python/pull/1) |
| 2 | CLI & Professional Environment | [week-2/assignment-2](https://github.com/ba-00001/python-intro-homework/blob/assignment-2/week-2/assignment-2/README.md) | [python-intro-homework#1](https://github.com/ba-00001/python-intro-homework/pull/1) |
| 3 | Control Flow | this page | [python-intro-homework#2](https://github.com/ba-00001/python-intro-homework/pull/2) |
| 4 | Core Data Structures | [week-4/assignment-4](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/README.md) | [python-intro-homework#3](https://github.com/ba-00001/python-intro-homework/pull/3) |
| 5 | Iteration & Algorithms | [week-5/assignment-5](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/README.md) | [python-intro-homework#4](https://github.com/ba-00001/python-intro-homework/pull/4) |
