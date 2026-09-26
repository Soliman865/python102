# Week 1 — Exercises
# Do these on your own! Read the instructions in each section.
# Don't look at lesson.py until you've tried each one.

# ============================================================
# EXERCISE 1: Python Recap — fix the function (5 min)
# ============================================================
# This function is supposed to return the sum of two numbers.
# It has a bug. Find it and fix it.

def add_numbers(a, b):
    result = a + b  # BUG: wrong operator
    return result

# Test it — should print 10
print(add_numbers(3, 7))


# ============================================================
# EXERCISE 2: Build a Cat class (15 min)
# ============================================================
# Build a Cat class with:
#   Attributes: name, colour, age
#   Methods:
#     meow()    → prints "{name} says: Meow!"
#     describe() → prints "I am {name}. I am a {colour} cat, {age} years old."
#     is_kitten() → returns True if age <= 1, False otherwise
#
# Then create 2 Cat objects and call all 3 methods on each.

# YOUR CODE HERE:


# ============================================================
# EXERCISE 3: Extend your Cat class (10 min)
# ============================================================
# Add a method called birthday() that increases the cat's age by 1
# and prints "{name} just turned {new_age}!"
#
# Test: create a cat that is 1 year old, call birthday(),
# then call is_kitten() — it should now return False.

# YOUR CODE HERE:


# ============================================================
# BONUS: A different class (if you finish early)
# ============================================================
# Design your own class for something you care about.
# It must have:
#   - at least 3 attributes
#   - at least 2 methods
#   - at least 1 method that returns a boolean (True/False)
#
# Ideas: Song, Player, Planet, Book, Car, BubbleTea ...

# YOUR CODE HERE:
