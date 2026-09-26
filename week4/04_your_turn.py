# WEEK 4 · ACTIVITY 4 OF 4 · YOUR TURN
#
# You will learn:
#   How to save a dict with json.dump and load it with json.load.
#
# What to do:
#   1. Run 04_lesson.py first if you have not already.
#   2. Fill in save_player. Delete pass.
#   3. Fill in load_player. Delete pass. Remember to return the loaded dict.
#   4. Run this file.
#   5. You are done when the last line says: Activity 4: PASSED
#
# Only edit the two TODO spots. Leave the CHECK section alone.

import json
import os

def save_player(path, player):
    # TODO:
    # with open(path, "w") as file:
    #     json.dump(player, file)
    pass

def load_player(path):
    # TODO:
    # with open(path, "r") as file:
    #     return json.load(file)
    pass


path = "week4_player_check.json"
loaded = None
error = None
try:
    save_player(path, {"name": "Mira", "score": 40})
    loaded = load_player(path)
except Exception as problem:
    error = problem

if os.path.exists(path):
    os.remove(path)

# CHECK — do not edit below this line
print("Loaded:", loaded)
print("---")
if loaded == {"name": "Mira", "score": 40}:
    print("Activity 4: PASSED")
    print("You finished today's 4 activities.")
elif error is not None:
    print("Activity 4: not yet.")
    print("Saving or loading hit an error:", error)
    print("Use json.dump in save_player and return json.load in load_player.")
else:
    print("Activity 4: not yet.")
    print('Loaded data should be {"name": "Mira", "score": 40}.')
    print("Yours is:", loaded)
