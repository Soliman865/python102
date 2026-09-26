# WEEK 4 · ACTIVITY 5 · EXTRA
#
# Do this only after activities 1 to 4 print PASSED.
#
# You will learn:
#   How to load JSON only when the file exists.
#
# What to do:
#   1. Run 05_lesson.py first if you have not already.
#   2. Replace pass with open and return json.load.
#   3. Leave the exists check as it is.
#   4. Run this file.
#   5. You are done when the last line says: Activity 5: PASSED
#
# Only edit the TODO. Leave the CHECK section alone.

import json
import os

def load_score(path):
    if not os.path.exists(path):
        return None
    # TODO:
    # with open(path, "r") as file:
    #     return json.load(file)
    pass


path = "week4_player_check.json"
with open(path, "w") as file:
    json.dump({"score": 40}, file)

missing = load_score("not_a_real_file.json")
found = load_score(path)
os.remove(path)

# CHECK — do not edit below this line
print("Missing:", missing)
print("Found:", found)
print("---")
if missing is None and found == {"score": 40}:
    print("Activity 5: PASSED")
else:
    print("Activity 5: not yet.")
    print("A missing file should return None. Yours is", missing)
    print('The saved file should return {"score": 40}. Yours is', found)
