# Assignment 2 — Video Reflection Script

**Target length:** 3–5 minutes (this script runs ~4:15 spoken at a normal pace).
**Setup:** screen share of the terminal and the editor, webcam in the corner for
the intro and the close.

**Before you hit record**

- Open a terminal, cleared, sitting in `python-intro-homework/` — *not* inside
  `week-2/assignment-2/` yet. The first thing you do on camera is `cd` into it,
  and that only reads as real if you start outside.
- Open the four warmups and `mini_project.py` in the editor as separate tabs.
- Open two browser tabs: the `assignment-2` branch on GitHub, and pull request #1.
- Know your answer for `warmup2.py` (today's date) and your test temperature for
  the mini-project (use **72**, the sample output uses it).

---

## 0:00 – 0:25 · Intro (webcam)

> Hey, I'm Brian Bazurto, and this is my reflection for Assignment 2 of Python
> Intro 26.3 with Code the Dream. This week was the command line and the
> professional environment — moving around my machine from the terminal instead
> of Finder, and getting work into Git with a branch, commits, and a pull
> request. Four warmups and a Fahrenheit-to-Celsius converter. Let me show you.

*(Switch to screen share, terminal.)*

---

## 0:25 – 1:05 · The repository move, and navigating there (screen: terminal)

> First thing worth saying, because it cost me time: Assignment 1 went in a repo
> I made myself, so I assumed everything did. It doesn't. From Week 2 the work
> goes in a **fork of the class homework repo**, and I spent a while looking for
> a `week-2` folder in a repository that was never going to have one.

*(Type each command, let the output land before the next.)*

```bash
ls
cd week-2/assignment-2
pwd
```

> `ls` lists what's here, so I can see the week folders. `cd week-2/assignment-2`
> moves two levels at once — the slash chains them, I don't need two commands.
> And `pwd` prints where I actually am, which is the one I use most, because
> "can't open file" almost always means I'm running the right filename from the
> wrong folder. `cd ..` is how I get back up when I overshoot.

---

## 1:05 – 1:30 · Warmup 1 — proving the setup works

```bash
python3 warmup1.py
```

> `Python is working!` — that's the whole point of warmup 1. The code isn't the
> exercise; checking that Python is actually installed and that I can run a file
> **from the terminal** rather than from an editor's play button is the exercise.
> I recorded the command and its output in the header comment, because six weeks
> from now the file alone won't tell me what I ran.

---

## 1:30 – 1:55 · Warmup 2 — input, no conversion

*(Open `warmup2.py`, then run it.)*

```bash
python3 warmup2.py
```

> Warmup 2 asks for today's date and echoes it back in an f-string. One thing I
> want to point at deliberately: there's **no conversion here**. `input()` hands
> back text, the date stays text, and text is what I want — so there's nothing to
> wrap in `int()` or `float()`. That matters because in the very next warmup, not
> converting is exactly what breaks.

---

## 1:55 – 2:20 · Warmup 3 — reading git log

*(Open `warmup3.py`, scroll to the header comment.)*

> Warmup 3 is my first real commit, and the header holds the actual
> `git log --oneline` output:

```
2f9b361 Add warmup1 and warmup2 for week 2
294742d add week 2 folder
58d836d Add files via upload
```

> Reading it: newest at the top, oldest at the bottom. The short string on the
> left is the commit hash — an id for that snapshot, which is how I'd point at
> one specific commit later. The bottom two came with the repo when I forked it,
> so they aren't mine. And `--oneline` squashes each commit to a single row
> instead of printing the author and date for every one.
>
> The ordering detail is that this log only exists **because** I committed
> warmup 1 and 2 first. There was nothing to show until something was saved.

---

## 2:20 – 3:05 · Warmup 4 — the error I caused on purpose

*(Open `warmup4.py`, scroll to the commented-out broken version.)*

> Warmup 4 is a deliberate bug. I wrote the broken version first, ran it, read
> what Python said, and *then* fixed it — rather than writing it correctly and
> inventing an error afterwards. Here's the broken code, and here's the real
> traceback:

```
Traceback (most recent call last):
  File "warmup4.py", line 6, in <module>
    age = 2026 - birth_year
          ~~~~~^~~~~~~~~~~~
TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

> Reading it top to bottom: "Traceback" just means an error report follows. The
> `File` and line number tell me exactly where to look. Those little `~~~^~~~`
> marks underline the part of the line that broke, so I'm not guessing which bit
> of a long line is at fault. And the last line is the actual problem —
> `TypeError`, and it names both types involved, `int` and `str`.
>
> The cause: `input()` always hands back a string, even when I type digits. So
> `birth_year` was the text `"1998"`, not the number. Python has no rule for
> subtracting text from a number, so it stopped rather than guessing what I
> meant.

*(Highlight the fixed line.)*

> And that's a `TypeError` as opposed to a `ValueError` — a TypeError means the
> *type* is wrong for the operation; a ValueError would mean the type is right
> but the contents aren't usable, like `int("hello")`. The fix is one `int()` in
> the right place.

---

## 3:05 – 3:35 · Mini-project — Fahrenheit to Celsius (screen: terminal)

*(Open `mini_project.py`, then run it with 72.)*

```bash
python3 mini_project.py
```

> `72` in, `22.2°C` out. Two decisions in here I'd defend.
>
> First, `float()` and not `int()`. Temperatures aren't whole numbers — typing
> `98.6` with `int()` would fail outright, and typing `72` with `float()` just
> gives me `72.0`. So float is the safer choice for both kinds of input.

*(Highlight the brackets in the formula.)*

> Second, the brackets. Python does multiplication and division before
> subtraction, so without them this would calculate `fahrenheit - (32 * 5 / 9)`.
> I checked it with 72: the correct version gives 22.2, the unbracketed one gives
> 54.2. It wouldn't crash — it would just be quietly wrong, which is worse.
>
> And `:.1f` only changes how the number is *printed*. `celsius` still holds the
> full 22.222… underneath.

---

## 3:35 – 4:00 · Mindset — AI for learning (webcam)

> The mindset question this week was about AI tools. I use them most days, and I
> run some smaller models locally for the low-stakes work so I'm not paying for
> things that don't need to be good.
>
> What all that use has actually taught me is where it stops being reliable. I've
> been handed answers that sounded completely confident and were just wrong. So
> the rule I've settled on for this course is that I don't let it write something
> I couldn't then explain out loud — which is roughly what this video is a test
> of. Warmup 4 is the honest version of that: I caused the error, read it myself,
> and the fix stuck because I understood the cause, not because I pasted it.

---

## 4:00 – 4:15 · Close (webcam)

> So that's Assignment 2 — the terminal, Git, and one type bug that taught me
> more than the other four files combined. Everything's linked in the submission
> README. Thanks for watching.

---

## Delivery notes

- Actually type the `cd` and `pwd` commands live. Don't start already inside the
  folder — the navigation *is* the assignment.
- Read the `TypeError` line slowly and out loud. Reviewers listen for whether you
  understand it or just pasted a fix.
- Don't read the header comments verbatim; they're written out, so say the short
  version and let the screen carry the detail.
- Under 3:00 reads as thin; over 5:00 gets cut off. Time your first take.

---

## Video URL

Upload to YouTube (unlisted) or Loom, then paste the link here and in the two
other places it is needed.

**Video URL:** `VIDEO_URL_HERE`

| Also paste it into | Where |
| --- | --- |
| Submission README `URL2` row | [README.md](README.md) |
| Pull request description | [python-intro-homework#1](https://github.com/ba-00001/python-intro-homework/pull/1) |
| Course index video table | [main README](https://github.com/ba-00001/brian-bazurto-python/blob/main/README.md#video-reflections) |
