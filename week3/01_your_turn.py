# WEEK 3 · ACTIVITY 1 OF 4 · YOUR TURN
#
# You will learn:
#   How to put the risky line inside try.
#
# What to do:
#   1. Run 01_lesson.py first if you have not already.
#   2. Find safe_int. Replace pass with return int(text).
#   3. Leave the except block as it is.
#   4. Run this file.
#   5. You are done when the last line says: Activity 1: PASSED
#
# Only edit the TODO line. Leave the CHECK section alone.

def safe_int(text):
    try:
        # TODO: return int(text)
        pass
    except ValueError:
        return None


# CHECK — do not edit below this line
try:
    number = safe_int("12")
    word = safe_int("hello")
except ValueError:
    number = "crash"
    word = "crash"

print("12 →", number)
print("hello →", word)
print("---")
if number == 12 and word is None:
    print("Activity 1: PASSED")
elif number == "crash":
    print("Activity 1: not yet.")
    print("hello should not crash. except ValueError should return None.")
else:
    print("Activity 1: not yet.")
    print("safe_int('12') should be 12. Yours is", number)
    print("safe_int('hello') should be None. Yours is", word)
    print("Inside try, return int(text).")
