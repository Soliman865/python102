# SOLUTION FILE — answer key for week5/01_your_turn.py
# This fills in the TODOs so the file prints PASSED.
# Do not give this file to students before they finish on their own.

# WEEK 5 · ACTIVITY 1 OF 5 · YOUR TURN
#
# You will learn:
#   How to return 0 when there are no scores, and max when there are some.
#
# What to do:
#   1. Run 01_lesson.py first if you have not already.
#   2. Fill in best_score. Delete pass.
#   3. Run this file.
#   4. You are done when the last line says: Activity 1: PASSED
#
# Only edit best_score. Leave the CHECK section alone.

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, value):
        self.scores.append(value)

    def best_score(self):
        if len(self.scores) == 0:
            return 0
        return max(self.scores)


empty = Player("Nova")
mira = Player("Mira")
mira.add_score(10)
mira.add_score(40)

# CHECK — do not edit below this line
try:
    empty_best = empty.best_score()
    mira_best = mira.best_score()
except Exception as problem:
    print("Activity 1: not yet.")
    print("best_score hit an error:", problem)
    print("Return 0 when the list is empty, before you call max.")
else:
    print("Nova's best:", empty_best)
    print("Mira's best:", mira_best)
    print("---")
    if empty_best == 0 and mira_best == 40:
        print("Activity 1: PASSED")
    else:
        print("Activity 1: not yet.")
        print("An empty player should have best score 0. Yours is", empty_best)
        print("Mira's best should be 40. Yours is", mira_best)
