# Week 4 — Exercises: Modules & the Standard Library
# Try these on your own. Don't look at lesson.py until you've given each one a real go.

import math
import random
import datetime
import os
import json

# ============================================================
# EXERCISE 1: math challenges (5 min)
# ============================================================
# Using the math module, calculate and print:
#   a) The square root of 256
#   b) 3 to the power of 8 (hint: math.pow)
#   c) The circumference of a circle with radius 7
#      Formula: circumference = 2 × π × r
#   d) Round 9.4 down and round 9.4 up

# YOUR CODE HERE:


# ============================================================
# EXERCISE 2: Random name picker (10 min)
# ============================================================
# Write a function called pick_teams(names, team_size) that:
#   1. Takes a list of names and a team size
#   2. Shuffles the names randomly
#   3. Splits them into teams of team_size
#      (the last team may be smaller if names don't divide evenly)
#   4. Prints each team, like:
#        Team 1: Alex, Jordan
#        Team 2: Riley, Sam
#        Team 3: Casey
#
# Test it with at least 7 names and team_size=2.
# Run it twice — the teams should be different each time!

# YOUR CODE HERE:


# ============================================================
# EXERCISE 3: Timestamp logger (10 min)
# ============================================================
# Write a function called log_event(message) that:
#   1. Gets the current date and time
#   2. Appends a line to "events.log" in this format:
#        [2026-09-18 12:00] message here
#   3. Prints "Logged: {message}"
#
# Call it 3 times with different messages, then open "events.log" and confirm all 3 are there.
# Hint: use "a" mode (append) so each call adds a new line without erasing old ones.

# YOUR CODE HERE:


# ============================================================
# EXERCISE 4: Save and load a high score (15 min)
# ============================================================
# Write two functions:
#
#   save_score(name, score)
#     - Saves {"name": name, "score": score, "date": today's date} to "highscore.json"
#     - If the file already exists and the new score is LOWER than the saved one,
#       print "Not a new high score!" and don't overwrite.
#     - Otherwise save it and print "New high score saved!"
#
#   load_score()
#     - If "highscore.json" exists, load and print the name, score, and date.
#     - If it doesn't exist, print "No high score yet."
#
# Test the flow:
#   load_score()             → No high score yet.
#   save_score("Alex", 150)  → New high score saved!
#   save_score("Alex", 100)  → Not a new high score!
#   save_score("Alex", 200)  → New high score saved!
#   load_score()             → shows 200

# YOUR CODE HERE:


# ============================================================
# BONUS: Combine everything (if you finish early)
# ============================================================
# Write a "daily challenge" program that:
#   1. On startup, checks if "challenge.json" exists for today's date
#      (use datetime to get today as a string like "2026-09-18")
#   2. If not: randomly pick a challenge from a list of 5 challenges,
#      save it to "challenge.json" with today's date, and print it
#   3. If yes: load and print it (same challenge for the whole day)
#
# Example challenges: "Do 20 push-ups", "Read for 15 mins",
#   "Learn one new Python function", "Write a haiku", "Draw something"

# YOUR CODE HERE:
