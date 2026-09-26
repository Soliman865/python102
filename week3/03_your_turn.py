# WEEK 3 · ACTIVITY 3 OF 4 · YOUR TURN
#
# You will learn:
#   How to raise ValueError when a score is not positive.
#
# What to do:
#   1. Run 03_lesson.py first if you have not already.
#   2. Find the if value <= 0 block. Replace pass with raise.
#   3. Run this file.
#   4. You are done when the last line says: Activity 3: PASSED
#
# Only edit the TODO line. Leave the CHECK section alone.

class ScoreBook:
    def __init__(self):
        self.scores = []

    def add_score(self, value):
        if value <= 0:
            # TODO: raise ValueError("Score must be a positive number.")
            pass
        self.scores.append(value)


book = ScoreBook()
book.add_score(10)

raised = False
try:
    book.add_score(-3)
except ValueError:
    raised = True

# CHECK — do not edit below this line
print("Scores:", book.scores)
print("---")
if raised and book.scores == [10]:
    print("Activity 3: PASSED")
elif not raised:
    print("Activity 3: not yet.")
    print("-3 should raise ValueError, and it should not be stored.")
    print("Scores are", book.scores)
else:
    print("Activity 3: not yet.")
    print("10 should stay in the list. Scores are", book.scores)
