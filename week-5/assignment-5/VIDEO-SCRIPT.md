# Assignment 5 — Video Reflection Script

**Target length:** 3–5 minutes (this script runs ~4:30 spoken at a normal pace).
**Setup:** screen share of the editor and a terminal in `week-5/assignment-5/`,
webcam for the intro, the mindset section and the close.

**Before you hit record**

- Terminal cleared, already inside `week-5/assignment-5/`.
- Five editor tabs: the four warmups and `mini_project.py`. Also open
  `week-5/data/numbers.py` — you'll point at it and say you didn't modify it.
- Decide your live inputs:
  - `warmup2.py` → type **hello**, then **-3**, then **7**. Three inputs, because
    the two invalid ones fail in *different* ways and that's the point of the file.
  - `warmup3.py` → **Priya** (found at index 4), then run again with a name that
    isn't there.
  - `mini_project.py` → options **1**, **3** (search for 55), **4**, then **5**.
- Scroll `mini_project.py` to the bubble sort block before you start — that's
  where the most time goes.

---

## 0:00 – 0:25 · Intro (webcam)

> Hey, I'm Brian Bazurto, and this is my reflection for Assignment 5 of Python
> Intro 26.3 with Code the Dream. This week was iteration and algorithms — `for`
> loops, `while` loops, and writing minimum, maximum, search and sort **by hand**
> instead of calling `min()`, `max()` or `sorted()`. Four warmups and the Number
> Cruncher.

*(Switch to screen share.)*

---

## 0:25 – 0:55 · Warmup 1 — for loops, and the off-by-one

*(Open `warmup1.py` and run it.)*

> Sum 1 to 100. Two things I'd point at.

*(Highlight `total = 0` above the loop.)*

> The running total has to exist **before** the loop starts. Creating it inside
> would reset it to zero on every pass, and the answer would come out as 100 —
> which looks like a number, so you might not notice.

*(Highlight `range(1, 101)`.)*

> And `range(start, stop)` includes the start and **excludes** the stop, so to get
> 1 through 100 the stop has to be 101. Writing `range(1, 100)` is the obvious
> mistake and gives 4950 — only 50 short. Plausible enough that you'd believe it.
>
> This is a `for` loop and not a `while` because the number of passes is known up
> front. It runs exactly a hundred times and stops on its own.

---

## 0:55 – 1:35 · Warmup 2 — while loops, and two kinds of invalid

*(Open `warmup2.py`, then run it.)*

```bash
python3 warmup2.py
```

*(Type `hello`, then `-3`, then `7`.)*

> A `while` loop this time, because I've no idea how many bad answers someone
> will type. Could be none, could be five. There's no count to give a `for` loop,
> only a condition to keep going on.
>
> And notice I just typed two *different* kinds of wrong. `hello` — `int()` can't
> convert that at all, so it raises an error. `-3` — converts perfectly fine, it's
> just the wrong value. Two different failures, so there are **two separate
> guards**, not one.

*(Highlight the `try` / `except ValueError`.)*

> The `try`/`except` runs the risky line and catches the error instead of letting
> it stop the program. Without it, `hello` would crash out with a traceback rather
> than asking again.

*(Highlight `number = None`.)*

> And the starting value is `None` rather than 0, deliberately — because zero is
> itself an invalid answer I'd have to tell apart from "haven't asked yet". `None`
> makes the loop condition read as "keep going while I haven't got an answer".

---

## 1:35 – 2:05 · Warmup 3 — linear search by hand

```bash
python3 warmup3.py
```

*(Search for `Priya`, then run again with a name that isn't in the list.)*

> Linear search — no `.index()`, no `in`. The loop does the work, which is the
> point. Linear just means it checks one item after another from the start, with
> no shortcuts.

*(Highlight `found_at = -1`.)*

> Minus one is the "haven't found it" marker, and it has to be a value no real
> index can ever be. Starting at 0 would be a bug — I'd have no way to tell
> "found at the first position" from "never found it at all".

*(Highlight the `break`.)*

> `break` stops the loop immediately. Without it the loop keeps walking the rest
> of the list for no reason — and if a name appeared twice it would report the
> **last** one instead of the first.
>
> And the check happens after the loop, not inside it. Printing "not found" inside
> would fire once per non-matching name.

---

## 2:05 – 2:30 · Warmup 4 — FizzBuzz, where order is the whole exercise

*(Open `warmup4.py` and run it.)*

> FizzBuzz, 1 to 30. The order of the conditions is the entire exercise.

*(Highlight the first `if`.)*

> The both-at-once case has to be tested **first**, because 15 satisfies
> `number % 3 == 0` as well — and only the first true branch runs. So if Fizz went
> first, 15 would print "Fizz" and "FizzBuzz" would never appear at all. Most
> specific condition at the top, most general at the bottom.
>
> Same `%` as last week — remainder after division, so a remainder of zero means
> it divides evenly.

---

## 2:30 – 3:35 · Mini-project — Number Cruncher, and the clever bit (screen)

*(Point at `week-5/data/numbers.py`, then open `mini_project.py`.)*

> The numbers come from `week-5/data/numbers.py`, copied, original untouched.
>
> This is a menu loop — and this was the first thing I've written that behaved
> like an actual program instead of something that prints and quits.

*(Highlight the `choice` comparison.)*

> Small thing: I compare `choice` against the **string** `"1"`, with no `int()`
> conversion. That way typing `abc` hits the `else` and gets a polite message
> instead of crashing.

```bash
python3 mini_project.py
```

*(Choose 1.)*

> Minimum starts from `numbers[0]` rather than some arbitrary big number. That
> guarantees the answer is a value actually in the list, and it saves me having to
> guess a starting number bigger than anything here. Maximum is the same idea with
> the comparison flipped.

*(Choose 3, search for 55.)*

> Search converts the input with `int()` inside a `try`, because the list holds
> integers — `"42" == 42` is `False`, so without the conversion the search would
> silently never match.

*(Choose 4, then scroll to the bubble sort code.)*

> And this is the part I actually want to talk about.

*(Highlight `working = numbers[:]`.)*

> First, `[:]` is a full slice, which makes a **copy**. Sorting the original would
> mean the list stayed sorted for every later menu choice, and the program would
> quietly stop working on the data it was given.

*(Highlight the `swapped` flag.)*

> Second — the `swapped` flag. Bubble sort compares neighbouring pairs and swaps
> them if they're the wrong way round; after one full pass the largest value has
> been carried to the end, which is the "bubble". I got the swapping straight away
> and the **stopping** not at all — until it clicked that the algorithm works out
> for itself when it's finished. A whole pass with no swaps *is* what sorted means.
> Nothing counts the passes. The data decides when it's done. That's the first bit
> of code that struck me as clever rather than just working.

*(Highlight `range(len(working) - 1)`.)*

> And the minus one is because the comparison looks at `i` **and** `i + 1`.
> Without it, the last `i` points past the end and you get
> `IndexError: list index out of range`. Twenty numbers only have nineteen
> neighbouring pairs.

---

## 3:35 – 4:15 · Mindset — comfort with the unknown (webcam)

> The mindset question asked about "aha" moments and what's been hardest.
>
> The clearest aha was small: `input()` always gives you text back, even when the
> person typed a number. I got the `TypeError` and sat there annoyed, because I
> *had* typed a number. When it landed, a lot of other things landed with it —
> types are a real thing and not a technicality, and the error was an accurate
> description of what I'd asked for rather than Python being difficult.
>
> The other was the `swapped` flag I just walked through.
>
> Hardest, by a distance, was not the Python — it was Git and GitHub. I lost real
> time to not understanding that Assignment 2 moves into a fork of the class repo
> rather than the personal one from Week 1.
>
> And I'll be straight about the other thing: I fell behind in Weeks 2 and 3 and
> handed both in late. Not because they were hard. Because catching up takes
> longer than keeping up — which is obvious now and apparently needed learning the
> hard way.

---

## 4:15 – 4:30 · Close (webcam)

> So that's Assignment 5. Writing `min`, search and sort by hand made visible what
> the built-ins are doing, and the bubble sort stopping condition is the thing I'll
> remember. Everything's linked in the submission README. Thanks for watching.

---

## Delivery notes

- In warmup 2, type **both** kinds of invalid input. "hello" and "-3" failing
  differently is the reason the file has two guards, and it doesn't land if you
  only show one.
- Give the bubble sort a full minute. It's the highest-value explanation in this
  video — cut from warmup 1 or 4 if you need the time.
- Actually pick menu options live rather than describing them. The graded
  requirement is a working menu loop.
- Under 3:00 reads as thin; over 5:00 gets cut off. Time your first take.

---

## Video URL

Upload to YouTube (unlisted) or Loom, then paste the link here and in the two
other places it is needed.

**Video URL:** `VIDEO_URL_HERE`

| Also paste it into | Where |
| --- | --- |
| Submission README `URL2` row | [README.md](README.md) |
| Pull request description | [python-intro-homework#4](https://github.com/ba-00001/python-intro-homework/pull/4) |
| Course index video table | [main README](https://github.com/ba-00001/brian-bazurto-python/blob/main/README.md#video-reflections) |
