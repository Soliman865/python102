"""
Week 5 - Exercise: Habit Tracker
Python102 | Math+Coding Academy

Try this on your own before checking solution.py.

Build a command-line Habit Tracker that saves data to a file, using the
same pattern we used in lesson.py (Contact Book):

  - Each habit is a dictionary: {"name": ..., "times_done": 0}
  - All habits are stored in a list
  - Data is saved to "habits.json" after every change
  - Data is loaded from "habits.json" when the program starts

Your menu should have these options:
  1. View habits       - print each habit's name and times_done
  2. Add habit         - ask for a habit name, start times_done at 0
  3. Mark habit done   - ask which habit (by number), add 1 to times_done
  4. Delete habit      - ask which habit (by number), remove it
  5. Quit

TODO 1: Write load_habits() - load the list from HABITS_FILE if it
        exists, otherwise return an empty list.

TODO 2: Write save_habits(habits) - write the list to HABITS_FILE
        using json.dump().

TODO 3: Write add_habit(habits) - ask for a name, create a new
        dictionary, append it to the list, and save.

TODO 4: Write view_habits(habits) - loop through the list and print
        each habit's name and times_done, numbered starting at 1.

TODO 5: Write mark_done(habits) - show the habits, ask which number,
        add 1 to that habit's times_done, and save. Handle bad input
        (non-numbers or out-of-range numbers) without crashing.

TODO 6: Write delete_habit(habits) - show the habits, ask which
        number, remove it from the list, and save.

TODO 7: Write main() - load the habits, then loop showing the menu
        and calling the right function based on the user's choice.

Stretch goal (optional): Add a "streak" field and increase it only if
the habit is marked done on a new day (hint: look at Python's `datetime`
module - we haven't covered it in class, so this is for the curious).
"""

import json
import os

HABITS_FILE = "habits.json"


def load_habits():
    # TODO 1
    pass


def save_habits(habits):
    # TODO 2
    pass


def add_habit(habits):
    # TODO 3
    pass


def view_habits(habits):
    # TODO 4
    pass


def mark_done(habits):
    # TODO 5
    pass


def delete_habit(habits):
    # TODO 6
    pass


def main():
    # TODO 7
    pass


if __name__ == "__main__":
    main()
