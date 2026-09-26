# SOLUTION FILE — answer key for week3/04_your_turn.py
# This fills in the TODOs so the file prints PASSED.
# Do not give this file to students before they finish on their own.

# WEEK 3 · ACTIVITY 4 OF 4 · YOUR TURN
#
# You will learn:
#   How to raise an error type you named yourself.
#
# What to do:
#   1. Run 04_lesson.py first if you have not already.
#   2. Inside the if, replace pass with raise InvalidScoreError.
#   3. Use InvalidScoreError, not ValueError.
#   4. Run this file.
#   5. You are done when the last line says: Activity 4: PASSED
#
# Only edit the TODO line. Leave the CHECK section alone.

class InvalidScoreError(Exception):
    pass


class ScoreBook:
    def __init__(self):
        self.scores = []

    def add_score(self, value):
        if value <= 0:
            raise InvalidScoreError("Score must be a positive number.")
        self.scores.append(value)


book = ScoreBook()
saw_custom_error = False
saw_value_error = False
try:
    book.add_score(0)
except InvalidScoreError:
    saw_custom_error = True
except ValueError:
    saw_value_error = True

good = ScoreBook()
good.add_score(8)

# CHECK — do not edit below this line
print("---")
if saw_custom_error and book.scores == [] and good.scores == [8]:
    print("Activity 4: PASSED")
    print("You finished today's 4 activities.")
elif saw_value_error:
    print("Activity 4: not yet.")
    print("Raise InvalidScoreError, not ValueError.")
else:
    print("Activity 4: not yet.")
    print("0 should raise InvalidScoreError and should not be stored.")
    print("Scores are", book.scores)
