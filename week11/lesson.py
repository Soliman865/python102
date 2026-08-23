# Week 11 - Debugging AI Code
# Math+Coding Academy | Python102
#
# AI code runs fine and still lies to you sometimes. Let's catch it in the act.

# ===========================================================
# ROUND 1 - Find the bug (just by reading, don't run it yet)
# ===========================================================

def average_grade(scores):
    total = 0
    for i in range(len(scores) - 1):
        total += scores[i]
    return total / len(scores)

print(average_grade([80, 90, 100]))   # should print 90

# FIX IT HERE:


# ===========================================================
# ROUND 2
# ===========================================================

def is_even(n):
    return n % 2 == 1

print(is_even(4))   # should print True

# FIX IT HERE:


# ===========================================================
# ROUND 3 - Run it TWICE and compare
# ===========================================================

def add_habit(name, habits=[]):
    habits.append(name)
    return habits

print(add_habit("Read"))
print(add_habit("Exercise"))
# Did the 2nd print start empty, or does it remember "Read"?
# Famous Python gotcha - look up "mutable default argument"

# FIX IT HERE:


# ===========================================================
# ROUND 4 - Can't spot this one by eye, you have to check a number
# ===========================================================

def get_highest(scores):
    highest = 0
    for score in scores:
        if score > highest:
            highest = score
    return highest

print(get_highest([-30, -10, -25]))   # should print -10

# FIX IT HERE:


# ===========================================================
# ROUND 5 - It never crashes. That's the bug.
# ===========================================================

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

def average_per_day(times_done, days):
    result = safe_divide(times_done, days)
    print(f"Average per day: {result}")

average_per_day(10, 0)
# Nothing crashed. But is "Average per day: None" actually telling the
# user anything useful? What SHOULD happen instead?

# FIX IT HERE:


# ===========================================================
# ROUND 6 - The menu number trap
# ===========================================================

def remove_habit(habits, number):
    """number is what the user typed - the menu shows 1. Read  2. Exercise"""
    del habits[number]
    return habits

habits = ["Read", "Exercise", "Sleep early"]
print(remove_habit(habits, 1))   # user typed "1" meaning "Read"
# Did "Read" actually get removed?

# FIX IT HERE:


# ===========================================================
# NOW: instead of eyeballing every fix, let's make Python check for us
# ===========================================================

import unittest

class TestAverageGrade(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(average_grade([80, 90, 100]), 90)

    def test_one_score(self):
        self.assertEqual(average_grade([75]), 75)   # breaks the OLD buggy version!


if __name__ == "__main__":
    unittest.main()

# Run it: python -m unittest lesson.py
# Try it against your BROKEN average_grade first - watch it fail.
# Put your fix back - watch it pass.

# ===========================================================
# YOUR TURN
# ===========================================================
# Write 2 tests for get_highest() - one normal case, one that would've
# caught the Round 4 bug.

# YOUR CODE HERE


# Write 2 tests for remove_habit() - one normal case, one that would've
# caught the Round 6 bug.

# YOUR CODE HERE
