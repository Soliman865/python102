# WEEK 2 · ACTIVITY 3 OF 4 · YOUR TURN
#
# You will learn:
#   How to choose the sentence that print(hero) shows.
#
# What to do:
#   1. Run 03_lesson.py first if you have not already.
#   2. Find __str__. Replace the return line.
#   3. Return a string in this exact shape: Nova | health: 100
#   4. Use self.name and self.health, the same way the lesson does.
#   5. Run this file.
#   6. You are done when the last line says: Activity 3: PASSED
#
# Only edit the return line. Leave the CHECK section alone.
# Spaces matter. Copy the shape from 03_lesson.py.

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def __str__(self):
        return f"{self.name} | health: {self.health}"


nova = Hero("Nova")
print(nova)

# CHECK — do not edit below this line
print("---")
if str(nova) == "Nova | health: 100":
    print("Activity 3: PASSED")
else:
    print("Activity 3: not yet.")
    print("print(nova) should show: Nova | health: 100")
    print("It shows:", nova)

