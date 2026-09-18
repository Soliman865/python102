# Weeks 7-8: Building an AI Weather Mood App

You're going to build a Python app that fetches **live weather data** and displays it in
a window that changes colour based on the mood of the weather.
The AI writes most of the code — but you're going to build it **in small steps**, which
is how real developers use AI. One big prompt gives you one big blob you can't debug.
Four small prompts give you four pieces you understand.

## The 2-week build

| Week | You build | New idea |
|------|-----------|----------|
| 7 | A `weather.py` module — fetch live weather, parse JSON, handle errors | What an API is, how JSON works, incremental prompting |
| 8 | A Tkinter GUI on top — background colour + emoji change with the weather | Separating logic from display; catching AI mistakes in UI code |

---

## Before You Start (5 min)

1. Get a free API key at **[openweathermap.org](https://openweathermap.org/)** → Sign Up → API Keys
   No credit card. New keys take up to **10 minutes** to activate.
2. `pip install requests`

---

## Week 7: Build the Weather Module — 4 Steps

> **Rule for this week:** finish each step and confirm it works before moving to the next.
> Do not paste all 4 prompts at once.

---

### Step 1 — Fetch raw data and print it

**Prompt:**
> "Write a Python script that uses the requests library to fetch current weather for
> a hardcoded city ('London') from the OpenWeatherMap API. URL:
> `https://api.openweathermap.org/data/2.5/weather`
> Use params: q=London, appid=YOUR_KEY, units=metric.
> Print the full JSON response."

**When you get the code:**
- Replace `YOUR_KEY` with your actual API key, run it
- You should see a big JSON blob printed — find `temp` inside it
- Find `weather` in the JSON — is it a list or a dict? (This matters in Step 2)

> ⚠️ **Common AI mistake at this step:**
> The AI sometimes builds the URL by joining strings: `url = BASE_URL + "?q=" + city + "&appid=" + key`
> That works, but it's fragile and hard to read. Ask it: *"rewrite this to use a `params` dict with `requests.get`"*
> and compare both versions.

**Move to Step 2 when:** you can see `"temp"` in the printed output.

---

### Step 2 — Parse the JSON into a clean dict

**Prompt:**
> "Update the script so instead of printing the raw JSON, it extracts these fields
> into a Python dict and prints that:
> city (data['name']), country (data['sys']['country']), temp (data['main']['temp']),
> feels_like (data['main']['feels_like']), humidity (data['main']['humidity']),
> condition (data['weather'][0]['main']), description (data['weather'][0]['description']),
> wind_speed (data['wind']['speed']).
> Round temp and feels_like to 1 decimal place."

**When you get the code:**
- Run it. Print the dict and check all 8 keys are there.

> ⚠️ **Common AI mistake at this step:**
> The AI often writes `data['weather']['main']` — but `weather` is a **list**, not a dict.
> The correct path is `data['weather'][0]['main']`.
> If your code crashes with `TypeError: list indices must be integers`, this is why.
> Fix: add `[0]` after `data['weather']`.

**Move to Step 3 when:** you see a clean 8-key dict printed with no crash.

---

### Step 3 — Handle bad input

**Prompt:**
> "Update the script to handle two error cases:
> 1. If the city is not found (HTTP 404), raise a ValueError with the message
>    'City not found: {city}'
> 2. If the response is any other non-200 status, raise a RuntimeError with
>    'API error: HTTP {status_code}'
> Check status_code BEFORE calling .json(). Also wrap the call in try/except
> in the main block and print the error message instead of crashing."

**When you get the code:**
- Test with a real city → should work fine
- Test with `"xyzfakecity"` → should print the ValueError message, not crash

> ⚠️ **Common AI mistake at this step:**
> The AI often writes `except Exception as e:` — one catch-all. That hides the difference
> between "city not found" and "API key is wrong". Ask it to split it into two separate
> `except` blocks: `except ValueError` and `except RuntimeError`.
> Also check: does it check `status_code` BEFORE calling `.json()`? If `.json()` is called
> on a 404 response it works, but the data structure is different — the code will crash
> on a missing key later. Order matters.

**Move to Step 4 when:** a fake city prints a clean error and doesn't crash.

---

### Step 4 — Wrap it in reusable functions

**Prompt:**
> "Refactor the script into a module called weather.py with two functions:
> 1. get_weather(city) — takes a city string, returns the 8-key dict.
>    Raises ValueError for city not found, RuntimeError for other API errors.
> 2. get_mood(condition) — takes the condition string (e.g. 'Rain', 'Clear') and
>    returns a mood word: Clear→sunny, Clouds→cloudy, Rain/Drizzle→rainy,
>    Thunderstorm→stormy, Snow→snowy, Mist/Fog/Haze→foggy, anything else→unknown.
> Add an if __name__ == '__main__': block that asks the user for a city name,
> calls both functions, and prints the result."

**When you get the code:**
- Run `python weather.py` — enter your city, confirm all 8 fields print
- Enter a fake city — confirm `ValueError` is caught and printed, not a crash
- Check `get_mood("Tornado")` — does it return `"unknown"` gracefully?

> ⚠️ **Common AI mistake at this step:**
> The AI sometimes makes `get_weather` return `None` on error instead of raising.
> That means the caller gets `None` silently and crashes later with a confusing `NoneType` error.
> Check: does `get_weather("fakecity")` raise an exception, or return `None`?
> If it returns `None`, ask: *"change it to raise ValueError instead of returning None."*

**Week 7 checkpoint — before moving to Week 8:**
- [ ] `python weather.py` → enter a real city → see all 8 fields
- [ ] Enter a fake city → see a clean error message, no crash
- [ ] You can explain, out loud, why `data['weather'][0]['main']` needs the `[0]`
- [ ] You can explain why we check `status_code` before calling `.json()`

---

## Week 8: Build the GUI — 4 Steps

> `weather.py` is your foundation. Don't change it this week — the GUI imports it.
> If the GUI breaks, the bug is almost always in `app.py`, not `weather.py`.

Mood → colour + emoji table (use these exact hex values in your prompts):

| Mood | Emoji | Background |
|------|-------|------------|
| sunny | ☀️ | `#FFD97D` |
| cloudy | ☁️ | `#B0BEC5` |
| rainy | 🌧️ | `#5C9BD6` |
| stormy | ⛈️ | `#546E7A` |
| snowy | ❄️ | `#E3F2FD` |
| foggy | 🌫️ | `#CFD8DC` |
| unknown | 🌡️ | `#ECEFF1` |

---

### Step 5 — Build the window skeleton

**Prompt:**
> "Create app.py — a Tkinter window (420×520, not resizable) with:
> a text Entry box and a Search button at the top,
> a large emoji Label in the centre (font size 80),
> a temperature Label below (font size 42, bold),
> a city/country Label, and a description Label.
> Don't connect the button to anything yet — just make the window appear with placeholder text."

**When you get the code:**
- Run it. Does the window open?
- Click the button — nothing should happen yet (that's fine)

> ⚠️ **Common AI mistake at this step:**
> Missing `root.mainloop()` at the bottom — the window flashes and closes immediately.
> If that happens, add `root.mainloop()` as the last line.
> Also: if the button command is written as `command=on_search()` (with brackets),
> it runs the function immediately on startup instead of when clicked.
> It should be `command=on_search` (no brackets).

**Move to Step 6 when:** the window opens and stays open.

---

### Step 6 — Connect the Search button

**Prompt:**
> "Connect the Search button to a function called on_search.
> When clicked: get the text from the Entry box, call get_weather() from weather.py,
> call get_mood() on the condition, and print the result to the console for now.
> Wrap the call in try/except: catch ValueError and RuntimeError separately and print
> each error to the console."

**When you get the code:**
- Search for a real city — do you see the dict printed in the terminal?
- Search for a fake city — do you see the error message in the terminal (not a crash)?

> ⚠️ **Common AI mistake at this step:**
> The AI sometimes puts `import weather` at the top but then calls `weather.get_weather()`
> instead of the imported function. Or it copies the get_weather logic INTO app.py,
> creating a duplicate. Check: is `weather.py` actually being imported and used?
> If the code works without `weather.py` existing, it's a duplicate — ask the AI to
> delete the copy and import from weather instead.

**Move to Step 7 when:** a real city prints a result in the terminal; a fake city prints an error.

---

### Step 7 — Update the display

**Prompt:**
> "Now instead of printing to the console, update the Tkinter labels and window background:
> - Set the window background and ALL label backgrounds to the mood colour
> - Set the emoji label text to the mood emoji
> - Set the temperature label to '{temp}°C'
> - Set the city label to '{city}, {country}'
> - Set the description label to the description
> Use this mood→colour+emoji mapping: [paste the table above]"

**When you get the code:**
- Search for a city — does the whole window change colour?
- Search for another city — does it change to a different colour?

> ⚠️ **This is the most common AI mistake in this whole project:**
> The AI almost always updates `root.config(bg=colour)` but forgets to update
> **every individual label's** `bg` too. Labels have their own background colour.
> If you see grey boxes behind the temperature or description text, that's the bug.
> Check: does the code call `.config(bg=colour)` on root AND on every label?
> Ask: *"make sure every Label widget's bg is also updated to match the window background."*

**Move to Step 8 when:** the whole window — including all text labels — changes colour with no grey boxes.

---

### Step 8 — Add error display in the UI

**Prompt:**
> "Add an error Label widget below the description.
> When ValueError is caught, show 'City not found.' in red in that label.
> When RuntimeError is caught, show 'API error — try again.' in red.
> When a search succeeds, clear the error label.
> Make sure the error label's background matches the window background."

**When you get the code:**
- Search a fake city — does the red error message appear in the window?
- Search a real city after that — does the red message disappear?

> ⚠️ **Common AI mistake at this step:**
> The error label often has a hardcoded white background (`bg='white'`).
> That creates a white box when the window is a different colour.
> Also: the AI sometimes forgets to clear the error label on a successful search —
> so the red message stays even after you find a valid city.
> Check both cases and fix with a targeted follow-up prompt if needed.

**Week 8 checkpoint — you're done when:**
- [ ] Searching 5 different cities each shows a different mood colour
- [ ] A fake city shows a clean red error in the window — no crash, no grey boxes
- [ ] You can trace one search out loud: Entry → button click → get_weather → get_mood → which label gets updated
- [ ] You can explain why `weather.py` and `app.py` are separate files

---

## Reference Files

`weather.py` and `app.py` in this folder are reference implementations.
Build your own with the prompts above first. If you get stuck, compare your AI's
version line by line against the reference — don't just copy it.

---

## Push your work

```bash
git add .
git commit -m "Week 7/8 - weather module + mood GUI"
git push
```
