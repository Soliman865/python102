# Week 5 — Mini Project: Game High Score Tracker

## 🎯 What You're Building

A command-line app that lets you track high scores for your favourite games.

**It must use everything from weeks 2–4:**
- ✅ OOP — a `Player` class that stores name and scores
- ✅ Error handling — catch bad input, handle missing players
- ✅ `json` module — save scores to a file so they survive when you close the app
- ✅ `datetime` module — record *when* a score was added

---

## 🗂️ How the App Works

```
=== High Score Tracker ===
1. View all players
2. Add a player
3. Add a score for a player
4. View a player's scores
5. Show the top scorer
6. Quit
```

- All data is saved to `scores.json` automatically after every change
- On startup, scores are loaded from `scores.json` if it exists
- If a player name doesn't exist, the app prints a helpful message instead of crashing

---

## ✅ Requirements Checklist

Before you're done, you should be able to say yes to all of these:

- [ ] The `Player` class has `name` and `scores` attributes
- [ ] `Player.add_score(value)` raises a `ValueError` if the score is not a positive number
- [ ] The menu works in a loop until the user picks Quit
- [ ] All scores are saved to `scores.json` — they're still there when you restart the app
- [ ] Each score entry records the value **and** the date/time it was added
- [ ] Bad input (letters where a number is expected) doesn't crash the app

---

## 📁 Files This Week

- `starter.py` — skeleton with TODOs — **start here**
- `solution.py` — reference solution — **try the starter first!**

---

## 💡 Hints

- Use a **dict** to store all players: `{"Alex": <Player object>, "Jordan": <Player object>}`
- To save: convert each Player to a plain dict (`{"name": ..., "scores": [...]}`) before `json.dump()`
- To load: read the JSON file, create Player objects from the saved dicts
- For the date: `datetime.datetime.now().strftime("%Y-%m-%d %H:%M")`
