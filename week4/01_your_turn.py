# WEEK 4 · ACTIVITY 1 OF 4 · YOUR TURN
#
# You will learn:
#   How to call math.sqrt and use math.pi.
#
# What to do:
#   1. Run 01_lesson.py first if you have not already.
#   2. Fill in both TODOs. Delete each pass.
#   3. Run this file.
#   4. You are done when the last line says: Activity 1: PASSED
#
# Only edit the two TODO spots. Leave the CHECK section alone.

import math

def square_root(number):
    # TODO: return math.sqrt(number)
    pass

def circumference(radius):
    # TODO: return 2 * math.pi * radius
    pass


# CHECK — do not edit below this line
root = square_root(256)
circle = circumference(7)
print("Square root of 256:", root)
print("Circumference of radius 7:", circle)
print("---")
if root == 16.0 and circle is not None and abs(circle - (2 * math.pi * 7)) < 0.001:
    print("Activity 1: PASSED")
else:
    print("Activity 1: not yet.")
    print("square_root(256) should be 16.0. Yours is", root)
    print("circumference(radius) should return 2 * math.pi * radius.")
