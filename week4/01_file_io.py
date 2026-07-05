# 01 – File I/O and Data Persistence
# Math+Coding Academy | Python102
#
# You already know: variables, functions, loops, and — from last week —
# lists, dictionaries, and lists of dictionaries like class_records.
#
# Problem: every program you've written so far forgets everything the
# moment you close it. Run it again and grocery_list, contacts, and
# class_records all start over empty. This week fixes that.
#
#   FILE I/O  — reading data from a file, and writing data to a file,
#               so it survives after your program ends.
#
# We'll go from the simplest possible case (writing plain text) up to
# saving a full list of dictionaries — exactly like class_records from
# Week 3 — and loading it back exactly as it was.
#
# Work through each program. Run it, then open the file it creates in
# VS Code's file explorer to see what actually got written to disk.

# ===========================================================
# PROGRAM 1 – Writing a file
# ===========================================================
# open(filename, mode) gives you a file object. "w" means WRITE —
# it creates the file if it doesn't exist, and ERASES it if it does.
#
# The "with" block automatically closes the file for you when it's
# done, even if something goes wrong. Always use "with" to open files.

with open("notes.txt", "w") as f:
    f.write("Week 4 - File I/O\n")
    f.write("This line was written by Python.\n")

print("Wrote notes.txt — check the file explorer in VS Code.")

# CHALLENGE: Change the code to write 3 of your own lines to a file
# called about_me.txt. Run it, then open about_me.txt in VS Code
# to confirm it worked.

# ===========================================================
# PROGRAM 2 – Reading a file back
# ===========================================================
# "r" means READ. If the file doesn't exist, this crashes with
# FileNotFoundError — the file must already exist.

with open("notes.txt", "r") as f:
    contents = f.read()   # reads the WHOLE file as one string

print("\n=== Whole file at once ===")
print(contents)

# Usually you want to work line by line instead. A file object can be
# looped over directly, one line at a time — just like looping over a
# list. Each line still has its "\n" at the end, so we .strip() it.

print("=== Line by line ===")
with open("notes.txt", "r") as f:
    for line in f:
        print("LINE:", line.strip())

# CHALLENGE: Read about_me.txt back and print only the SECOND line
# you wrote (hint: read all lines into a list with .readlines(),
# then index into it like a list).

# ===========================================================
# PROGRAM 3 – Write vs. append, and building lines from a list
# ===========================================================
# "w" ERASES the file first. "a" means APPEND — it adds to the end
# of the file without erasing what's already there.

def save_grocery_list(items, filename="groceries.txt"):
    """Overwrite the file with the current grocery list, one item per line."""
    with open(filename, "w") as f:
        for item in items:
            f.write(item + "\n")

def add_to_grocery_file(item, filename="groceries.txt"):
    """Append a single new item without erasing what's already saved."""
    with open(filename, "a") as f:
        f.write(item + "\n")

groceries = ["milk", "eggs", "bread"]
save_grocery_list(groceries)
add_to_grocery_file("apples")

with open("groceries.txt", "r") as f:
    print("\n=== groceries.txt ===")
    print(f.read())

# CHALLENGE: Call add_to_grocery_file() two more times with different
# items, then read and print the file to confirm all of them stuck
# around (that "w" didn't wipe out your earlier additions).

# ===========================================================
# PROGRAM 4 – Saving structured data with JSON
# ===========================================================
# Plain text works for a list of strings, but class_records from
# Week 3 is a LIST OF DICTIONARIES. Writing that out line-by-line
# and parsing it back yourself would be painful and error-prone.
#
# JSON (JavaScript Object Notation) is a text format that maps almost
# perfectly onto Python lists and dictionaries. Python's built-in
# `json` module converts between them automatically:
#
#   json.dump(data, file)   — Python object  -> JSON text in a file
#   json.load(file)         — JSON text in a file -> Python object
#
# This means class_records, exactly as it looked in memory, can be
# saved and loaded with almost no extra code.

import json

class_records = [
    {"name": "Amelia", "grade": 88},
    {"name": "Noah",   "grade": 73},
    {"name": "Priya",  "grade": 95},
]

def save_records(records, filename="class_records.json"):
    with open(filename, "w") as f:
        json.dump(records, f, indent=2)   # indent=2 makes it human-readable

def load_records(filename="class_records.json"):
    with open(filename, "r") as f:
        return json.load(f)

save_records(class_records)
print("\nSaved class_records.json.")

loaded = load_records()
print("=== Loaded back from disk ===")
for record in loaded:
    print(f"{record['name']}: {record['grade']}")

# Prove it survives: this is a NEW list, not the same object in memory —
# it was rebuilt entirely from the text in class_records.json.
print("\nSame data?", loaded == class_records)
print("Same object in memory?", loaded is class_records)

# CHALLENGE: Add a 4th record to `loaded` (append a new dictionary),
# save it back with save_records(), then load it again in a fresh
# call to prove the 4th record is now permanently there too.

# ===========================================================
# PROGRAM 5 – Reading and writing CSV files
# ===========================================================
# CSV ("comma-separated values") is the format spreadsheets export to.
# Every row is one record, and commas separate the columns. It's a
# plain list-of-lists shape rather than JSON's list-of-dictionaries,
# so it's a better fit when your data already looks like rows and
# columns — attendance sheets, grade exports, anything from Excel
# or Google Sheets.
#
# Python's built-in `csv` module handles the commas and quoting for
# you — don't try to split lines on "," yourself, it breaks the
# moment a value contains a comma.

import csv

attendance = [
    ["name", "monday", "tuesday", "wednesday"],
    ["Amelia", "present", "present", "absent"],
    ["Noah", "absent", "present", "present"],
    ["Priya", "present", "present", "present"],
]

def save_csv(rows, filename="attendance.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def load_csv(filename="attendance.csv"):
    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        return list(reader)

save_csv(attendance)
print("\nSaved attendance.csv.")

rows = load_csv()
print("=== Loaded from attendance.csv ===")
header, *data_rows = rows        # first row is the header, rest are data
for row in data_rows:
    print(row)

# csv.DictReader is even more useful — it uses the header row as keys,
# so each row comes back as a dictionary instead of a plain list.

def load_csv_as_dicts(filename="attendance.csv"):
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

records = load_csv_as_dicts()
print("\n=== Same file, as dictionaries ===")
for record in records:
    print(f"{record['name']} was absent on:",
          [day for day in ["monday", "tuesday", "wednesday"] if record[day] == "absent"])

# CHALLENGE: Add a "thursday" column to the attendance data (update the
# header row and every data row), save it, then load it with
# load_csv_as_dicts() and print who was absent on Thursday.
#
# Save this thought: class_records as JSON, and attendance as CSV,
# are exactly the kind of saved data your Week 5 mini project — a
# Personal Data App — will read from and write to every time it runs.
