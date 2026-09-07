# Assignment 6 — Video Reflection Script

**Target length:** 3–5 minutes (this script runs ~4:25 spoken at a normal pace).
**Setup:** screen share of the editor and a terminal in `week-6/assignment-6/`,
webcam for the intro, the mindset section and the close.

**Before you hit record**

- Terminal cleared, inside `week-6/assignment-6/`.
- Open **both** mini-projects side by side if your editor allows it:
  `week-5/assignment-5/mini_project.py` and `week-6/assignment-6/mini_project.py`.
  The before/after is the strongest thing you can show this week.
- Other tabs: the four warmups.
- Decide your live inputs:
  - `warmup4.py` → **85** (valid), then run again with **abc** (invalid).
  - `mini_project.py` → **4** (sort — it also prints "Original is unchanged"),
    then **3** searching for 55, then **5**.

---

## 0:00 – 0:25 · Intro (webcam)

> Hey, I'm Brian Bazurto, and this is my reflection for Assignment 6 of Python
> Intro 26.3 with Code the Dream. This week was functions and scope — default
> parameters, returning values instead of printing them, where variables live,
> and then refactoring last week's Number Cruncher into functions. The
> refactor is the interesting part, so I'll spend most of the time there.

*(Switch to screen share.)*

---

## 0:25 – 0:55 · Warmup 1 — default parameters

*(Open `warmup1.py` and run it.)*

> One function, called three different ways. `name` is required; `greeting` has a
> default, so callers can leave it out and get "Hello".

*(Highlight the `def` line.)*

> One rule I hit: defaults have to come **after** the non-default parameters.
> Writing `def greet(greeting="Hello", name)` is a `SyntaxError`, not a runtime
> problem — Python won't even load the file.
>
> The third call passes the greeting by keyword. Same result as leaving it out
> here, but the point is that naming the parameter means I don't have to remember
> the order.

---

## 0:55 – 1:25 · Warmup 2 — return vs print

*(Open `warmup2.py` and run it.)*

> Two temperature conversions, and the thing that matters is that these **return**
> their answer instead of printing it.

*(Highlight a `return`.)*

> If I used `print()` in here, the function would show the number but *evaluate to*
> `None` — so `f"{celsius_to_fahrenheit(0)}"` would print the word "None". Because
> it returns, the maths happens inside the curly braces at the call site and
> `:.1f` rounds it for display.
>
> Same bracket point as Week 2, still true: `(f - 32)` has to happen before
> multiplying by five ninths.

---

## 1:25 – 2:00 · Warmup 3 — scope, and an error I caused on purpose

*(Open `warmup3.py` and run it.)*

> Warmup 3 is scope, in two examples. First one: `secret` is created inside
> `make_secret` and thrown away when the function ends. Printing it from outside
> gives:

```
NameError: name 'secret' is not defined
```

> I triggered that for real and kept it as a comment so the rest of the file
> still runs. And the error is **accurate** — by the time that line executes, the
> function has already finished and `secret` is gone.

*(Scroll to example 2.)*

> Second example is the fix: `return` sends a copy of the value back to the caller
> before the local one disappears. `escaped_secret` is a *different* variable in
> the outer scope that happens to hold the same string. The function's own
> `secret` is still gone.

---

## 2:00 – 2:30 · Warmup 4 — a function that answers one question

*(Open `warmup4.py`, then run it twice.)*

```bash
python3 warmup4.py
```

*(85, then re-run with abc.)*

> `is_valid_score` answers one yes/no question and returns the answer, so the
> decision about what to *print* stays out of it.
>
> Two separate checks inside. `isinstance` catches the case where the score isn't
> a whole number at all — the string `"85"` and the float `85.5` both fail there.
> Then a chained comparison, `0 <= score <= 100`, which reads as both halves
> joined by "and", inclusive at both ends.

*(Highlight the `.lstrip("-").isdigit()` line.)*

> The awkward bit is the caller. `input()` always gives text, and my function
> rejects text on purpose — so I convert first, but only when the text is actually
> digits, otherwise `int()` would raise before my function got a look in. And
> `.lstrip("-")` lets a negative like `-5` through to be converted and then
> correctly rejected as *out of range* rather than as "not a number".
>
> Because it returns a real `True` or `False`, it drops straight into the `if`
> with no `== True` needed.

---

## 2:30 – 3:35 · Mini-project — the same program, reorganised (screen)

*(Put the Week 5 and Week 6 files side by side.)*

> Here's Week 5's Number Cruncher and here's Week 6's. This is a **new file** — I
> didn't edit the Week 5 one — so the git history holds both versions and you can
> see exactly what moved.
>
> The algorithms are unchanged. Minimum, maximum, search and sort are still
> written by hand, no `min()`, `max()` or `sorted()`. What changed is **where they
> live**.

*(Point at Week 5's `elif choice == "3"` block, then at Week 6's `search`.)*

> In Week 5 the search logic sat inside an `elif` branch, and it could only ever
> be used by that branch. Now it's a function with a name, and the menu just calls
> it.

*(Highlight `return position` inside `search`.)*

> The refactor also removed something. Week 5's search needed a `break` and a
> `found_at` variable. `return` exits the function immediately, so the `break`
> disappeared entirely.

*(Highlight the printing in `main` for choice 3.)*

> And this is the decision I'd most want to defend. The printing lives in `main`,
> **not** in `search`. `search` answers one question — where is it — and `main`
> decides what that means to the user. That split is the whole reason `search`
> could be reused by something that wants to *act* on the index rather than print
> it. Every one of these functions returns; none of them print.

```bash
python3 mini_project.py
```

*(Choose 4.)*

> And `bubble_sort` works on a copy, which is why I print the original underneath
> — proof it came back unchanged. If it sorted in place, the caller's list would
> come back reordered as a side effect and every later menu choice would be
> working on different data than it was given.

*(Scroll to the bottom of the file.)*

> Last thing: nothing above this line *ran* anything — it only defined names.
> `main()` at the bottom is the one call that starts the program.

---

## 3:35 – 4:10 · Mindset — peer collaboration (webcam)

> The mindset question was about collaboration. In my family it's the default and
> nobody calls it collaboration — something needs doing, several people turn up,
> and it gets worked out on the spot. It's also completely verbal. You find out
> what's happening because you were in the room.
>
> That's the part I've had to unlearn. Knowledge living in people and getting
> passed on by being present doesn't work for software. Commit messages, pull
> request descriptions, a README that explains itself — that's collaboration with
> people who **weren't** in the room, including me in three months. That was a
> genuinely new idea and it took a while to stop feeling like paperwork.
>
> My own challenge is that I go quiet when I'm behind, which is precisely
> backwards. It's happened twice in this course. Weeks 2 and 3 went in late, and
> as I slipped further I posted less, because turning up to say "still not done"
> felt worse than saying nothing. The Week 2 fork confusion is the clearest case —
> I never asked, because asking meant admitting I was lost. One message would have
> cost a minute.

---

## 4:10 – 4:25 · Close (webcam)

> So that's Assignment 6. Refactoring didn't make the program do anything new — it
> made four pieces of it reusable, and it deleted a `break` I no longer needed.
> Everything's linked in the submission README. Thanks for watching.

---

## Delivery notes

- The side-by-side of Week 5 and Week 6 `mini_project.py` is the single most
  persuasive thing in this video. Set it up before you record.
- Say "return, not print" out loud at least twice — it's the graded idea of the
  week and it appears in warmup 2, warmup 4 and the refactor.
- Show the `NameError` comment in warmup 3 rather than describing it.
- Under 3:00 reads as thin; over 5:00 gets cut off. Time your first take.

---

## Video URL

Upload to YouTube (unlisted) or Loom, then paste the link here and in the two
other places it is needed.

**Video URL:** `VIDEO_URL_HERE`

| Also paste it into | Where |
| --- | --- |
| Submission README `URL2` row | [README.md](README.md) |
| Pull request description | [python-intro-homework#5](https://github.com/ba-00001/python-intro-homework/pull/5) |
| Course index video table | [main README](https://github.com/ba-00001/brian-bazurto-python/blob/main/README.md#video-reflections) |
