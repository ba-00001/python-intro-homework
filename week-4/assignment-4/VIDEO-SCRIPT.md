# Assignment 4 — Video Reflection Script

**Target length:** 3–5 minutes (this script runs ~4:20 spoken at a normal pace).
**Setup:** screen share of the editor and a terminal in `week-4/assignment-4/`,
webcam for the intro, the mindset section and the close.

**Before you hit record**

- Terminal cleared, already inside `week-4/assignment-4/`.
- Four editor tabs: `warmup1.py`, `warmup2.py`, `warmup3.py`, `mini_project.py`.
- Also open `week-4/data/roster.py` in a fifth tab — you are going to point at it
  and say you didn't touch it.
- Run `mini_project.py` once before recording. The `Subjects offered:` line is a
  **set**, so its order changes between runs; you want to have seen that already
  so it doesn't throw you live.

---

## 0:00 – 0:25 · Intro (webcam)

> Hey, I'm Brian Bazurto, and this is my reflection for Assignment 4 of Python
> Intro 26.3 with Code the Dream. This week was the core data structures — lists,
> dictionaries and sets — three warmups and a Student Roster Analyzer. The theme
> for me was **picking the right container**, because each of these three is good
> at something the others are bad at.

*(Switch to screen share.)*

---

## 0:25 – 1:05 · Warmup 1 — indexing and slicing, no loops

*(Open `warmup1.py` and run it.)*

> Warmup 1 is a list of eight numbers, and all four answers come from indexing
> and slicing — nothing here loops.
>
> `numbers[0]` is the first item, because positions start at zero, not one.

*(Highlight `numbers[-1]`.)*

> For the last one I used `numbers[-1]` rather than `numbers[7]`. Negative
> indexes count back from the end, so this keeps working if the list length
> changes. `[7]` only works for exactly eight items.

*(Highlight `numbers[2:6]`.)*

> The slice is the one that caught me. Slicing is `[start:stop]` and **the stop
> is not included** — so `2:6` gives positions 2, 3, 4 and 5. Four items,
> stopping just before 6. My first attempt returned three numbers because I
> assumed the end was inclusive.
>
> And `[::-1]` is start and stop left blank — meaning the whole list — with a
> step of minus one, so walk it backwards. It builds a **new** list, so `numbers`
> itself is untouched afterwards.

---

## 1:05 – 1:40 · Warmup 2 — dictionaries, and the thing that surprised me

*(Open `warmup2.py` and run it.)*

> Warmup 2 is a dictionary — labelled values. I reach for a dictionary when one
> thing has several different attributes, because position means nothing here.
> Asking for "item 1" of a student wouldn't mean anything.

*(Point at the `subjects` key.)*

> Worth noticing that the value of `subjects` is itself a list. A dictionary can
> hold any type, including another collection.

*(Highlight the `for key, value in student.items()` line.)*

> The loop takes **two** variables because `.items()` hands back the key and its
> value on each pass. If I looped over the dictionary directly I'd only get the
> keys, and I'd have to look each value up separately.

*(Highlight `student["graduated"] = False`.)*

> And this is the bit that genuinely surprised me. There's no `.add()` for
> dictionaries — assigning to a key that doesn't exist yet **creates** it. The
> same syntax that changes an existing value also adds a new one. The new key
> goes on the end, and printing the whole dictionary is how I confirmed it landed.

---

## 1:40 – 2:10 · Warmup 3 — sets, and why order stops existing

*(Open `warmup3.py` and run it.)*

> Warmup 3 is two lists of programming languages turned into sets. A set is
> unordered and holds no duplicates, and that second part is the useful bit —
> it's what makes "everything from both lists, no repeats" a single operator
> instead of a loop with a check inside it.
>
> `|` is union — everything in either set, each listed once, so the two copies of
> Python collapse to one. `&` is intersection — only the ones in both, so Python
> and SQL.

*(Highlight the difference line.)*

> `-` is difference, and this is the one where **order matters** in a way it
> doesn't for the other two. `my_set - teammate_set` is "mine that they don't
> have". Flipping it gives theirs that I don't have, which is a completely
> different answer.
>
> One thing to know reading the output: sets have no order, so these can print in
> a different sequence each run. That isn't a bug.

---

## 2:10 – 3:15 · Mini-project — Student Roster Analyzer (screen)

*(Point at `week-4/data/roster.py` in the other tab first.)*

> The roster comes from `week-4/data/roster.py`, which I copied from and left
> untouched, as instructed.

*(Open `mini_project.py`.)*

> This is nested data — a **list** of students where each student is a
> **dictionary**. The list keeps them in order, the dictionary keeps each
> student's fields labelled. Getting at a value takes two steps:
> `students[0]` is a whole dictionary, and `students[0]["name"]` is the actual
> text.

*(Scroll to the top scorer block.)*

> The assignment says not to use `max()`, so the top scorer is tracked by hand.
> Two variables held **outside** the loop so they survive between passes — and
> the pair is the whole trick. Tracking only the score would leave me knowing 95
> and not who got it. So both update together or neither does.

*(Highlight `top_score = -1`.)*

> `top_score` starts at minus one rather than zero, so the first student always
> wins the first comparison no matter what the scores are.

*(Scroll to the average.)*

> The average accumulates first and divides once at the end. Dividing inside the
> loop would give a running average, which isn't the same number. And `len()`
> means I'm not hardcoding 8 — the code stays correct if the roster changes.

*(Scroll to subjects and high scorers.)*

> Subjects use a **set**, because a set throws away repeats on its own — adding
> "Python" three times still leaves one entry, with no "have I already got this?"
> check. High scorers use a **list**, because there I want every name that
> qualifies, in roster order. Same loop shape, different container, chosen for
> what each one is good at. And it's `> 75` strictly, so a 75 exactly doesn't make
> the cut.

*(Run it.)*

```bash
python3 mini_project.py
```

*(Point at the average.)*

> One output detail I want to be honest about, because it looked like a bug. The
> real average is 650 over 8, which is **81.25 exactly** — and it prints 81.2, not
> 81.3. That's not rounding down; Python rounds a value sitting exactly halfway
> to the nearest *even* digit. Took me a while to find that out, and I'd rather
> say it than pretend I meant it.

---

## 3:15 – 3:50 · Mindset — curiosity, and one thing I do without knowing why (webcam)

> The mindset question was about curiosity. Mine recently was how people actually
> remember vocabulary in a new language — I'd built a language learning project
> on an assumption I'd never checked, that if repetition works then more
> repetition works better. It doesn't. Spaced repetition is about reviewing right
> before you'd have forgotten, and what surprised me when I tried it on myself is
> **how bad doing it properly feels**. The version that feels good is the one
> that doesn't work.
>
> The second half asked for a best practice I follow without knowing the why, and
> mine is this: a branch for every assignment, merged with a pull request. I do
> it because I've been told to. I can recite the reasons — keeps work separate,
> lets people review it, gives you a way back — but I'm one person in my own repo
> and nobody reviews my pull request before it merges. So right now it feels like
> performing a ritual correctly without knowing what it's for.
>
> The way I'd find out isn't reading more about it. It's causing the problem on
> purpose — two branches editing the same lines in a throwaway repo, merge both,
> and sit with the conflict.

---

## 3:50 – 4:20 · Close (webcam)

> So that's Assignment 4. The one sentence I'd take out of it: list, dictionary
> and set aren't three ways to write the same thing — the set doing deduplication
> for free is why the subjects loop has no `if` in it. Everything's linked in the
> submission README. Thanks for watching.

---

## Delivery notes

- Show `week-4/data/roster.py` briefly and say you left it untouched. It's a
  stated requirement and it costs five seconds.
- The 81.25 → 81.2 explanation is the strongest thing in this video. Don't skip
  it to save time; cut something in warmup 1 instead.
- Say "a set has no order, so this line can print differently each run" *before*
  you run the mini-project, not after.
- Under 3:00 reads as thin; over 5:00 gets cut off. Time your first take.

---

## Video URL

Upload to YouTube (unlisted) or Loom, then paste the link here and in the two
other places it is needed.

**Video URL:** `VIDEO_URL_HERE`

| Also paste it into | Where |
| --- | --- |
| Submission README `URL2` row | [README.md](README.md) |
| Pull request description | [python-intro-homework#3](https://github.com/ba-00001/python-intro-homework/pull/3) |
| Course index video table | [main README](https://github.com/ba-00001/brian-bazurto-python/blob/main/README.md#video-reflections) |
