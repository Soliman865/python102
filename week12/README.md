# Week 12 — Final Project Showcase

This is your last week of Python102. You're going to build something **you choose**,
using AI as your coding partner — and then present it to the class.

The project doesn't have to be big. It has to be **yours**: something you understand
completely, can explain, and are proud of.

---

## What to Build

You choose the idea. It can be a game, a tool, an app — anything that interests you.

**It must include all three of these:**

| Requirement | What it means |
|-------------|--------------|
| At least one class (OOP) | A class with `__init__`, attributes, and methods — not just functions |
| Error handling | At least one `try/except` and one `raise` — handle bad input gracefully |
| One "outside tool" | A module (`json`, `random`, `datetime`…), an API, or a GUI (Tkinter) |

**Ideas if you're not sure what to build:**

| Idea | What it uses |
|------|-------------|
| 🎮 Text-based mini game (quiz, adventure, guessing) | OOP for game state, json to save progress |
| 📋 Personal to-do list with categories | OOP, json to save/load, datetime for due dates |
| 🌐 "What's on today?" dashboard | API (weather, NASA, news), Tkinter to display it |
| 🎵 Music mood recommender | OOP, random to pick songs, maybe Tkinter |
| 🏋️ Workout tracker | OOP, json to save, datetime to log dates |
| 🃏 Flashcard quiz app | OOP, json to save cards, score tracking |

---

## How to Work This Week

Build it in **small steps with AI**, exactly like weeks 7–10.

1. **Write a one-sentence description** of what your app does
2. **Break it into 3–5 small pieces** before you start prompting
3. **Build one piece at a time** — verify it works before moving to the next
4. **Read every line** the AI gives you before you keep it
5. **Write at least one test** for your most important function (from week 11)

> If you're stuck on what to build: tell the AI your idea in one sentence and ask it
> to break it into 4 small coding steps for you. Then follow those steps one at a time.

---

## Requirements Checklist

Before the showcase, you should be able to say yes to all of these:

- [ ] My project runs from start to finish without crashing
- [ ] I can explain every function and class — not just what it does, but why it's there
- [ ] I tested at least one "bad input" case — it handles it gracefully
- [ ] Data is saved somewhere (a `.json` file, or I can explain why it doesn't need to be)
- [ ] I wrote at least one `unittest` test for a function I care about
- [ ] I can point to one place where the AI got something wrong and show how I fixed it

---

## Showcase Format (last 30 min of class)

Each student gets **3–4 minutes**:

1. **Demo** — run it live, show the main feature working
2. **One thing the AI got wrong** — show the bug, explain how you caught it and fixed it
3. **One thing you're proud of** — a piece of code you understand well and think is good

> No slides needed. Just your code and your terminal.

---

## Push Your Work

```bash
git add .
git commit -m "Week 12 - final project: [describe your project in a few words]"
git push
```

---

## A Note on Using AI

You've used AI every week since week 6. By now you know:
- AI is fast at writing boilerplate, slow at understanding *your* requirements
- The first prompt rarely gives you exactly what you need
- Reading AI code critically is the real skill — not accepting it blindly

Your final project is proof that you've learned that skill.
What you built matters less than the fact that you can fully explain it.
