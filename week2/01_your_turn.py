# WEEK 2 · ACTIVITY 1 OF 4 · YOUR TURN
#
# You will learn:
#   How to write a method that changes an object's data.
#
# What to do:
#   1. Run 01_lesson.py first if you have not already.
#   2. Find heal. Replace pass with your own lines.
#   3. Copy the shape of take_damage, but add the amount instead of subtracting it.
#   4. Run this file.
#   5. You are done when the last line says: Activity 1: PASSED
#
# Only edit heal. Leave the CHECK section alone.

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, amount):
        self.health = self.health - amount
        print(f"{self.name} took {amount} damage. Health is now {self.health}.")

    def heal(self, amount):
        self.health = self.health + amount
        print(f"{self.name} healed {amount} . Health is now {self.health}.")

        # TODO: print the hero's name, the amount, and the new health
        # Example of what to print: Mira healed 20. Health is now 90.
        pass


mira = Hero("Mira")
mira.take_damage(30)  # health is now 70
mira.heal(20)

# CHECK — do not edit below this line
print("---")
if mira.health == 90:
    print("Activity 1: PASSED")
else:
    print("Activity 1: not yet.")
    print("After healing 20, health should be 90.")
    print("Health is", mira.health)
    print("Inside heal, add amount to self.health. Use take_damage as the pattern.")
