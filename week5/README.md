# Week 5 – Mini Project 1: Personal Data App (without AI)

## Objective
Consolidate Weeks 1-4 (Python/VS Code, Git/GitHub, Lists & Dictionaries,
File I/O) into one working CLI app before AI is introduced in Week 6.
No new syntax this week — the goal is fluency and confidence combining
what they already know.

## Class flow (60-75 min)

| Time | Activity |
|------|----------|
| 0-10 min | Recap: what's a list of dicts, why do we save to a file? Draw the Contact Book's data flow on the whiteboard (load → menu loop → save). |
| 10-40 min | Live-code `lesson.py` together (Contact Book). Type it out, don't paste — run it after every function so they see incremental progress. |
| 40-45 min | `git add / commit / push` the working Contact Book to their own repo (reinforces Week 2). |
| 45-70 min | Hand out `exercise.py` (Habit Tracker). Students work independently/pairs. Circulate. |
| 70-75 min | Wrap up: 1-2 students demo their tracker. Assign finishing the exercise for next class if incomplete. |

## Key concepts reinforced
- List of dictionaries as a simple "database"
- `json.dump` / `json.load` for persistence
- Menu-driven `while True` loop with `input()`
- Defensive input handling (`try/except` on `int()` and index access)
- Functions that take `contacts`/`habits` as a parameter and mutate it in place

## Common student errors to watch for
- Forgetting to call `save_*()` after add/delete → changes don't persist
- Off-by-one on `choice - 1` when converting menu number to list index
- Not guarding against an empty list before indexing (`contacts[0]` on `[]`)
- Leaving `habits.json` from a previous run in the folder and being confused why old data reappears — good moment to explain persistence is a feature, not a bug

## Files
- `lesson.py` — Contact Book, built together in class
- `exercise.py` — Habit Tracker starter with 7 TODOs, same pattern as lesson.py
- `solution.py` — reference solution to exercise.py

## Note for next week
Week 6 introduces AI concepts. Make sure every student leaves this class
with a working save/load loop — Week 9's Mini Project 2 builds an
API + GUI app directly on this pattern.
