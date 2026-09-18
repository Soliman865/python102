# Week 5 — Starter: Game High Score Tracker
# Read week5/README.md first for the full spec.
#
# This file has the skeleton. Fill in every section marked TODO.
# Run it after each section to check your progress.

import json
import datetime
import os

SAVE_FILE = "scores.json"

# ============================================================
# The Player Class
# ============================================================

class Player:
    def __init__(self, name):
        self.name = name
        # Each score entry will be a dict: {"value": 95, "date": "2026-09-18 12:00"}
        self.scores = []

    def add_score(self, value):
        # TODO: raise a ValueError if value is not a positive number (i.e. <= 0)
        # TODO: create a score entry dict with "value" and "date" (use datetime)
        # TODO: append it to self.scores
        # TODO: print "{name} scored {value}!"
        pass

    def best_score(self):
        # TODO: return the highest score value in self.scores
        # TODO: return 0 if there are no scores yet
        pass

    def show_scores(self):
        # TODO: if no scores, print "{name} has no scores yet."
        # TODO: otherwise print each score entry as:
        #       "  95 — 2026-09-18 12:00"
        pass

    def to_dict(self):
        # TODO: return a plain dict so we can save to JSON:
        # {"name": self.name, "scores": self.scores}
        pass

    @staticmethod
    def from_dict(data):
        # TODO: create a Player from a saved dict
        # Hint: create a Player, then set player.scores = data["scores"], return it
        pass


# ============================================================
# Save / Load
# ============================================================

def save_all(players):
    # TODO: convert each Player in the dict to a plain dict using to_dict()
    # TODO: write the list to SAVE_FILE using json.dump with indent=2
    # TODO: print "Saved."
    pass

def load_all():
    # TODO: if SAVE_FILE does not exist (use os.path.exists), return an empty dict {}
    # TODO: open SAVE_FILE, json.load it
    # TODO: convert each saved dict back to a Player using Player.from_dict()
    # TODO: return a dict of {player_name: Player object}
    pass


# ============================================================
# Menu Actions
# ============================================================

def view_all_players(players):
    if not players:
        print("No players yet.")
        return
    print("\n--- All Players ---")
    for name, player in players.items():
        best = player.best_score()
        print(f"  {name} | Best score: {best}")

def add_player(players):
    name = input("Enter player name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in players:
        print(f"{name} already exists.")
        return
    players[name] = Player(name)
    print(f"Player '{name}' added.")

def add_score_for_player(players):
    name = input("Player name: ").strip()
    if name not in players:
        print(f"No player named '{name}'.")
        return
    try:
        value = int(input("Score: "))
        players[name].add_score(value)
    except ValueError as e:
        print(f"Error: {e}")

def view_player_scores(players):
    name = input("Player name: ").strip()
    if name not in players:
        print(f"No player named '{name}'.")
        return
    players[name].show_scores()

def show_top_scorer(players):
    if not players:
        print("No players yet.")
        return
    # TODO: find the player with the highest best_score() and print their name and score
    pass


# ============================================================
# Main Menu Loop
# ============================================================

def main():
    players = load_all()
    print("=== High Score Tracker ===")

    while True:
        print("\n1. View all players")
        print("2. Add a player")
        print("3. Add a score")
        print("4. View a player's scores")
        print("5. Show top scorer")
        print("6. Quit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            view_all_players(players)
        elif choice == "2":
            add_player(players)
            save_all(players)
        elif choice == "3":
            add_score_for_player(players)
            save_all(players)
        elif choice == "4":
            view_player_scores(players)
        elif choice == "5":
            show_top_scorer(players)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1–6.")

if __name__ == "__main__":
    main()
