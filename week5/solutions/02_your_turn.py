# SOLUTION FILE — answer key for week5/02_your_turn.py
# This fills in the TODOs so the file prints PASSED.
# Do not give this file to students before they finish on their own.

# WEEK 5 · ACTIVITY 2 OF 5 · YOUR TURN
#
# You will learn:
#   How to reject a score that is 0 or negative.
#
# What to do:
#   1. Run 02_lesson.py first if you have not already.
#   2. Inside the if, replace pass with raise ValueError.
#   3. Run this file.
#   4. You are done when the last line says: Activity 2: PASSED
#
# Only edit the TODO line. Leave the CHECK section alone.

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, value):
        if value <= 0:
            raise ValueError("Score must be a positive number.")
        self.scores.append(value)


mira = Player("Mira")
mira.add_score(20)
raised = False
try:
    mira.add_score(0)
except ValueError:
    raised = True

# CHECK — do not edit below this line
print("Scores:", mira.scores)
print("---")
if raised and mira.scores == [20]:
    print("Activity 2: PASSED")
else:
    print("Activity 2: not yet.")
    print("0 should raise ValueError and should not be stored.")
    print("Scores are", mira.scores)
