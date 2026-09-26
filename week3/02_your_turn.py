# WEEK 3 · ACTIVITY 2 OF 4 · YOUR TURN
#
# You will learn:
#   How to catch IndexError, the "spot is not in the list" error.
#
# What to do:
#   1. Run 02_lesson.py first if you have not already.
#   2. Find get_item. Replace pass with return items[index].
#   3. Leave the except block as it is.
#   4. Run this file.
#   5. You are done when the last line says: Activity 2: PASSED
#
# Only edit the TODO line. Leave the CHECK section alone.

def get_item(items, index):
    try:
        # TODO: return the item at this index
        pass
    except IndexError:
        return None


shopping = ["milk", "eggs", "bread"]

# CHECK — do not edit below this line
try:
    eggs = get_item(shopping, 1)
    missing = get_item(shopping, 10)
except IndexError:
    eggs = "crash"
    missing = "crash"

print("index 1 →", eggs)
print("index 10 →", missing)
print("---")
if eggs == "eggs" and missing is None:
    print("Activity 2: PASSED")
elif eggs == "crash":
    print("Activity 2: not yet.")
    print("Index 10 should not crash. except IndexError should return None.")
else:
    print("Activity 2: not yet.")
    print("Index 1 should be eggs. Yours is", eggs)
    print("Index 10 should be None. Yours is", missing)
    print("Inside try, return items[index].")
