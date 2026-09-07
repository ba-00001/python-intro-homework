# Assignment 9 — Video Reflection Script

**Target length:** 3–5 minutes (this script runs ~4:35 spoken at a normal pace).
**Setup:** screen share of the editor, a terminal in `week-9/assignment-9/` with
the venv active, and a browser. Webcam for the intro, the mindset section and
the close.

**Before you hit record**

- Terminal cleared, inside `week-9/assignment-9/`, venv active (`(.venv)` visible).
- **You need a live internet connection.** Run `mini_project.py` once before
  recording to confirm the World Bank API is responding and to warm the terminal.
- Browser tabs, in this order — you'll flip through them during the API
  substitution section:
  1. `https://restcountries.com/v3.1/all` — shows the deprecation body live
  2. `https://api.worldbank.org/v2/country?format=json&per_page=5` — shows the
     `[metadata, [rows]]` wrapper
  3. `https://api.agify.io/?name=michael`
- Editor tabs: the four warmups and `mini_project.py`.
- Decide your live inputs for the mini-project: option **1**, search **land**
  (finds Finland, Iceland, Ireland, Poland, Switzerland, Thailand); then option
  **2**, region **north america**; then **3**.

---

## 0:00 – 0:25 · Intro (webcam)

> Hey, I'm Brian Bazurto, and this is my reflection for Assignment 9 of Python
> Intro 26.3 with Code the Dream. This week was external libraries and APIs —
> `requests`, JSON, and navigating dictionaries inside lists inside dictionaries.
> Four warmups and a Country Explorer CLI.
>
> There's one thing I have to explain up front, because it changed the assignment:
> the API the course specifies stopped working during the course.

*(Switch to screen share, browser.)*

---

## 0:25 – 1:10 · The API substitution (screen: browser)

*(Open the restcountries v3.1 tab.)*

> The assignment names `restcountries.com/v3.1` for warmup 3 and the mini-project.
> Here it is, live. Notice **the status is 200** — and the body is this:

```json
{"success": false, "data": null,
 "errors": [{"message": "This API version has been deprecated..."}]}
```

> No country data. And the v5 replacement requires an API key —
> `Authorization: Bearer` — so it's no longer a keyless public API and doesn't fit
> the assignment's brief.

*(Switch to the World Bank tab.)*

> So I substituted the **World Bank Indicators API**. Keyless, no registration,
> and it carries all four required fields — name, capital, region and population.
> Warmups 1 and 2 still use Agify, exactly as the assignment specifies.
>
> And honestly, this turned out to be the most useful thing that happened to this
> assignment. An endpoint that returns **200 with no data in it** is the cleanest
> possible argument for why checking the status code alone isn't enough. It's the
> reason my fetch function validates the *shape* of the response too, and I'd
> never have thought to do that if the API had just worked.

---

## 1:10 – 1:40 · Warmups 1 and 2 — the request, and `.get()`

*(Open `warmup1.py` and run it.)*

> Warmup 1 is the first request. `requests.get()` sends an HTTP GET and waits.

*(Highlight `timeout=10`.)*

> The timeout isn't in the assignment, but without it a server that never answers
> hangs the script forever rather than raising something I can catch.
>
> I print the status separately from the body, because a request can come back
> "successfully" with a status saying the data isn't there — 404, 500 — and
> `.json()` on that gives you an error body, not your data. `.json()` parses into
> Python objects: a JSON object becomes a dict, a JSON array becomes a list. From
> there it's the same data structures as the last few weeks.

*(Open `warmup2.py`, highlight the `.get()` line.)*

> Warmup 2 pulls out individual fields — including one that doesn't exist.
> `data["birthday"]` would raise `KeyError`, because Agify never returns that.
> `.get()` returns a default instead of raising.
>
> And that's *the* reason `.get()` is the right tool for API data specifically: I
> don't control this response. A field being missing is a normal thing about
> somebody else's server, not a bug in my code.

---

## 1:40 – 2:10 · Warmup 3 — the nested wrapper

*(Switch to the World Bank browser tab, then open `warmup3.py`.)*

> Warmup 3 loops through a JSON list. Look at the shape in the browser first — the
> top level is a **two-item list**: `[0]` is pagination metadata and `[1]` is the
> actual list of countries. So the data I want is one level deeper than it looks.
> That's exactly the "dicts inside lists inside dicts" navigation this week is
> about.

*(Highlight the `region=ECS` query parameter.)*

> I pass `region=ECS` as a query parameter so the **server** does the filtering and
> sends back less data, rather than me downloading everything and throwing most of
> it away.
>
> And `[:10]` slicing is safe past the end — if the region had only four countries
> this quietly gives four rather than raising `IndexError`.

---

## 2:10 – 2:35 · Warmup 4 — two different failures

*(Open `warmup4.py` and run it.)*

> Warmup 4 deliberately points at a hostname that can't resolve, so the request
> fails before any HTTP happens at all.

*(Highlight `except requests.exceptions.RequestException`.)*

> `RequestException` is the **base class** for requests' own errors, so this one
> clause covers ConnectionError, Timeout, TooManyRedirects and the rest. Catching
> the base class is right here because the user's next step is the same for all of
> them: check the connection and retry.
>
> And then there's a **second** check, in the `else`. A response arriving is not
> the same as a response being useful. Those are two genuinely different failures
> and they need two guards — which is the lesson the deprecated API taught the
> hard way.

---

## 2:35 – 3:40 · Mini-project — Country Explorer, and the bug (screen)

*(Open `mini_project.py`.)*

> The mini-project is an interactive menu over live country data.

*(Scroll to `fetch_json`.)*

> `fetch_json` does one job — one GET — and it has **three** ways of failing, in
> order: never reached the server, reached it but the status isn't 200, and got a
> 200 whose *shape* is wrong. That third check is the one the deprecation bought
> me.
>
> The trade-off with the World Bank API is that name, capital and region come from
> one endpoint and population from another, so this script fetches both and joins
> them.

*(Scroll to `fetch_populations`, highlight the `countryiso3code` line.)*

> And here's the bug I want to talk about, because I actually shipped it first
> time. The population rows carry `row["country"]["id"]`, which looks like the
> obvious key to join on. It isn't — that's a different World Bank code, things
> like `"ZH"` and `"1A"`. The other endpoint's `"id"` is the ISO3 code.
>
> So joining on the wrong `id` matched **nothing**, and every population came out
> as **zero**. Silently. Because `.get(key, 0)` did exactly what I told it to —
> return the default when the key isn't there. The defensive habit I'd learned
> last week is precisely what hid the bug: 217 countries loaded, no error, every
> population zero.

*(Highlight the aggregates filter.)*

> One more real-data detail: the World Bank list includes aggregate rows like
> "Arab World" and "Euro area", which aren't countries. They're all marked with
> the region "Aggregates", so filtering on that leaves only real ones.

```bash
python3 mini_project.py
```

*(Option 1, search `land`.)*

> Search is a **substring** test, so `land` finds Finland, Iceland, Ireland,
> Poland, Switzerland and Thailand — that's `in` on strings doing partial matching.

*(Option 2, region `north america`.)*

> Region filter is partial too, so `europe` matches "Europe & Central Asia"
> without me knowing the World Bank's full region name — and it's sorted by
> population, largest first, with `sorted()` returning a **new** list rather than
> reordering the caller's.

*(Point at a population figure.)*

> And `:,` in the f-string gives the thousands separators.

---

## 3:40 – 4:20 · Mindset — accessibility (webcam)

> The mindset question was about accessibility, and the version of it I've
> actually lived is bandwidth. For a long stretch I had a connection that was slow
> and unreliable rather than absent — which is its own particular problem, because
> everything technically worked and nothing worked well. Large downloads failed at
> 80% and started again. Pages built assuming a fast connection would sit blank,
> because a spinner is all you get when the JavaScript that draws the content
> hasn't arrived.
>
> I reorganised around it — queue downloads overnight, keep documentation locally,
> prefer text over anything that streamed. Some of that is still habit.
>
> The part I'd underline is that nobody building those sites thought of themselves
> as excluding me. They had a fast connection, it worked when they tested it, and
> their site was unusable for me anyway. Nobody decided that. It just happened.
>
> Which reframed accessibility for me — I'd been treating it as a checklist you
> apply to a finished thing. It's closer to a set of assumptions you make at the
> start and never notice you've made. The `timeout` in this week's code is a small
> version of the same idea: I only put it there because I've been the person on
> the end of a connection that doesn't answer.

---

## 4:20 – 4:35 · Close (webcam)

> So that's Assignment 9. Two things I'm taking forward: a 200 doesn't mean you
> got your data, and a safe default can hide a bug just as well as it prevents a
> crash. Everything's linked in the submission README, including the full write-up
> on the API substitution. Thanks for watching.

---

## Delivery notes

- Lead with the API substitution. It's the first thing a reviewer will wonder
  about, and showing the live deprecation body answers it in twenty seconds.
- The "every population came out zero" bug is the best moment in this video —
  it shows real debugging on real data. Give it the time.
- Check the API is up right before you record. If it's down, say so on camera and
  walk the code instead; don't fake output.
- Under 3:00 reads as thin; over 5:00 gets cut off. Time your first take.

---

## Video URL

Upload to YouTube (unlisted) or Loom, then paste the link here and in the two
other places it is needed.

**Video URL:** `VIDEO_URL_HERE`

| Also paste it into | Where |
| --- | --- |
| Submission README `URL2` row | [README.md](README.md) |
| Pull request description | [python-intro-homework#8](https://github.com/ba-00001/python-intro-homework/pull/8) |
| Course index video table | [main README](https://github.com/ba-00001/brian-bazurto-python/blob/main/README.md#video-reflections) |
