"""
Week 5 - Solution: Habit Tracker
Python102 | Math+Coding Academy

Reference solution. Try the exercise yourself first!
"""

import json
import os

HABITS_FILE = "habits.json"


def load_habits():
    if not os.path.exists(HABITS_FILE):
        return []

    with open(HABITS_FILE, "r") as f:
        return json.load(f)


def save_habits(habits):
    with open(HABITS_FILE, "w") as f:
        json.dump(habits, f, indent=2)


def add_habit(habits):
    name = input("Habit name: ")
    habits.append({"name": name, "times_done": 0})
    save_habits(habits)
    print(f"Added habit: {name}")


def view_habits(habits):
    if not habits:
        print("No habits saved yet.")
        return

    for i, habit in enumerate(habits, start=1):
        print(f"{i}. {habit['name']} - done {habit['times_done']} times")


def mark_done(habits):
    view_habits(habits)
    if not habits:
        return

    try:
        choice = int(input("Which habit did you complete? "))
        habits[choice - 1]["times_done"] += 1
        save_habits(habits)
        print(f"Nice work! {habits[choice - 1]['name']} updated.")
    except (ValueError, IndexError):
        print("That's not a valid habit number.")


def delete_habit(habits):
    view_habits(habits)
    if not habits:
        return

    try:
        choice = int(input("Which habit do you want to delete? "))
        removed = habits.pop(choice - 1)
        save_habits(habits)
        print(f"Deleted {removed['name']}.")
    except (ValueError, IndexError):
        print("That's not a valid habit number.")


def main():
    habits = load_habits()

    while True:
        print("\n--- Habit Tracker ---")
        print("1. View habits")
        print("2. Add habit")
        print("3. Mark habit done")
        print("4. Delete habit")
        print("5. Quit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_habits(habits)
        elif choice == "2":
            add_habit(habits)
        elif choice == "3":
            mark_done(habits)
        elif choice == "4":
            delete_habit(habits)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
