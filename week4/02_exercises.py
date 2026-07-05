# 02 – Week 4 Exercises
# Math+Coding Academy | Python102
#
# These are your independent exercises for Week 4.
# Use everything from 01_file_io.py — open()/with, read()/write(),
# append mode, json.dump()/json.load(), and the csv module.
#
# Structure every exercise with functions. Run your file often and
# check the actual .txt/.json/.csv files it creates in VS Code's file
# explorer — don't just trust the printed output.
#
# When you're done, add, commit, and push — same as every week.

# ===========================================================
# EXERCISE 1 – Grocery list, but it remembers
# ===========================================================
# Bring back the grocery list manager from Week 3 Exercise 1 — but
# this time it saves to grocery_list.txt so the list survives between
# runs of your program.
#
# Requirements:
# - On startup, load grocery_list.txt into a list if it exists
#   (if the file doesn't exist yet, start with an empty list —
#   don't let a missing file crash your program)
# - Ask the user to type items one at a time, type "done" to stop
# - After each item is added, save the FULL list back to the file
#   (overwrite it — don't just append, or removed items will come back)
# - Let the user remove an item by name before quitting, and save again
# - Print the final list, and how many items are in it
#
# Structure your solution with at least these functions:
#   load_list(filename)              → returns a list (empty if file missing)
#   save_list(items, filename)       → overwrites the file with the current list
#   build_list(items)                → returns the list after adding items
#   remove_items(items)              → removes items the user names
#
# Test it: add a few items, quit the program, run it again, and
# confirm your items are still there.

# YOUR CODE HERE


# ===========================================================
# EXERCISE 2 – Contact book, saved as JSON
# ===========================================================
# Bring back the contact book from Week 3 Exercise 2 — but now it's
# permanently saved to contacts.json instead of disappearing when
# the program ends.
#
# Requirements:
# - On startup, load contacts.json into a dictionary if it exists,
#   otherwise start with a dictionary containing 3 pre-filled contacts
#   (name -> {"phone": ..., "city": ...})
# - Ask the user to type a name to look up. If found, print their
#   phone and city. If not found, print a friendly message — use
#   .get() so it never crashes with a KeyError
# - Let the user add a new contact (name, phone, city)
# - Save the FULL contact dictionary back to contacts.json before quitting
# - Print the full, updated contact book at the end
#
# Structure your solution with functions:
#   load_contacts(filename)              → returns a dictionary
#   save_contacts(contacts, filename)    → writes it with json.dump
#   look_up(contacts, name)              → prints phone/city or a friendly miss
#   add_contact(contacts, name, phone, city)

# YOUR CODE HERE


# ===========================================================
# EXERCISE 3 – Grade book, saved as JSON
# ===========================================================
# Bring back the grade book from Week 3 Exercise 3 — a LIST of
# DICTIONARIES, one per student — and make it permanent using JSON,
# the same way PROGRAM 4 saved class_records.
#
# Requirements:
# - On startup, load grades.json into a list if it exists, otherwise
#   start with an empty list
# - Let the user add new students (name + grade) to the list
# - After every student is added, print the current class average
#   (write this from scratch — don't just reuse Week 3's function
#   without understanding it)
# - Save the FULL list back to grades.json before quitting
# - Print every student and their grade, and the name of the student
#   with the highest grade
#
# Structure your solution with functions:
#   load_records(filename)     → returns a list of dictionaries
#   save_records(records, filename)
#   add_student(records, name, grade)
#   class_average(records)
#   top_student(records)       → returns the name with the highest grade
#
# Test it: add students, quit, run again, and confirm the class
# average includes students from your PREVIOUS run too.

# YOUR CODE HERE


# ===========================================================
# EXERCISE 4 (Bonus) – Attendance report from a CSV file
# ===========================================================
# Using the attendance.csv idea from PROGRAM 5, write a program that
# reads an attendance file and produces a summary report.
#
# Requirements:
# - Write your own attendance.csv with a header row (name + at least
#   4 day columns) and at least 5 students, using save_csv() /
#   csv.writer — either reuse PROGRAM 5's code or write your own
# - Read it back with csv.DictReader
# - For each student, print how many days they were "present" and
#   how many they were "absent"
# - Print the name of the student with the BEST attendance (most
#   "present" days) and the name of the student with the WORST
# - Print the class-wide attendance rate as a percentage:
#     (total "present" cells) / (total cells that aren't the name column)
#
# Hint: you already wrote the "which days was X absent" logic in
# PROGRAM 5 — this asks you to count instead of list, and add up
# totals across every student instead of just one.

# YOUR CODE HERE
