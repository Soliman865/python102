# Week 4 — Lesson: Modules & the Standard Library
# We explore this together in class. Read every comment.

import math
import random
import datetime
import os
import json

# ============================================================
# PART 1: Quick Recap — File I/O
# ============================================================

# Writing to a text file
with open("notes.txt", "w") as f:
    f.write("Hello from Python102!\n")
    f.write("File I/O lets us save data.\n")

# Reading it back
with open("notes.txt", "r") as f:
    content = f.read()
print("File contents:")
print(content)

# Appending (adding without erasing)
with open("notes.txt", "a") as f:
    f.write("This line was added later.\n")

# Clean up
os.remove("notes.txt")
print("(notes.txt cleaned up)\n")


# ============================================================
# PART 2: math — Built-in Maths Functions
# ============================================================

print("=== math module ===")
print(math.sqrt(144))       # 12.0  — square root
print(math.floor(7.9))      # 7     — round DOWN
print(math.ceil(7.1))       # 8     — round UP
print(round(7.5))           # 8     — standard rounding
print(math.pi)              # 3.14159...
print(math.pow(2, 10))      # 1024.0 — 2 to the power of 10
print()


# ============================================================
# PART 3: random — Randomness
# ============================================================

print("=== random module ===")

# Random integer (both ends included)
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

# Random item from a list
colours = ["red", "green", "blue", "yellow"]
picked = random.choice(colours)
print(f"Random colour: {picked}")

# Shuffle a list in place
cards = ["Ace", "King", "Queen", "Jack"]
random.shuffle(cards)
print(f"Shuffled cards: {cards}")

# Random float between 0 and 1
chance = random.random()
print(f"Random float: {chance:.2f}")   # 2 decimal places
print()


# ============================================================
# PART 4: datetime — Dates and Times
# ============================================================

print("=== datetime module ===")

now = datetime.datetime.now()
print(f"Right now: {now}")
print(f"Just the date: {now.strftime('%Y-%m-%d')}")
print(f"Just the time: {now.strftime('%H:%M:%S')}")
print(f"Friendly format: {now.strftime('%B %d, %Y')}")  # e.g. September 18, 2026

# You can also create a specific date
birthday = datetime.date(2014, 3, 15)
print(f"Birthday: {birthday}")
print()


# ============================================================
# PART 5: json — Save and Load Python Data
# ============================================================

print("=== json module ===")

# A Python dict we want to save
player_data = {
    "name": "Alex",
    "level": 5,
    "scores": [95, 87, 102],
    "active": True
}

# Save to a .json file
with open("player.json", "w") as f:
    json.dump(player_data, f, indent=2)   # indent=2 makes it human-readable
print("Saved player.json")

# Load it back
with open("player.json", "r") as f:
    loaded_data = json.load(f)

print(f"Loaded: {loaded_data}")
print(f"Player name: {loaded_data['name']}")
print(f"Top score: {max(loaded_data['scores'])}")

# Clean up
os.remove("player.json")
print("(player.json cleaned up)\n")


# ============================================================
# PART 6: os — Talk to the Operating System
# ============================================================

print("=== os module ===")
print(f"Current folder: {os.getcwd()}")

# Check if a file exists before trying to open it
filename = "scores.json"
if os.path.exists(filename):
    print(f"{filename} exists!")
else:
    print(f"{filename} does not exist (that's fine).")

# Create a folder safely (no crash if it already exists)
os.makedirs("my_saves", exist_ok=True)
print("Created 'my_saves' folder (or it already existed).")

# Clean up
os.rmdir("my_saves")
print("(my_saves folder cleaned up)")
