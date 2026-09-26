# Week 5 — Teacher notes

Students start at `README.md`. This file is for you.

## Class plan (about 70 minutes)

Say this, then let them work:

> Today you build a high score tracker in five small pieces. Same rule as the last two weeks: lesson, then your turn, stop at PASSED. After all five pass, you run the finished app and follow the steps.

| Minutes | What you do |
|---------|-------------|
| 0–8 | Run `01_lesson.py` together. Point at `self.scores` and `max`. |
| 8–18 | They do `01_your_turn.py`. |
| 18–30 | They do activity 2. This is week 3's `raise` again. |
| 30–42 | They do activity 3. Each score is now a dict with `value` and `date`. |
| 42–55 | Run `04_lesson.py` together. This is week 4's `json` again. |
| 55–65 | They do activity 5, then start `05_app.py` if time remains. |
| Last 10 | Walk through the app steps together if most of the room has not started it. |

Activities 1 to 4 are the project. Activity 5 and the app are the payoff. If the class is slow, stop after activity 4 and demo `05_app.py` yourself.

`scores.json` is created when they play the app. It is gitignored. They can delete it to start fresh.

## Answer key

Activity 1, inside `best_score`:

```python
if len(self.scores) == 0:
    return 0
return max(self.scores)
```

Activity 2, inside the `if`:

```python
raise ValueError("Score must be a positive number.")
```

Activity 3, inside `add_score` (delete `pass`):

```python
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
entry = {"value": value, "date": date}
self.scores.append(entry)
```

Activity 4, inside `save_all` (delete `pass`):

```python
with open(path, "w") as file:
    json.dump(data, file, indent=2)
```

Activity 5, inside the loop:

```python
if player.best_score() > best_value:
    best_value = player.best_score()
    best_player = player
```

## Stuck points to watch for

- Activity 1: they call `max` on an empty list. The `if len(self.scores) == 0` line has to come first.
- Activity 3: they append the number instead of the dict, then `best_score` crashes. Point at the three lines in the lesson.
- Activity 4: `json.dump` must be inside `with open`. The list to save is named `data`.
- The app asks for input. They need to click the terminal and type there, then press Enter.
