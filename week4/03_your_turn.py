# WEEK 4 · ACTIVITY 3 OF 4 · YOUR TURN
#
# You will learn:
#   How to format a date as YYYY-MM-DD.
#
# What to do:
#   1. Run 03_lesson.py first if you have not already.
#   2. Replace the return line. Use strftime.
#   3. The text must be exactly 2014-03-15.
#   4. Run this file.
#   5. You are done when the last line says: Activity 3: PASSED
#
# Only edit the return line. Leave the CHECK section alone.

import datetime

def format_birthday():
    birthday = datetime.date(2014, 3, 15)
    # TODO: return birthday.strftime("%Y-%m-%d")
    return ""


text = format_birthday()
print("Birthday:", text)

# CHECK — do not edit below this line
print("---")
if text == "2014-03-15":
    print("Activity 3: PASSED")
else:
    print("Activity 3: not yet.")
    print("It should be exactly: 2014-03-15")
    print("Yours is:", text)
