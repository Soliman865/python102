# Week 4 — File I/O and Data Persistence

Every program you've written so far forgets everything the moment it ends. This week fixes that: you'll learn to read data from a file and write data to a file, so `grocery_list`, `contacts`, and `class_records` survive after you close VS Code.

By the end of this week, your programs will save real data to disk — as plain text, as JSON, and as CSV — the same three formats real software uses to persist data.

## Files in this folder

| File | What it covers |
|---|---|
| `01_file_io.py` | Writing and reading text files, append vs. overwrite, saving/loading with JSON, reading/writing CSV files |
| `02_exercises.py` | Tasks to do on your own — grocery list, contact book, and grade book, now saved permanently, plus a bonus CSV attendance report |

## Read these in order

`01_file_io.py` has 5 programs, each building on the last. Run each one, then actually open the `.txt`, `.json`, and `.csv` files it creates in VS Code's file explorer — seeing the real file on disk is the point of this week, not just the printed output. Try the `CHALLENGE` at the end of each program before moving to `02_exercises.py`.

## What you need before starting

- Comfortable with: functions, `for` loops, lists, dictionaries, and lists of dictionaries (Weeks 1–3)
- Your Week 3 grocery list, contact book, and grade book exercises — you'll be upgrading all three this week
- Your GitHub repo, ready to `add`, `commit`, and `push` your work this week too

## The formats, in one line each

> **Plain text (`.txt`)** — just lines of text, good for simple lists like a grocery list.
> **JSON (`.json`)** — maps directly onto Python lists/dicts, best for structured data like `class_records`.
> **CSV (`.csv`)** — rows and columns, best for spreadsheet-style data like attendance.

If your data is a list of dictionaries — use JSON.
If your data looks like a spreadsheet — use CSV.
If it's just lines of text — plain `.txt` is enough.

## Looking ahead

Next week is Mini Project 1 — a Personal Data App. You'll build one complete program that reads its data from a file on startup and saves it back on exit, so it behaves like real software instead of a script that forgets everything every time it runs. Everything you practice this week — `load_*()` on startup, `save_*()` before quitting — is the exact pattern that project is built on.
