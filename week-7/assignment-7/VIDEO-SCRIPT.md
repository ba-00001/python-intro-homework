# Assignment 7 — Video Reflection Script

**Target length:** 3–5 minutes (this script runs ~4:20 spoken at a normal pace).
**Setup:** screen share of the editor, a terminal in `week-7/assignment-7/`, and
a file browser or editor sidebar showing `week-7/data/`. Webcam for the intro,
the mindset section and the close.

**Before you hit record**

- Terminal cleared, inside `week-7/assignment-7/`. **This matters more this week
  than any other** — every path in these files is relative, so running from the
  wrong folder breaks them. That's a talking point, not an accident.
- Editor tabs: the four warmups, `mini_project.py`, and `../data/expenses.csv`.
- **Delete `food_report.txt` before recording** so you can write it live and show
  it appearing. It's committed in the repo, so restore it afterwards with
  `git checkout food_report.txt` if you want the committed copy back.
- Have `warmup3.py`'s `os.getcwd()` output in mind — you'll use it to explain
  relative paths.

---

## 0:00 – 0:25 · Intro (webcam)

> Hey, I'm Brian Bazurto, and this is my reflection for Assignment 7 of Python
> Intro 26.3 with Code the Dream. This week was text data and modules — reading
> files, `csv.DictReader`, and the `os` and `datetime` modules — building up to an
> Expense Report Generator that reads a CSV and writes a formatted text file.

*(Switch to screen share.)*

---

## 0:25 – 1:00 · Warmup 1 — reading a file line by line

*(Open `warmup1.py` and run it.)*

> Warmup 1 reads `../data/notes.txt` and prints each line with its number. Three
> details in four lines of code.

*(Highlight `with open(...)`.)*

> `with` closes the file automatically when the block ends — including if
> something raises partway through. Without it I'd need `f.close()`, and it'd get
> skipped on an error.

*(Highlight the `for` line.)*

> Looping over the file object hands back one line at a time. It doesn't load the
> whole file into memory, which is why this same pattern still works on a file too
> big to fit. And `enumerate(f, start=1)` numbers them — without `start` it'd
> begin at zero and print "Line 0" for the first one.

*(Highlight `.strip()`.)*

> And `.strip()`, because each line still carries the `\n` it ended with. `print`
> adds its own newline, so without stripping, every line comes out double-spaced.

---

## 1:00 – 1:30 · Warmup 2 — DictReader

*(Open `../data/students.csv` briefly, then `warmup2.py`, then run it.)*

> `csv.DictReader` reads the first row as the header and turns every later row
> into a dictionary keyed by those headers. So instead of `row[0]` and `row[2]` —
> which break the moment somebody moves a column — I get `row["name"]` and
> `row["score"]`.

*(Point at `row['score']`.)*

> One thing to flag now because it bites in the mini-project: **every value comes
> back as a string**, including score. That's fine here because I'm only printing.
> It is not fine the moment you do arithmetic.

---

## 1:30 – 2:05 · Warmup 3 — the `os` module, and why paths break

*(Open `warmup3.py` and run it.)*

> Three things the `os` module does for me.

*(Point at the `os.getcwd()` output in the terminal.)*

> First — where Python is actually running from. This is the answer to why
> `../data/notes.txt` works from one folder and not another. Relative paths are
> resolved from **here**, the working directory, not from wherever the `.py` file
> is saved. That one sentence explains most of my file-not-found problems.
>
> Second, `os.path.exists()` returns a plain `True` or `False` and never raises,
> so it's a cheap guard against `FileNotFoundError`. The mini-project uses exactly
> this before it opens the CSV.

*(Highlight `os.path.join`.)*

> Third, `os.path.join` builds the path from its parts and inserts the right
> separator for the operating system — a forward slash here, a backslash on
> Windows. Gluing strings together with `"/"` would only ever be right on one
> platform.

---

## 2:05 – 2:25 · Warmup 4 — `datetime`, and one formatting choice

*(Open `warmup4.py` and run it.)*

> `from datetime import datetime` — I pull the class out of the module so I write
> `datetime.now()` rather than `datetime.datetime.now()`. The module and the class
> share a name, which is confusing exactly once.
>
> `strftime` turns a datetime into text with format codes: `%B` is the full month
> name, `%Y` the four-digit year.

*(Highlight `today.day`.)*

> The day goes in with `today.day` and **not** the `%d` code, on purpose. `%d`
> zero-pads, so the 2nd of the month comes out "September 02". Using `.day` gives
> "September 2", which is how a date is actually written.

---

## 2:25 – 3:35 · Mini-project — Expense Report Generator (screen)

*(Open `../data/expenses.csv`, then `mini_project.py`.)*

> The mini-project reads that CSV, filters it to one category, totals it, and
> writes a formatted report to a text file.

*(Point at the `build_report(category)` signature.)*

> First decision: I wrote it as `build_report(category)` rather than hardcoding
> "Food". That also covers the optional extension for free — calling it with
> "Transport" writes `transport_report.txt` in the same format, with no second
> filename to keep in sync, because the filename is built from the category.

*(Scroll to `load_expenses`, highlight the `os.path.exists` guard.)*

> The guard from warmup 3 is here. Without it, `open()` on a missing file raises
> `FileNotFoundError` and the program dies with a traceback instead of a message a
> person can act on.

*(Highlight `row["amount"] = float(row["amount"])`.)*

> And here's the DictReader problem landing for real. Everything comes back as a
> string, so `"54.30" + "35.00"` would **concatenate** into `"54.3035.00"` rather
> than adding. It wouldn't crash — it'd just produce nonsense. So the conversion
> happens on the way in, once, before any maths.

*(Scroll to `write_report`, highlight the `"w"`.)*

> Writing mode is `"w"`, which truncates the file and starts fresh. `"a"` would
> append, so re-running the program would stack a second report underneath the
> first.

*(Highlight `:.2f`.)*

> And `:.2f` on the money, so 35.0 writes as `$35.00` instead of looking broken.

```bash
python3 mini_project.py
```

*(Open the newly created `food_report.txt`.)*

> There's the file, written live. Header with today's date, one line per expense,
> total at the bottom.

*(Point at the function list.)*

> Same shape as last week: `load_expenses`, `filter_by_category`, `total_amount`
> and `write_report` each do one job and return, and `build_report` is the only
> one that orchestrates. That's why adding the "Transport" extension was a single
> extra call, not a second program.

---

## 3:35 – 4:05 · Mindset — debugging (webcam)

> The mindset question asked for three adjectives about debugging. Mine were
> **humbling, repetitive and clarifying**.
>
> Humbling because the bug is nearly always mine and it's usually not clever. The
> computer has been right and I've been wrong every time so far.
>
> Repetitive because most of my bugs are the same three bugs — wrong type, wrong
> scope, wrong path. The `TypeError` in Week 2 and the `NameError` I triggered on
> purpose in Week 6 are the same mistake at different addresses: assuming a value
> is something it isn't. And this week added the third one, wrong path, which
> `os.getcwd()` answers in one line.
>
> Clarifying because a bug is the only time the code tells you what it actually
> does rather than what you meant.
>
> The practice that's changed most: printing the **type**, not just the value.
> `print(x)` shows `42`. `print(type(x))` shows `<class 'str'>` — which is the
> actual bug. Assignment 1 had me printing types next to values and at the time it
> felt like busywork. It's now the first thing I reach for.

---

## 4:05 – 4:20 · Close (webcam)

> So that's Assignment 7. The thread was that data coming out of a file is text
> until you make it something else, and that a relative path means nothing without
> knowing where you're standing. Everything's linked in the submission README.
> Thanks for watching.

---

## Delivery notes

- Delete `food_report.txt` before recording and let the program create it on
  camera. Showing an output file appear is worth more than pointing at one.
- The `"54.3035.00"` concatenation example is the best line in this video. Say the
  wrong answer out loud.
- Show `os.getcwd()` output before you explain relative paths, not after — the
  explanation only lands once they've seen the actual directory.
- Under 3:00 reads as thin; over 5:00 gets cut off. Time your first take.

---

## Video URL

Upload to YouTube (unlisted) or Loom, then paste the link here and in the two
other places it is needed.

**Video URL:** `VIDEO_URL_HERE`

| Also paste it into | Where |
| --- | --- |
| Submission README `URL2` row | [README.md](README.md) |
| Pull request description | [python-intro-homework#6](https://github.com/ba-00001/python-intro-homework/pull/6) |
| Course index video table | [main README](https://github.com/ba-00001/brian-bazurto-python/blob/main/README.md#video-reflections) |
