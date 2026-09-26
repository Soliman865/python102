# SOLUTION FILE — answer key for week5/03_your_turn.py
# This fills in the TODOs so the file prints PASSED.
# Do not give this file to students before they finish on their own.

# WEEK 5 · ACTIVITY 3 OF 5 · YOUR TURN
#
# You will learn:
#   How to store a score dict that includes today's date.
#
# What to do:
#   1. Run 03_lesson.py first if you have not already.
#   2. Fill in add_score. Delete pass.
#   3. Use the three lines from the lesson.
#   4. Run this file.
#   5. You are done when the last line says: Activity 3: PASSED
#
# Only edit add_score. Leave the CHECK section alone.

import datetime

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, value):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        entry = {"value": value, "date": date}
        self.scores.append(entry)

    def best_score(self):
        if len(self.scores) == 0:
            return 0
        best = self.scores[0]["value"]
        for entry in self.scores:
            if entry["value"] > best:
                best = entry["value"]
        return best


mira = Player("Mira")
error = None
try:
    mira.add_score(50)
    entry = mira.scores[0]
    best = mira.best_score()
except Exception as problem:
    entry = None
    best = None
    error = problem

# CHECK — do not edit below this line
today = datetime.date.today().strftime("%Y-%m-%d")
print("Scores:", mira.scores)
print("---")
if (
    error is None
    and isinstance(entry, dict)
    and entry.get("value") == 50
    and str(entry.get("date", "")).startswith(today)
    and best == 50
):
    print("Activity 3: PASSED")
elif error is not None:
    print("Activity 3: not yet.")
    print("add_score hit an error:", error)
    print("Append a dict with keys value and date. Copy the three lines from 03_lesson.py.")
else:
    print("Activity 3: not yet.")
    print("The score should be a dict with value 50 and today's date.")
    print("Yours is:", entry)
