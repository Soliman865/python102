# SOLUTION FILE — answer key for week5/05_your_turn.py
# This fills in the TODOs so the file prints PASSED.
# Do not give this file to students before they finish on their own.

# WEEK 5 · ACTIVITY 5 OF 5 · YOUR TURN
#
# You will learn:
#   How to remember the player with the highest score while you loop.
#
# What to do:
#   1. Run 05_lesson.py first if you have not already.
#   2. Inside the for loop, replace pass with the if from the lesson.
#   3. Run this file.
#   4. You are done when the last line says: Activity 5: PASSED
#   5. Then open 05_app.py and follow the steps at the top.
#
# Only edit the loop. Leave the CHECK section alone.

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

def top_scorer(players):
    best_player = None
    best_value = -1
    for player in players.values():
        if player.best_score() > best_value:
            best_value = player.best_score()
            best_player = player
    return best_player


players = {
    "Mira": Player("Mira"),
    "Zed": Player("Zed"),
}
players["Mira"].add_score(10)
players["Zed"].add_score(50)
winner = top_scorer(players)

# CHECK — do not edit below this line
print("---")
if winner is not None and winner.name == "Zed" and winner.best_score() == 50:
    print("Activity 5: PASSED")
    print("Next file: 05_app.py")
else:
    print("Activity 5: not yet.")
    print("Zed should win with 50.")
    if winner is None:
        print("top_scorer returned None. Update best_player inside the loop.")
    else:
        print("You returned", winner.name, "with", winner.best_score())
