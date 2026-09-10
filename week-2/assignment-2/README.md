# Assignment 2 — CLI & Professional Environment

Week 2 of Python Intro 26.3. Everything required for this assignment lives in
this folder.

## Submission links

| Field | Link |
|-------|------|
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/1 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Mindset Response** | [see below](#mindset-response--ai-for-learning) |

## Required files

| File | What it does |
|------|--------------|
| [warmup1.py](warmup1.py) | Prints `Python is working!`; header comment records the terminal command and its output |
| [warmup2.py](warmup2.py) | Header comment lists the `cd` / `ls` / `pwd` commands used to reach this folder; asks for today's date and echoes it back |
| [warmup3.py](warmup3.py) | Header comment holds real `git log --oneline` output; prints what I learned this week |
| [warmup4.py](warmup4.py) | Deliberate `TypeError` bug, the real traceback, the cause, and the fix — then the corrected code |
| [mini_project.py](mini_project.py) | Fahrenheit → Celsius converter, rounded to one decimal with an f-string |

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
Python is working!

$ python3 mini_project.py
Enter a temperature in Fahrenheit: 72
72.0°F is 22.2°C.
```

## Requirements checklist

- [x] Warmup 1 — prints the message, command and output recorded as comments
- [x] Warmup 2 — navigation commands recorded, `input()` echoed in a sentence
- [x] Warmup 3 — real `git log --oneline` output pasted, second script committed
- [x] Warmup 4 — error message pasted, cause and fix explained
- [x] Mini-project — conversion done by hand, f-string output, one decimal place
- [ ] Video reflection recorded and linked above
- [x] Mindset response written

## Mindset Response — AI for Learning

> *"Artificial intelligence is not a substitute for human intelligence; it is a
> tool to amplify human creativity and ingenuity."* — Fei-Fei Li

### 1. Have you ever used any AI tools (ex. chatGPT, Grammerly, Dall-E, etc.)? If yes, what did you use it for? If no, did you choose not to use AI, or you just haven't explored it/aren't aware of how to use it?

Yes, a lot. I use AI coding assistants most days on my own projects, and I run
some smaller models locally for the low-stakes stuff so I'm not paying for
things that don't need to be good. Outside of code: summarising long
documentation, first drafts of writing that I then rewrite, and working out what
an error message actually means.

The main thing all that use has taught me is where it stops being reliable.
I've been given answers that sounded completely confident and were just wrong. A
function that doesn't exist. A flag that got removed a couple of versions back.
Nothing in how it was written warned me. So I treat what it tells me as a lead
rather than a fact — if I can't run it, or find it in the real documentation, I
don't rely on it. I learned that by getting caught out, not by being sensible up
front.

### 2. What are ways you think AI can help you as you learn content throughout this class?

The thing I find genuinely useful is asking why rather than what. When a
traceback means nothing to me, having it put in plain English — Python is
telling you it can't subtract text from a number — gets me unstuck without
giving me the answer. I still have to go and fix it myself.

Other things: making extra practice problems on something I'm shaky on, since
the assignment only gives you one go at each idea. Having it look at code I've
already written and asking what I'd change. And being able to ask something
basic at 1am without using up a mentor's time on it. That last one is bigger
than it sounds. Plenty of small confusions never get asked because they feel too
stupid to ask, and those are the ones that pile up.

Sal Khan's point in the interview is roughly the same idea. The useful version
behaves like a tutor that asks you things, not an answer key that ends the
conversation.

### 3. What are ways that AI can cause frustration or negatively impact your learning?

What worries me isn't wrong answers, it's right ones turning up too early. The
bit where you're stuck is the bit where you learn, and a working answer skips
straight past it. Reading a correct solution feels a lot like understanding it,
and that feeling does not survive sitting in front of an empty file a week
later. I've definitely nodded along to code I couldn't have written and couldn't
debug.

The other problem is that it answers at the wrong level. Ask a general question
and you get something idiomatic back — comprehensions, error handling, patterns
we haven't covered. It works. I can't explain it, which makes it useless for a
video reflection and worse than useless when it breaks.

So the rule I've set myself for this course is that I don't hand in code I
couldn't have written, and I use it to explain rather than to write. If I'm
about to paste something in without understanding it, that's my signal I've
skipped something and need to go back rather than forward.

## All assignments

| # | Topic | Submission README | Pull request |
| --- | --- | --- | --- |
| 1 | Python Basics | [assignment-1](https://github.com/ba-00001/brian-bazurto-python/blob/assignment-1/assignment-1/README.md) | [brian-bazurto-python#1](https://github.com/ba-00001/brian-bazurto-python/pull/1) |
| 2 | CLI & Professional Environment | this page | [python-intro-homework#1](https://github.com/ba-00001/python-intro-homework/pull/1) |
| 3 | Control Flow | [week-3/assignment-3](https://github.com/ba-00001/python-intro-homework/blob/assignment-3/week-3/assignment-3/README.md) | [python-intro-homework#2](https://github.com/ba-00001/python-intro-homework/pull/2) |
| 4 | Core Data Structures | [week-4/assignment-4](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/README.md) | [python-intro-homework#3](https://github.com/ba-00001/python-intro-homework/pull/3) |
| 5 | Iteration & Algorithms | [week-5/assignment-5](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/README.md) | [python-intro-homework#4](https://github.com/ba-00001/python-intro-homework/pull/4) |
