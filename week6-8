# Weeks 6-8: Building a Habit Tracker With AI

You're going to build this over 3 weeks with Gemini or Copilot as your
coding partner. The AI writes a lot of the code. Your job is to drive it,
run everything yourself, and be able to explain what it wrote before you
move on. If you can't explain a piece, stop and ask the AI (or your
instructor) to walk you through it before continuing.

## The 3-week build

| Week | You build | New idea |
|---|---|---|
| 6 | A working CLI habit tracker, plain functions + dictionaries | Prompting AI for code you already understand the shape of |
| 7 | Refactor it into classes (`Habit`, `HabitTracker`) | Reading AI code that's more advanced than what you'd write yourself |
| 8 | Add a Tkinter GUI on top of the same logic | One set of functions, two different interfaces |

---

## Week 6: CLI version

**Goal:** a menu-driven program: view, add, mark done, delete, quit. Saves to `habits.json`.

**Prompt to give the AI:**
> "Write a Python command-line habit tracker. Habits are stored as a list of
> dictionaries with `name` and `times_done`. Menu options: view habits, add a
> habit, mark a habit done, delete a habit, quit. Save to habits.json after
> every change and load it on startup."

**Do this, don't just read it:**
1. Run it. Add 2-3 habits, mark one done, quit, run it again, confirm they're still there.
2. Find the line that saves to the file, and the line that loads it. Point them out to your instructor.
3. Type `4` at the menu with an empty habit list. Does it crash? If it does, ask the AI to fix it, then explain the fix back in your own words.

**Checkpoint before Week 7:**
- [ ] You can explain, without looking, what happens between typing `2` at the menu and your habit showing up in `habits.json`
- [ ] You tried at least one input that breaks it, and either fixed it or understand why it broke

---

## Week 7: Refactor into classes

**Goal:** same behavior, but a `Habit` and a `HabitTracker` class instead of dicts and loose functions.

**Prompt to give the AI:**
> "Refactor this into a `Habit` dataclass with `name` and `times_done`, and a
> `HabitTracker` class that handles loading, saving, adding, marking done, and
> deleting. Keep the same JSON file format."

**Do this, don't just accept it:**
1. Before running anything, read `Habit` out loud. What does `@dataclass` save you from typing?
2. Find `to_dict()` / `from_dict()`. Ask: why do we need these if `Habit` already holds the data? (Hint: JSON only understands lists and dicts, not custom Python objects.)
3. Find where `HabitTracker` raises an error (`ValueError`, `IndexError`) instead of printing one. Ask the AI: "why raise instead of just printing here?"
4. Run the CLI again. Behavior should be identical to Week 6: if it isn't, that's a bug in the refactor, not a new feature.

**Checkpoint before Week 8:**
- [ ] You can explain what `to_dict()` and `from_dict()` are for, in your own words
- [ ] You can point to where `HabitTracker` stores the file path and why it's not a global variable anymore

---

## Week 8: Add a GUI

**Goal:** the same `HabitTracker` logic, now with a Tkinter window instead of (or alongside) the menu.

**Prompt to give the AI:**
> "Add a Tkinter GUI on top of my existing HabitTracker class. A listbox
> showing habits, an entry box + Add button, and Complete/Delete buttons for
> the selected habit. Keep the CLI working too: let me choose CLI or GUI
> with a command-line flag."

**Do this, don't just accept it:**
1. Run `python app.py --cli`: confirm the old menu still works exactly like Week 7.
2. Run `python app.py --gui`: try the buttons.
3. Find `refresh_list()`. Ask: why does every button call this at the end? What would happen if `add_habit()` forgot to call it?
4. Trace one click, out loud, start to finish: Add button → which function runs → which `HabitTracker` method gets called → what shows up on screen.

**Checkpoint: you should be able to say, honestly:**
- [ ] "I know what every function in this project does"
- [ ] "I've broken it on purpose at least once and fixed it myself"
- [ ] "If the AI had gotten something wrong here, I think I'd have caught it"

That last one is the actual goal of these 3 weeks: not the working app, the ability to tell whether it's *actually* working.

---

## Push your work

Same routine as always, at the end of each week:
```bash
git add .
git commit -m "Week 6/7/8 - describe what changed"
git push
```
