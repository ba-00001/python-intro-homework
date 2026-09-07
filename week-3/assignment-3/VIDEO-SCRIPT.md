# Assignment 3 — Video Reflection Script

**Target length:** 3–5 minutes (this script runs ~4:20 spoken at a normal pace).
**Setup:** screen share of the editor and a terminal sitting in
`week-3/assignment-3/`, webcam in the corner for the intro, the mindset section
and the close.

**Before you hit record**

- Terminal cleared, already inside `week-3/assignment-3/`.
- Five editor tabs open: `warmup1.py` through `warmup4.py` and `mini_project.py`.
- Decide your live inputs now so you aren't thinking on camera:
  - `warmup2.py` → **15** (Teen)
  - `warmup4.py` → **-7** (negative *and* odd — one input proves both blocks)
  - `mini_project.py` → **Saturday / evening**, then a second run with
    **blah / morning** to show the fallback.
- Have warmup 3's five Boolean lines on screen; you will read the outputs off it.

---

## 0:00 – 0:25 · Intro (webcam)

> Hey, I'm Brian Bazurto, and this is my reflection for Assignment 3 of Python
> Intro 26.3 with Code the Dream. This week was control flow — `if`, `elif`,
> `else`, Boolean logic, and how Python decides which branch to run. Four warmups
> and a Day Planner mini-project. The thread running through all of it is
> **order** — the order conditions are written in changes the answer, and it does
> it quietly.

*(Switch to screen share.)*

---

## 0:25 – 1:05 · Warmup 1 — why the order of `elif` matters

*(Open `warmup1.py`.)*

> Warmup 1 maps a score to a letter grade. Score is 84, and it prints a B.
>
> The thing I actually want to point at is why the chain has to run **highest to
> lowest**. Python checks these top to bottom and runs the *first* one that's
> true, then skips the rest entirely — the later conditions never even get
> tested.

*(Highlight `elif score >= 60`.)*

> So if I'd put `score >= 60` first, an 84 would match it and come out as a **D**
> — because 84 genuinely *is* greater than or equal to 60. It wouldn't crash. It
> would just be wrong. Going downwards means that by the time a condition is
> reached, everything above it has already been ruled out, so `>= 80` here can
> only mean 80 to 89.
>
> And `else` takes no condition at all — it catches whatever got that far, which
> here is everything under 60.

*(Point at the two prints at the bottom.)*

> Small structural choice: I store the letter in a variable and print once at the
> end, instead of printing inside each branch. The branches do one job — decide —
> and the output lives in one place.

---

## 1:05 – 1:35 · Warmup 2 — `and`, and a conversion that isn't optional

```bash
python3 warmup2.py
```

*(Type 15.)*

> Age categories. 15 comes out as Teen.
>
> Two things. First, `int()` goes on straight away — and not just for tidiness.
> Strings compare **alphabetically**, so `"9" > "17"` is actually `True` in
> Python. That wouldn't crash either; it would quietly hand back the wrong
> category. Same failure mode as warmup 1: silently wrong.
>
> Second, each range needs both ends checked, which is what `and` is for — true
> only when the left side *and* the right side are both true. `age >= 13` on its
> own would match a forty-year-old as well. The last branch is the exception:
> 65-and-up has no upper end, so there's no `and` there.

---

## 1:35 – 2:15 · Warmup 3 — Boolean precedence, including the two I got wrong

*(Open `warmup3.py` and run it.)*

> Warmup 3 is five Boolean expressions. I worked them out on paper first and then
> ran the file to check, and the useful part was that **two of them I got wrong**
> — both about precedence. The order is: `not` first, then `and`, then `or`.

*(Point at line 2.)*

> This is the one that catches people. `True or False and False`. If it went
> strictly left to right it'd be `(True or False) and False`, which is `False`.
> But `and` binds tighter than `or`, so Python does `False and False` first —
> that's `False` — and then `True or False`, which is **`True`**.

*(Point at line 1.)*

> And this one: `not True and False`. `not` applies to `True` on its own, not to
> the whole expression, so it reads as `(not True) and False`.
>
> The last line shows short-circuiting — `or` only needs one side to be true, so
> once the left side is `True` Python never bothers evaluating the right.

---

## 2:15 – 2:45 · Warmup 4 — two blocks, and the edge case

```bash
python3 warmup4.py
```

*(Type -7.)*

> `-7 is negative.` and `-7 is odd.` — one input, two answers.
>
> That's the point of the file. These are **two independent questions** about the
> same number, so they get two separate `if`/`elif`/`else` blocks. A single chain
> can only ever run one branch, so it could print the sign or the parity, never
> both.

*(Highlight the `else` in the sign block.)*

> Zero gets its own case, because zero is neither positive nor negative. Letting
> it fall into the negative branch would be wrong, and it's exactly the edge case
> you miss if you only ever test with 7 and -7.
>
> And parity uses `%`, the remainder after division — `8 % 2` is 0, `7 % 2` is 1.
> Worth knowing that this works for negatives too: `-7 % 2` is 1 in Python, so -7
> comes out odd, which is what I wanted.

---

## 2:45 – 3:30 · Mini-project — Day Planner (screen: terminal)

*(Open `mini_project.py` first, then run it.)*

> The Day Planner asks for a day and a time of day and suggests something. Three
> days times three times of day is the nine combinations required.

```bash
python3 mini_project.py
```

*(Saturday / evening.)*

> Two design decisions worth explaining.

*(Highlight the `.strip().lower()` lines.)*

> One — I normalise the input up front. `.strip()` removes stray spaces at either
> end, `.lower()` makes it lowercase, and they chain because `.strip()` hands back
> a new string for `.lower()` to work on. After those two lines, everything below
> only ever has to compare against lowercase, so "Saturday", "saturday" and
> "SATURDAY" all just work.

*(Scroll up to the two `not in` checks.)*

> Two, and this is the one I'd defend hardest — the **unrecognised cases are
> checked first**, before any real combination. Doing it that way means the nine
> branches below can assume both answers are valid.

*(Run it again with blah / morning.)*

> If I'd done it the other way round, every single one of those nine branches
> would have needed its own `else` for bad input. Nine copies of the same error
> message is nine places to forget one.
>
> Same reasoning for the two constants at the top — the wording of "Monday,
> Tuesday, Wednesday…" lives in one place, so adding a day means editing one
> string instead of hunting inside a print.

---

## 3:30 – 4:05 · Mindset — motivation and growth mindset (webcam)

> The mindset question was about why I want to do this, and about growth mindset.
>
> The honest answer to the first one: I've been making things for a while without
> really knowing how any of it works, and I got tired of that. I've got side
> projects that mostly work — but they work the way something works when you've
> copied it together out of examples, and the second it breaks in a way the
> example didn't cover, I'm stuck, because I never had a picture in my head of
> what it was doing.
>
> On growth mindset, my example is guitar. About a year in I nearly stopped —
> chord changes I was fumbling in month three I was still fumbling in month
> eleven, and what I told myself was that I'd found my ceiling. Some people have
> an ear for it and I don't. That felt like being realistic at the time; it was
> textbook fixed mindset.
>
> What changed it was being told to slow down — metronome, at a speed that was
> almost boring, get it clean, and only then speed up. It felt like going
> backwards. That's the same instinct this week's warmup 3 needed: sit down and
> work the Booleans out on paper before running them, get two wrong, and find out
> *why* rather than just running it until it matched.

---

## 4:05 – 4:20 · Close (webcam)

> So that's Assignment 3. The pattern I keep noticing is that control-flow bugs
> don't crash — the wrong `elif` order, comparing strings instead of numbers,
> forgetting zero. They all just quietly give you the wrong answer. Everything's
> linked in the submission README. Thanks for watching.

---

## Delivery notes

- Run warmup 4 with **-7** once. One input demonstrating both blocks is tighter
  than four separate runs.
- Say the `True or False and False` walkthrough slowly — it's the single strongest
  moment in this video and it's easy to rush.
- Run the mini-project twice: valid input, then bad input. The fallback is a
  graded requirement, so show it rather than describe it.
- Under 3:00 reads as thin; over 5:00 gets cut off. Time your first take.

---

## Video URL

Upload to YouTube (unlisted) or Loom, then paste the link here and in the two
other places it is needed.

**Video URL:** `VIDEO_URL_HERE`

| Also paste it into | Where |
| --- | --- |
| Submission README `URL2` row | [README.md](README.md) |
| Pull request description | [python-intro-homework#2](https://github.com/ba-00001/python-intro-homework/pull/2) |
| Course index video table | [main README](https://github.com/ba-00001/brian-bazurto-python/blob/main/README.md#video-reflections) |
