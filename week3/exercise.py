# Week 3 — Exercises: Error Handling
# Try these on your own. Don't look at lesson.py until you've given each one a real go.

# ============================================================
# EXERCISE 1: Fix the crash (5 min)
# ============================================================
# This program crashes. Run it, read the error, then add try/except to fix it.

def get_item(items, index):
    return items[index]

shopping = ["milk", "eggs", "bread"]
print(get_item(shopping, 10))   # This will crash — fix it!

# After fixing: it should print a helpful message instead of crashing.


# ============================================================
# EXERCISE 2: Safe number input (10 min)
# ============================================================
# Write a function called ask_positive_number(prompt) that:
#   1. Asks the user for a number using input()
#   2. Converts it to an int
#   3. If the user types something that isn't a number → print "Please enter a valid number." and ask again
#   4. If the user enters 0 or a negative number → print "Please enter a positive number." and ask again
#   5. Once a valid positive number is given → return it
#
# Hint: you'll need a while True loop + try/except ValueError

# YOUR CODE HERE:


# ============================================================
# EXERCISE 3: Add error handling to your Superhero class (15 min)
# ============================================================
# Copy your Superhero class from week2/exercise.py.
# Add these rules with raise ValueError:
#
#   In __init__:
#     - if health is not between 1 and 100, raise ValueError
#     - if energy is not between 0 and 50, raise ValueError
#
#   In take_damage (add this method if you don't have it):
#     - if amount is negative, raise ValueError("Damage cannot be negative")
#
# Then test it:
#   - Create a hero normally (should work)
#   - Try creating a hero with health=200 (should raise ValueError)
#   - Try calling take_damage(-5) (should raise ValueError)
#   - Wrap the bad calls in try/except and print the error message

# YOUR CODE HERE:


# ============================================================
# EXERCISE 5: else and finally (10 min)
# ============================================================
# Write a function called load_score(filename) that:
#   - tries to open the file and read an integer from it
#   - if FileNotFoundError: print "No save file found." and return 0
#   - if ValueError (file exists but doesn't contain a number): print "Save file is corrupted." and return 0
#   - else (success): print "Score loaded: {score}" and return the score
#   - finally: print "Done checking save file."
#
# Test it three ways:
#   1. A file that doesn't exist
#   2. A file that contains "hello" (not a number) — create it manually first
#   3. A file that contains "250" — create it and try loading

# YOUR CODE HERE:


# ============================================================
# EXERCISE 6: Custom exception class (10 min)
# ============================================================
# Create a custom exception called InvalidMoveError.
# Then build a TicTacToe board class (just the validation, no full game needed):
#
#   Board:
#     __init__()       → creates a 3×3 grid (a list of 9 values, all " ")
#     place(pos, mark) → places "X" or "O" at position pos (0–8)
#                        raise InvalidMoveError if pos is out of range (not 0–8)
#                        raise InvalidMoveError if that spot is already taken
#     show()           → prints the board in a 3×3 layout
#
# Test:
#   - Place X at position 4 (should work)
#   - Place O at position 4 again (should raise InvalidMoveError — already taken)
#   - Place X at position 9 (should raise InvalidMoveError — out of range)
#   - Wrap bad moves in try/except and print the error nicely

# YOUR CODE HERE:


# ============================================================
# EXERCISE 7: Robust menu program (15 min)
# ============================================================
# Build a small "number guessing" CLI game with full error handling.
#
# Rules:
#   - The program picks a secret number between 1 and 20 (use random.randint)
#   - The player gets 5 guesses
#   - After each guess, print "Too high!", "Too low!", or "Correct!"
#   - If the player types something that isn't a number, print "That's not a number!" and don't use up a guess
#   - If the player runs out of guesses, reveal the number
#
# Requirements:
#   - Use try/except for invalid input
#   - Use a while loop for the game loop
#   - Track remaining guesses

import random

# YOUR CODE HERE:


# ============================================================
# BONUS: Chained exceptions (if you finish early)
# ============================================================
# Python lets you raise one exception while handling another, using raise...from:
#
#   try:
#       value = int("bad")
#   except ValueError as original:
#       raise RuntimeError("Could not parse config") from original
#
# Build a function called parse_config(text) that:
#   - Tries to split text on "=" to get a key and value (e.g. "score=100")
#   - Tries to convert the value to an int
#   - If either step fails, raises a ValueError("Invalid config line: {text}") from the original error
#
# Test with:
#   parse_config("score=100")     # works
#   parse_config("score=abc")     # ValueError
#   parse_config("no equals sign")  # ValueError

# YOUR CODE HERE:
