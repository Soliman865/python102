# SOLUTION FILE — answer key for week4/02_your_turn.py
# This fills in the TODOs so the file prints PASSED.
# Do not give this file to students before they finish on their own.

# WEEK 4 · ACTIVITY 2 OF 4 · YOUR TURN
#
# You will learn:
#   How to return a random dice roll and a random list item.
#
# What to do:
#   1. Run 02_lesson.py first if you have not already.
#   2. Fill in both TODOs. Delete each pass.
#   3. Run this file.
#   4. You are done when the last line says: Activity 2: PASSED
#
# Only edit the two TODO spots. Leave the CHECK section alone.

import random

def roll_dice():
    return random.randint(1, 6)

def pick_snack(snacks):
    return random.choice(snacks)


snacks = ["apple", "cracker", "yogurt"]
rolls = []
picked = []
for i in range(12):
    rolls.append(roll_dice())
    picked.append(pick_snack(snacks))

print("Rolls:", rolls)
print("Snacks:", picked)

# CHECK — do not edit below this line
print("---")
rolls_ok = True
different_rolls = []
for roll in rolls:
    if roll not in [1, 2, 3, 4, 5, 6]:
        rolls_ok = False
    if roll not in different_rolls:
        different_rolls.append(roll)
if len(different_rolls) < 2:
    rolls_ok = False

snacks_ok = True
different_snacks = []
for item in picked:
    if item not in snacks:
        snacks_ok = False
    if item not in different_snacks:
        different_snacks.append(item)
if len(different_snacks) < 2:
    snacks_ok = False

if rolls_ok and snacks_ok:
    print("Activity 2: PASSED")
else:
    print("Activity 2: not yet.")
    if not rolls_ok:
        print("roll_dice should use random.randint(1, 6), not one fixed number.")
    if not snacks_ok:
        print("pick_snack should use random.choice(snacks).")
