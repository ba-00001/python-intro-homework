# Assignment 6 — Functions & Scope

Week 6 of Python Intro 26.3. Everything required for this assignment lives in
this folder.

## Submission links

| Field | Link |
|-------|------|
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/5 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Mindset Response** | [see below](#mindset-response--peer-collaboration) |

## Required files

| File | What it does |
|------|--------------|
| [warmup1.py](warmup1.py) | `greet(name, greeting="Hello")` called three ways — name only, both positional, greeting by keyword |
| [warmup2.py](warmup2.py) | `celsius_to_fahrenheit()` and `fahrenheit_to_celsius()`, both returning values, printed to one decimal place |
| [warmup3.py](warmup3.py) | Scope demo — the `NameError` pasted as a comment, then `return` solving it |
| [warmup4.py](warmup4.py) | `is_valid_score(score)` returning `True`/`False`, called inside an `if` |
| [mini_project.py](mini_project.py) | Number Cruncher refactored — every operation in its own function, `main()` dispatching |

## What the refactor changed

`mini_project.py` is a **new file**, not an edit of the Week 5 submission — the
Week 5 version is untouched on the `assignment-5` branch, so the git history
holds both.

The algorithms are byte-for-byte the same logic: hand-written min, max, linear
search and bubble sort, still no `min()`, `max()`, `sorted()` or `.sort()`. What
moved is where they live:

| Week 5 | Week 6 |
|--------|--------|
| Min logic inside an `elif` branch | `find_min(numbers)` returning a value |
| Max logic inside an `elif` branch | `find_max(numbers)` returning a value |
| Search loop inside an `elif`, printing its own result | `search(numbers, target)` returning an index; `main()` prints |
| `working = numbers[:]` then sorting inline | `bubble_sort(numbers)` returning a new list |
| Menu `print()`s repeated in the `while` | `show_menu()` returning the choice |
| One long `while` loop at module level | `main()`, called once at the bottom |

The `search` split is the one I'd point at. Week 5's search knew how to find a
number *and* what to say about it. Week 6's only answers "which index", so
something that wanted to act on the index rather than print it could reuse it.

## Data source

The `numbers` list in `mini_project.py` is copied verbatim from
[`week-5/data/numbers.py`](../../week-5/data/numbers.py). The file in `data/` is
untouched.

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
Hello, Alex!
Good morning, Alex!
Hello, Alex!

$ python3 warmup2.py
0°C = 32.0°F
100°C = 212.0°F
72°F = 22.2°C

$ python3 warmup3.py
--- Example 1: the scope problem ---
Inside the function, secret is: I only exist inside this function
The function ran, but 'secret' is not available out here.

--- Example 2: return solves it ---
Outside the function, escaped_secret is: I was returned, so I survived

$ python3 warmup4.py
Enter a score (0-100): 150
Invalid score — must be between 0 and 100.

$ python3 mini_project.py

=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit
Choose an option (1-5): 3
Enter a number to search for: 61
Found at index 4

=== Number Cruncher ===
...
Choose an option (1-5): 4
Sorted: [3, 5, 8, 14, 17, 22, 29, 31, 40, 42, 47, 55, 59, 61, 66, 74, 78, 83, 86, 93]
Original is unchanged: [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
```

## Requirements checklist

- [x] Warmup 1 — default parameter, called with name only, both positional, and greeting by keyword
- [x] Warmup 2 — both conversion functions `return` rather than `print`, output rounded to one decimal
- [x] Warmup 3 — `NameError` traceback pasted in a comment, offending line commented out
- [x] Warmup 3 — `return` used to lift the value into the outer scope and printed to confirm
- [x] Warmup 4 — `is_valid_score` returns `True`/`False`, checks `int` **and** the 0–100 range, called inside an `if`
- [x] Mini-project — `find_min`, `find_max`, `search`, `bubble_sort`, `show_menu`, `main` all defined with `numbers` as a parameter
- [x] Mini-project — no logic outside a function except the `numbers` list and the `main()` call
- [x] Mini-project — `bubble_sort` returns a new list; the original is proven unchanged in the output
- [x] Mini-project — `search` returns only an index; `"Found at index X"` / `"Not found"` printed from `main()`
- [x] Mini-project — new file, Week 5 submission not modified
- [ ] Video reflection recorded and linked above
- [x] Mindset response written

## Mindset Response — Peer Collaboration

> *"Talk is cheap. Show me the code."* — Linus Torvalds

### 1. How is collaboration used in your own family/culture/current workplace/etc.?

In my family it's the default and nobody calls it collaboration. Something needs
doing, several people turn up, and the division of labour gets worked out on the
spot by whoever knows most about it. Nobody's assigned. It's also completely
verbal — you find out what's happening because you were in the room, not because
anyone wrote it down.

That's the part I've had to unlearn. The way I grew up working, knowledge lives
in people and gets passed on by being present. Software doesn't run that way.
The whole apparatus this course keeps pushing me toward — commit messages,
pull request descriptions, a README that explains itself — is collaboration with
people who *weren't* in the room, including me in three months. That was a
genuinely new idea to me and it took a while to stop feeling like paperwork.

Where I've seen the other model is open source, from the outside. I've read
issue threads to work out why something behaved oddly, and every bit of that was
people explaining themselves in writing to strangers. Torvalds' line is a bit
blunt but it's the same point: the artefact is what's shareable. What I
understood and didn't write down helps nobody.

### 2. What's one challenge you personally encounter while collaborating with others and what can you do to overcome the challenge?

I go quiet when I'm behind, which is precisely backwards.

It's happened twice in this course and both times the same way. Weeks 2 and 3
went in late, and as I slipped further I posted less, because turning up to say
"still not done" felt worse than saying nothing. The Week 2 fork confusion is
the clearest case — I'd misread which repository the work went in, spent days
looking for a folder that was never going to exist, and never once asked, since
asking meant admitting I was lost. One message would have cost a minute. It cost
days instead.

The pattern is that I treat being stuck as something to hide until it's fixed,
so nobody can correct me while correcting is still cheap. What I know now is
that the discomfort is worst right before you say it and basically gone
immediately after.

Two things I can actually do. One, a hard rule rather than a judgement call: if
I've made no progress in thirty minutes, or I'm re-reading an error I've already
read three times, I post it — unfinished, no tidying up first. Two, say the
uncomfortable thing early. "I'm behind on 7 and here's where I got stuck" is a
question someone can answer. Silence is not.

### 3. What's one topic you want to start collaborating with classmates on this week?

Git, easily. It's been the hardest part of this course for me by a wide margin
and none of it was the Python. Branches, what a fork actually is, which
repository a PR is opening against — I can follow the commands and I don't have
a picture of what they're doing, so when it goes sideways I'm guessing.

Concretely: I want to get on a screen share with someone and have us both
deliberately break things in a throwaway repo. Two branches editing the same
lines, merge them, sit with the conflict. Commit to `main` by accident and
recover it. I wrote in my Week 4 mindset response that I do branch-per-assignment
because I've been told to and have never hit the problem it solves. Causing the
problem on purpose, with someone who's already hit it, seems like the fastest
way to stop performing the ritual and start understanding it.

The other reason I want a person rather than an article is that I've read the
articles. What I'm missing isn't the definition of a merge conflict. It's having
seen one happen to somebody and watched what they did next.
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
