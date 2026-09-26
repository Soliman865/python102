# Week 4 — Teacher notes

Students start at `README.md`. This file is for you.

## Class plan (about 70 minutes)

Say this, then let them work:

> Python already has tools for math, random numbers, dates, and saving data. `import` loads them. Four activities. Lesson, then your turn. Stop when you see PASSED.

| Minutes | What you do |
|---------|-------------|
| 0–8 | Run `01_lesson.py` together. Point at `import math` and `math.sqrt`. |
| 8–20 | They do `01_your_turn.py`. |
| 20–35 | They do activity 2 on their own. The dice number changes every run. That is correct. |
| 35–48 | They do activity 3. The finished string must be exactly `2014-03-15`. |
| 48–65 | Run `04_lesson.py` together. This is the one week 5 needs. Point at `json.dump` and `json.load`. |
| 65–70 | Early finishers do activity 5. |

If a `week4_demo.json` or `week4_player_check.json` file is left in the folder, the activity crashed before cleanup. Delete it. Those names are in `.gitignore`.

## Answer key

Activity 1:

```python
return math.sqrt(number)
```

```python
return 2 * math.pi * radius
```

Activity 2:

```python
return random.randint(1, 6)
```

```python
return random.choice(snacks)
```

Activity 3:

```python
return birthday.strftime("%Y-%m-%d")
```

Activity 4, inside `save_player` (delete `pass`):

```python
with open(path, "w") as file:
    json.dump(player, file)
```

Inside `load_player` (delete `pass`):

```python
with open(path, "r") as file:
    return json.load(file)
```

Activity 5, inside `load_score` after the exists check:

```python
with open(path, "r") as file:
    return json.load(file)
```

## Stuck points to watch for

- They write `sqrt(256)` without `math.`
- Activity 2: `random.randint(1, 6)` includes both 1 and 6. A fixed `return 1` does not pass.
- Activity 3: missing dashes, or they print the date instead of returning it.
- Activity 4: they dump before the `with` block, or they forget `return` on load.
- If activity 2 fails and the code really uses `random.randint` and `random.choice`, run it once more. The check asks for more than one different result.
