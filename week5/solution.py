# Week 5 — Solution: Game High Score Tracker
# Reference solution — try starter.py first!

import json
import datetime
import os

SAVE_FILE = "scores.json"


class Player:
    def __init__(self, name):
        self.name = name
        self.scores = []   # list of {"value": int, "date": str}

    def add_score(self, value):
        if value <= 0:
            raise ValueError(f"Score must be a positive number, got {value}.")
        entry = {
            "value": value,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.scores.append(entry)
        print(f"{self.name} scored {value}!")

    def best_score(self):
        if not self.scores:
            return 0
        return max(entry["value"] for entry in self.scores)

    def show_scores(self):
        if not self.scores:
            print(f"{self.name} has no scores yet.")
            return
        print(f"\n--- {self.name}'s Scores ---")
        for entry in self.scores:
            print(f"  {entry['value']} — {entry['date']}")

    def to_dict(self):
        return {"name": self.name, "scores": self.scores}

    @staticmethod
    def from_dict(data):
        player = Player(data["name"])
        player.scores = data["scores"]
        return player


def save_all(players):
    data = [p.to_dict() for p in players.values()]
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("Saved.")

def load_all():
    if not os.path.exists(SAVE_FILE):
        return {}
    with open(SAVE_FILE, "r") as f:
        data = json.load(f)
    return {entry["name"]: Player.from_dict(entry) for entry in data}


def view_all_players(players):
    if not players:
        print("No players yet.")
        return
    print("\n--- All Players ---")
    for name, player in players.items():
        print(f"  {name} | Best score: {player.best_score()}")

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
    top = max(players.values(), key=lambda p: p.best_score())
    print(f"\nTop scorer: {top.name} with {top.best_score()} points")


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
