# Assignment 8 — Video Reflection Script

**Target length:** 3–5 minutes (this script runs ~4:30 spoken at a normal pace).
**Setup:** screen share of the editor and a terminal in `week-8/assignment-8/`,
webcam for the intro, the mindset section and the close.

**Before you hit record**

- Terminal cleared, inside `week-8/assignment-8/`, **with the virtual environment
  activated** — `source .venv/bin/activate`. Your prompt should show `(.venv)`.
  That's the proof for warmup 4 and it costs nothing to have on screen the whole
  video.
- Editor tabs: the four warmups, `mini_project.py`, `requirements.txt`, and
  `../data/messy_data.csv` — open the messy CSV early so viewers can see the bad
  rows before you run anything.
- Decide your live inputs:
  - `warmup1.py` → **hello**, then **12.5**
  - `warmup2.py` → **10** then **0** (ZeroDivisionError branch), then run again
    with **10** and **abc** (ValueError branch)
- Optional but strong: have a second terminal **without** the venv active, to show
  `ModuleNotFoundError` when `warmup4.py` runs against system Python.

---

## 0:00 – 0:25 · Intro (webcam)

> Hey, I'm Brian Bazurto, and this is my reflection for Assignment 8 of Python
> Intro 26.3 with Code the Dream. This week was errors and debugging — `try` and
> `except`, defensive programming, and virtual environments. Four warmups and a
> Defensive CSV Reader that's handed a file with deliberately broken rows in it.
>
> The one idea running through all of it: an error isn't a crash, it's
> information — and where you catch it decides how much of your program survives.

*(Switch to screen share.)*

---

## 0:25 – 0:55 · Warmup 1 — validating input

```bash
python3 warmup1.py
```

*(Type `hello`, then `12.5`.)*

> Keeps asking until `float()` accepts what I typed.

*(Highlight the `try` block — just the one line inside it.)*

> The thing I'd point at is how **little** is inside the `try`. Only the line that
> can actually raise. I could have wrapped the `input()` call too, and it would
> still work — but then a different problem on that line would get swallowed by an
> `except ValueError` that was never meant for it.
>
> `continue` skips the rest of the body and re-prompts. And the print at the
> bottom is only reachable when the conversion worked, so `number` definitely
> exists by the time I use it.

---

## 0:55 – 1:35 · Warmup 2 — two failures, two messages, and `else`

```bash
python3 warmup2.py
```

*(10 then 0.)*

> Divide by zero — its own message. Now the other failure:

*(Re-run with 10 and `abc`.)*

> Not a number — a different message.
>
> Both conversions and the division sit in one `try` block, because any of the
> three failing means the same thing to the user: I can't do this sum. But the
> **fixes** are different, so there are two separate `except` clauses.

*(Point at the ordering.)*

> On ordering — it matters when one exception is a subclass of another, because
> the first matching clause wins. These two are siblings, so either order works
> here. Putting the more specific case first is just the habit worth having.

*(Highlight the `else`.)*

> And the success case is in `else`, not at the end of `try`. `else` runs only
> when the `try` raised nothing — putting it there makes it obvious that this line
> isn't itself being guarded.

---

## 1:35 – 2:00 · Warmup 3 — a missing file, said usefully

*(Open `warmup3.py`, run it.)*

> Without the `except`, Python prints this:

```
FileNotFoundError: [Errno 2] No such file or directory: '../data/missing.txt'
```

> Which is accurate — and it's aimed at **me**, not at whoever is running the
> program. Catching it lets me say the same thing in a way that suggests what to
> do about it. That's the whole distinction this warmup is making: the traceback
> is for the developer, the caught message is for the user.

---

## 2:00 – 2:30 · Warmup 4 — the virtual environment

*(Point at `(.venv)` in the prompt, then run warmup4.)*

```bash
python3 warmup4.py
```

> It prints the `requests` version, which proves the import came from the venv.

*(Optional: switch to the terminal without the venv and run it — `ModuleNotFoundError`.)*

*(Open `requirements.txt`.)*

> Five packages in here, and I only installed **one** by hand — `requests`. The
> other four are its dependencies, pulled in automatically. That's exactly why you
> commit `requirements.txt` rather than a note saying "needs requests": it records
> the whole tree, at the versions that actually worked. And `.venv/` itself is
> gitignored — you commit the recipe, not the ingredients.

---

## 2:30 – 3:35 · Mini-project — the Defensive CSV Reader (screen)

*(Open `../data/messy_data.csv` and scroll it.)*

> Here's the data. It's deliberately broken — a blank amount, a non-numeric
> amount, a row with an extra column. The job is a clean summary rather than a
> crash on the first bad one.

*(Open `mini_project.py`, highlight the try inside the loop.)*

> **The entire design decision is where the `try` sits.** It's inside the row
> loop, not around it. One `try` around the whole loop would abandon every
> remaining row the moment one failed — a single bad cell on line 3 would cost me
> the eleven good rows after it. Handling each row inside the loop means one bad
> row costs exactly one row.

*(Highlight the `if None in row` guard.)*

> This one is a guard and **not** an `except`, on purpose. `DictReader` doesn't
> raise on extra columns — it quietly files the surplus under the key `None`. So
> it isn't an exception to catch, it's a *shape* to check for. And it has to
> happen first, because such a row might still parse "successfully" and hide the
> fact that it was malformed.

*(Scroll to `parse_row`, highlight the `amount is None` check.)*

> Similar problem here. A missing trailing column comes back as `None`, and
> `float(None)` raises `TypeError` — not `ValueError` — so it would escape both
> `except` clauses below. Converting it to a `ValueError` here keeps all the "bad
> amount" cases in one place.

*(Highlight `except ValueError as e`.)*

> And `as e` captures the exception so the report can quote the actual reason
> instead of just "something went wrong".

*(Point at the `open` in `read_csv_defensively`.)*

> One more: the assignment asked for `try`/`except FileNotFoundError` rather than
> the `os.path.exists()` check I used last week. Both work — but this one can't go
> stale. `exists()` answers a question a moment before you open the file, and
> something could delete it in between. Trying and catching asks the question and
> does the work at the same time.

```bash
python3 mini_project.py
```

> Rows attempted, parsed, skipped — and every skipped row says which row number
> and why. `start=1` on the enumerate so row 3 in the report is the third row of
> actual data, not counting the header.

---

## 3:35 – 4:15 · Mindset — problem solving (webcam)

> The mindset question was about a problem-solving process, and I'll be honest:
> I've got one that works and one I actually do under pressure, and they aren't
> the same.
>
> The one that works — reproduce it reliably first, because if I can't make it
> happen on demand then anything I "fix" is a guess I can't check. Then write down
> what I expected versus what happened, in two sentences. The gap between those
> two sentences is nearly always the bug. That's the step I skip most and the one
> that pays best — I've fixed two things this course while writing them down,
> before running anything. Then cut it down, and change one thing at a time.
>
> This week's mini-project was actually built that way: I got one row parsing,
> then fed it a bad row on purpose, then the whole file.
>
> What I actually do when I'm frustrated is speed up — change something, re-run,
> change something else, with no hypothesis. It feels like effort. It's how I lose
> an hour and learn nothing.

---

## 4:15 – 4:30 · Close (webcam)

> So that's Assignment 8. If there's one line to take from it: the `try` goes
> inside the loop, because the cost of an error should be one row and not the
> whole file. Everything's linked in the submission README. Thanks for watching.

---

## Delivery notes

- Record with `(.venv)` visible in the prompt for the whole video. It quietly
  evidences warmup 4 without you having to argue for it.
- Show `messy_data.csv` **before** running the mini-project. The output only means
  something once the audience has seen the bad rows.
- The "one bad row costs one row" line is the thesis of this assignment. Say it
  slowly and say it once, early.
- Under 3:00 reads as thin; over 5:00 gets cut off. Time your first take.

---

## Video URL

Upload to YouTube (unlisted) or Loom, then paste the link here and in the two
other places it is needed.

**Video URL:** `VIDEO_URL_HERE`

| Also paste it into | Where |
| --- | --- |
| Submission README `URL2` row | [README.md](README.md) |
| Pull request description | [python-intro-homework#7](https://github.com/ba-00001/python-intro-homework/pull/7) |
| Course index video table | [main README](https://github.com/ba-00001/brian-bazurto-python/blob/main/README.md#video-reflections) |
