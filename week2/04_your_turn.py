# WEEK 2 · ACTIVITY 4 OF 4 · YOUR TURN
#
# You will learn:
#   How to add 1 to a counter that every object shares.
#
# What to do:
#   1. Run 04_lesson.py first if you have not already.
#   2. Find __init__. Under the TODO, add 1 to Hero.heroes_made.
#   3. Use the class name Hero, not self.
#   4. Run this file.
#   5. You are done when the last line says: Activity 4: PASSED
#
# heroes_made = 0 is already written. Do not move that line inside __init__.
# Only add the new line. Leave the CHECK section alone.

class Hero:
    heroes_made = 0

    def __init__(self, name):
        self.name = name
        # TODO: add 1 to Hero.heroes_made
        Hero.heroes_made = Hero.heroes_made + 1


mira = Hero("Mira")
zed = Hero("Zed")

# CHECK — do not edit below this line
print("---")
if Hero.heroes_made == 2:
    print("Activity 4: PASSED")
    print("You finished today's 4 activities.")
else:
    print("Activity 4: not yet.")
    print("Hero.heroes_made should be 2. It is", Hero.heroes_made)
    print("Inside __init__, add 1 to Hero.heroes_made. Use Hero, not self.")
