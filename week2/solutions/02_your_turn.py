# SOLUTION FILE — answer key for week2/02_your_turn.py
# This fills in the TODOs so the file prints PASSED.
# Do not give this file to students before they finish on their own.

# WEEK 2 · ACTIVITY 2 OF 4 · YOUR TURN
#
# You will learn:
#   How to make one hero change another hero.
#
# What to do:
#   1. Run 02_lesson.py first if you have not already.
#   2. Find attack. Replace pass with your own lines.
#   3. Call other.take_damage and pass this hero's power.
#   4. Print a sentence that names both heroes.
#   5. Run this file.
#   6. You are done when the last line says: Activity 2: PASSED
#
# Only edit attack. Leave the CHECK section alone.

class Hero:
    def __init__(self, name, power):
        self.name = name
        self.health = 100
        self.power = power

    def take_damage(self, amount):
        self.health = self.health - amount

    def attack(self, other):
        other.take_damage(self.power)
        print(f"{self.name} hits {other.name} for {self.power} damage.")


mira = Hero("Mira", 25)
zed = Hero("Zed", 10)
mira.attack(zed)

# CHECK — do not edit below this line
print("---")
if zed.health == 75 and mira.health == 100:
    print("Activity 2: PASSED")
else:
    print("Activity 2: not yet.")
    print("Zed's health should be 75. It is", zed.health)
    print("Mira's health should still be 100. It is", mira.health)
    print("Inside attack, call other.take_damage(self.power).")
