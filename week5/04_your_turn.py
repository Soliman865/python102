# WEEK 5 · ACTIVITY 4 OF 5 · YOUR TURN
#
# You will learn:
#   How to write the player list to a JSON file.
#
# What to do:
#   1. Run 04_lesson.py first if you have not already.
#   2. Fill in save_all. Delete pass.
#   3. json.dump the list named data. Look at 04_lesson.py for the two lines.
#   4. Run this file.
#   5. You are done when the last line says: Activity 4: PASSED
#
# load_all is already written. Only edit save_all.
# Leave the CHECK section alone.

import json
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []

def save_all(path, players):
    data = []
    for player in players.values():
        data.append({"name": player.name, "scores": player.scores})
    # TODO:
    # with open(path, "w") as file:
    #     json.dump(data, file, indent=2)
    pass

def load_all(path):
    with open(path, "r") as file:
        data = json.load(file)
    players = {}
    for entry in data:
        player = Player(entry["name"])
        player.scores = entry["scores"]
        players[player.name] = player
    return players


path = "scores_check.json"
mira = Player("Mira")
mira.scores.append({"value": 40, "date": "2026-09-26 15:00"})
loaded = None
error = None
try:
    save_all(path, {"Mira": mira})
    loaded = load_all(path)
except Exception as problem:
    error = problem

if os.path.exists(path):
    os.remove(path)

# CHECK — do not edit below this line
print("---")
if (
    error is None
    and loaded is not None
    and "Mira" in loaded
    and loaded["Mira"].scores[0]["value"] == 40
):
    print("Activity 4: PASSED")
elif error is not None:
    print("Activity 4: not yet.")
    print("Saving or loading hit an error:", error)
    print("Inside save_all, json.dump the list named data.")
else:
    print("Activity 4: not yet.")
    print("After loading, Mira's score should be 40.")
