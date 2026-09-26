# WEEK 3 · ACTIVITY 5 · EXTRA
#
# Do this only after activities 1 to 4 print PASSED.
#
# You will learn:
#   How to open a file inside try, and return None when it is missing.
#
# What to do:
#   1. Run 05_lesson.py first if you have not already.
#   2. Replace pass with the two lines that open the file and return its text.
#   3. Run this file.
#   4. You are done when the last line says: Activity 5: PASSED
#
# Only edit the TODO. Leave the CHECK section alone.

import os

def read_saved_score(filename):
    try:
        # TODO:
        # with open(filename, "r") as file:
        #     return file.read()
        pass
    except FileNotFoundError:
        return None


# CHECK — do not edit below this line
with open("saved_score.txt", "w") as file:
    file.write("40")

missing = read_saved_score("missing_score.txt")
found = read_saved_score("saved_score.txt")

os.remove("saved_score.txt")

print("missing →", missing)
print("saved →", found)
print("---")
if missing is None and found == "40":
    print("Activity 5: PASSED")
else:
    print("Activity 5: not yet.")
    print("A missing file should return None. Yours is", missing)
    print('The saved file should return "40". Yours is', found)
