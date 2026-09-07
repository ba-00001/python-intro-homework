# Assignment 9 — External Libraries & APIs

Week 9 of Python Intro 26.3. Everything required for this assignment lives in
this folder.

## Submission links

| Field | Link |
|-------|------|
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/8 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Video script** | [VIDEO-SCRIPT.md](VIDEO-SCRIPT.md) |
| **Mindset Response** | [see below](#mindset-response--accessibility) |

## ⚠️ API substitution — please read

The assignment specifies `restcountries.com/v3.1` for Warmup 3 and the
mini-project. **That API was deprecated and no longer returns country data.**
It now answers with HTTP **200** and this body:

```json
{"success": false, "data": null,
 "errors": [{"message": "This API version has been deprecated. Please visit
   https://restcountries.com/docs/countries/legacy-api-deprecation to migrate
   to our new version (v5)."}]}
```

Its v5 replacement **requires an API key** (`Authorization: Bearer YOUR_KEY`),
so it is no longer a keyless public API and doesn't fit the assignment's brief.

I substituted the **World Bank API**, which is keyless, needs no registration,
and carries all four required fields:

| Endpoint | Provides |
|---|---|
| `api.worldbank.org/v2/country?format=json&per_page=400` | name, `capitalCity`, `region.value` |
| `api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&mrnev=1` | latest population per country |

Warmups 1 and 2 still use **Agify**, exactly as the assignment specifies.

Two things this cost, both of which turned out to be worth having:

1. **The data needs joining.** Population lives on a different endpoint, so
   `mini_project.py` fetches both and merges them on the ISO3 code.
2. **A 200 is not a success.** The deprecated endpoint is the perfect
   demonstration of why checking `status_code` alone isn't enough — it returned
   200 with no data in it. `fetch_json()` validates the response *shape* as
   well as the status.

## Required files

| File | What it does |
|------|--------------|
| [warmup1.py](warmup1.py) | `requests.get()` on Agify; prints status code and full JSON |
| [warmup2.py](warmup2.py) | Pulls `name`/`age` by key; `.get()` with a fallback for the absent `birthday` |
| [warmup3.py](warmup3.py) | Loops a JSON list of countries in one region, printing the first 10 |
| [warmup4.py](warmup4.py) | `except requests.exceptions.RequestException` plus a non-200 status check |
| [mini_project.py](mini_project.py) | Country Explorer CLI — menu loop, name search, region filter, joined from two endpoints |
| [requirements.txt](requirements.txt) | `pip freeze` — `requests` and its dependencies |

`.venv/` is gitignored.

## How to run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 warmup1.py
python3 warmup2.py
python3 warmup3.py
python3 warmup4.py
python3 mini_project.py
```

## Sample output

Agify's numbers move as its dataset grows, so these differ from the
assignment's sample — that's live data, not a bug.

```
$ python3 warmup1.py
Status code: 200
Response: {'count': 311558, 'name': 'michael', 'age': 57}

$ python3 warmup2.py
Name: michael
Predicted age: 57
Birthday: Not available

$ python3 warmup3.py
Region has 58 countries. First 10:
Albania
Andorra
Armenia
Austria
Azerbaijan
Belgium
Bulgaria
Bosnia and Herzegovina
Belarus
Switzerland

$ python3 warmup4.py
Error: Could not reach the server. Check your connection and try again.
(Details: ConnectionError)
```

Mini-project, searching `land` then filtering by `europe`:

```
$ python3 mini_project.py
Fetching country data from the World Bank API...
Loaded 217 countries.

=== Country Explorer ===
1. Search by name
2. Filter by region
3. Quit
Choose an option (1-3): 1
Search: land
Switzerland — Capital: Bern | Region: Europe & Central Asia | Population: 9,092,436
Channel Islands — Capital: N/A | Region: Europe & Central Asia | Population: 168,466
Finland — Capital: Helsinki | Region: Europe & Central Asia | Population: 5,646,436
Ireland — Capital: Dublin | Region: Europe & Central Asia | Population: 5,484,367
Iceland — Capital: Reykjavik | Region: Europe & Central Asia | Population: 392,404
Netherlands — Capital: Amsterdam | Region: Europe & Central Asia | Population: 18,087,633
Poland — Capital: Warsaw | Region: Europe & Central Asia | Population: 36,435,861
Thailand — Capital: Bangkok | Region: East Asia & Pacific | Population: 71,619,863
...
(18 results)

Choose an option (1-3): 2
Region: europe
Russian Federation — Capital: Moscow | Region: Europe & Central Asia | Population: 143,513,328
Turkiye — Capital: Ankara | Region: Europe & Central Asia | Population: 85,878,556
Germany — Capital: Berlin | Region: Europe & Central Asia | Population: 83,491,249
United Kingdom — Capital: London | Region: Europe & Central Asia | Population: 69,487,000
France — Capital: Paris | Region: Europe & Central Asia | Population: 68,720,337
...
```

`Channel Islands` is the missing-capital case — the API returns an empty string
and the program shows `N/A` instead of a blank column.

## A bug worth recording

The first version joined the two endpoints on `row["country"]["id"]` and every
population came out `0`. Both endpoints have a field called `id`, but they
aren't the same identifier — the country list uses ISO3 (`CHE`) while the
population rows put a World Bank code (`ZH`, `1A`) in `country.id` and keep
ISO3 in `countryiso3code`. Joining on the wrong one matched nothing and failed
*silently*, because `.get(key, 0)` did exactly what I told it to.

Fixing it meant printing both key sets side by side and comparing them. The
lesson is the one from Week 8: a default value stops a crash, and in doing so
it can hide that the lookup never worked. The comment in `fetch_populations()`
records this so I don't repeat it.

## Requirements checklist

- [x] Warmup 1 — `requests.get()`, prints status code and full JSON response
- [x] Warmup 2 — `name` and `age` accessed by key; `.get()` used to avoid `KeyError` on `birthday`
- [x] Warmup 3 — loops a JSON list, prints country names, limited to the first 10
- [x] Warmup 4 — `try`/`except requests.exceptions.RequestException`, plus a non-200 status check
- [x] Mini-project — fetches at start, parses into a list of dicts with name, capital, region, population
- [x] Mini-project — menu in a `while` loop with the three specified options
- [x] Mini-project — case-insensitive partial name search, printing capital, region and population
- [x] Mini-project — region filter sorted by population, largest first
- [x] Mini-project — missing capital shown as `N/A` rather than crashing
- [x] Mini-project — initial request wrapped in `try`/`except` with a status check; exits with a message on failure
- [x] `requirements.txt` up to date with `requests`
- [ ] Video reflection recorded and linked above
- [x] Mindset response written

## Mindset Response — Accessibility

> *"The power of the Web is in its universality."* — Tim Berners-Lee

### 1. When you've had limited or no access to something, what did you do? If you weren't able to access something you needed, how did this impact your life?

The one that shaped most of how I work now was bandwidth. For a long stretch I
had a connection that was slow and unreliable rather than absent, which is its
own particular problem — everything technically worked and nothing worked well.
Large downloads failed at 80% and started again. Video calls dropped. Pages
built on the assumption of a fast connection would sit blank, because a
spinner is all you get when the JavaScript that draws the actual content hasn't
arrived.

What I did was reorganise around it. Queue downloads overnight. Keep
documentation locally instead of looking things up. Prefer text over anything
that streamed. Some of that turned into habits I still have — I run local
models for low-stakes work partly because I stopped trusting a connection to be
there when I needed it.

The impact was mostly that things took longer and I did less of them. Not
dramatic, just steady friction. And the part I'd underline is that nobody
building those sites thought of themselves as excluding me. They had a fast
connection, it worked when they tested it, and their site was unusable for me
anyway. Nobody decided that. It just happened, which is the thing that stuck
with me.

### 2. Now that you've read about accessibility, and hopefully considered some of the challenges others face using the internet, are there things you can/will do differently in your current/future project(s)? Give examples.

Yes — and reading the WebAIM material reframed it for me. I'd been thinking of
accessibility as a checklist you apply to a finished website. It's closer to a
set of assumptions you make at the start, most of which you never notice you've
made.

Concretely, for the projects I'm actually working on:

**The CLI tools from this course.** It's tempting to say accessibility doesn't
apply to a terminal program, but it does, and it's mostly free. This week's
Country Explorer prints one country per line as plain labelled text — `Finland
— Capital: Helsinki | Region: ...`. A screen reader can read that. If I'd got
clever and drawn an ASCII table with box characters it would look tidier to me
and be close to unreadable aloud. I also don't rely on colour anywhere, and
every error says what to do rather than just what went wrong. `N/A` for a
missing capital rather than a blank gap is the same idea — the absence is
stated, not just left as empty space someone has to infer.

**The language-learning project.** This is where I've got the most to fix. It
leans on audio for pronunciation with no transcripts, which makes those
exercises useless to anyone deaf or hard of hearing. Adding text alongside
every clip is not hard and I simply hadn't thought about it. Timed exercises
are the other one — a countdown assumes a certain speed of reading and motor
response, and there's no reason it can't be adjustable or off.

**Habits rather than features.** Real text instead of text baked into images.
Actual alt text, describing the content rather than "image1.png". Checking
contrast with a tool instead of trusting my own eyes on a good monitor.
Keyboard navigation working before I touch any styling.

The connection back to my own experience is direct. Bad bandwidth taught me
that a thing being technically functional and a thing being usable are
different questions, and that the person building it is the last one likely to
notice the gap. Which means the answer can't be to rely on noticing. It has to
be testing with a tool, and asking people who aren't me.
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
