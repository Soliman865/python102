# Week 11 - Exercises
# Math+Coding Academy | Python102
#
# Same game as class. Find it, fix it, then write a test that proves it.

import unittest

# ===========================================================
# EXERCISE 1
# ===========================================================
def count_completed(habits):
    count = 0
    for habit in habits:
        if habit["times_done"] > 0:
            count = 1
    return count

print(count_completed([{"times_done": 3}, {"times_done": 5}, {"times_done": 0}]))
# should print 2

# FIX IT HERE:


# ===========================================================
# EXERCISE 2
# ===========================================================
def is_habit_done_today(status):
    return status == "Done"

print(is_habit_done_today("done"))   # user typed lowercase - should still count!

# FIX IT HERE:


# ===========================================================
# EXERCISE 3
# ===========================================================
def total_times_done(habits):
    total = 0
    for habit in habits:
        total = total + habit["times_done"]
    return total / len(habits)

print(total_times_done([]))
# What happens when the habit list is empty? Should this crash the whole
# program, or should it print something sensible like 0?

# FIX IT HERE:


# ===========================================================
# EXERCISE 4
# ===========================================================
def get_habit_names(habits):
    names = []
    for habit in habits:
        names.append(habit["Name"])
    return names

print(get_habit_names([{"name": "Read"}, {"name": "Exercise"}]))

# FIX IT HERE:


# ===========================================================
# EXERCISE 5 - write the tests
# ===========================================================
# Pick any TWO of your fixed functions above (1-4) and write 2 tests each
# (8 tests total). Include at least one edge case per function - an empty
# list, a zero, weird capitalization.

# YOUR CODE HERE


# ===========================================================
# EXERCISE 6 (if you finish early) - bring your own bug
# ===========================================================
# Grab ONE function from a project you built with AI help this term
# (habit tracker, mini project 2, whatever). Paste it below.
#
#  1. Try 3 inputs by hand, including a weird one (empty, zero, negative)
#  2. Write 2 tests for it
#  3. If you find a bug - fix it. If not - your tests are the proof.

# YOUR CODE HERE


if __name__ == "__main__":
    unittest.main()
