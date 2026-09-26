# Week 3 — Teacher notes

Students start at `README.md`. This file is for you.

## Why this shape

Same rule as week 2: one idea, one lesson, one your-turn, done when it prints `PASSED`. No blank "write a whole program" block. No `input()` loops, so they can run the file and see the result immediately.

`else`, `finally`, and chained exceptions are not in today's activities.

## Class plan (about 70 minutes)

Say this, then let them work:

> An exception is an error that stops the program. Today we catch some errors, and we create one on purpose when a score is not allowed. Four activities. Lesson, then your turn. Stop when you see PASSED.

| Minutes | What you do |
|---------|-------------|
| 0–8 | Run `01_lesson.py` together. Point at `try` and `except ValueError`. Say the second call would have crashed, and the program kept going. |
| 8–20 | They do `01_your_turn.py`. |
| 20–25 | Run `02_lesson.py`. Say the word after `except` is the error's name. `IndexError` is the wrong spot in a list. |
| 25–40 | They do `02_your_turn.py`. |
| 40–48 | Run `03_lesson.py`. Say `raise` means "stop and report this problem." |
| 48–58 | They do `03_your_turn.py`. |
| 58–70 | They do activity 4. Early finishers do activity 5. |

If the class is slow, stop after activity 3. Activity 4 still belongs to this week.

## Answer key

Activity 1, inside `try`:

```python
return int(text)
```

Activity 2, inside `try`:

```python
return items[index]
```

Activity 3, inside the `if`:

```python
raise ValueError("Score must be a positive number.")
```

Activity 4, inside the `if`:

```python
raise InvalidScoreError("Score must be a positive number.")
```

Activity 5, inside `try`:

```python
with open(filename, "r") as file:
    return file.read()
```

## Stuck points to watch for

- They edit the lesson file. Point them at `your_turn`.
- The new line is not indented under `try`. It must line up with the `TODO` comment.
- Activity 3: they print a message instead of `raise`, so the bad score still gets stored.
- Activity 4: they `raise ValueError` again. The "not yet" message tells them the class name to use.
- Activity 5: they forget `return`, so a real file still comes back as `None`.
