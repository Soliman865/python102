# Python102 — Week 1

## OOP Concepts & How Python Works

---

## 👋 Welcome to Python102

- You already know Python basics from Python101
- This semester we go **deeper** — real projects, real AI, real code
- By the end: you'll have built **3 full apps** using AI tools
- Today: two big ideas — _how Python runs your code_ and _OOP_

---

## 🔁 Quick Recap — What You Know

- **Variables** → boxes that store values
- **Functions** → reusable blocks of code
- **Loops** → repeat something many times
- **Lists & Dicts** → store collections of data
- **if/else** → make decisions in code

> If any of these feel fuzzy, don't worry — we'll warm up with them today.

---

## ⚙️ How Does Python Actually Run Your Code?

Two types of languages:

| Compiled (C, Java)                            | Interpreted (Python)                 |
| --------------------------------------------- | ------------------------------------ |
| Translates ALL code to machine language first | Reads and runs code **line by line** |
| Faster to run                                 | Easier to write and test             |
| Errors found before running                   | Errors found while running           |

> Python is an **interpreter** — it reads your `.py` file and executes it top to bottom, one line at a time.

---

## 🔍 What Happens When You Press Run?

```
your_code.py  →  Python Interpreter  →  Output
```

1. Python opens your `.py` file
2. Reads line 1, executes it
3. Reads line 2, executes it
4. Hits an error? **Stops right there** and tells you
5. No error? Keeps going until the last line

> That's why error messages show a **line number** — that's where Python stopped.

---

## 🌍 What Is OOP?

**OOP = Object-Oriented Programming**

The idea: model your code the way the real world works — with **things** (objects) that have:

- 📦 **Data** (what it knows) — called _attributes_
- ⚡ **Actions** (what it can do) — called _methods_

> **Everything in the real world is an object.**  
> A dog has a name and a breed (data) and can bark and sit (actions).

---

## 🐶 Classes vs Objects

- A **Class** is the _blueprint_ (the idea of a Dog)
- An **Object** is a _specific thing_ made from that blueprint (your dog, Max)

```
Class: Dog
  └── Object: max  (name="Max", breed="Lab")
  └── Object: luna (name="Luna", breed="Poodle")
```

> One blueprint → many different objects. Each object has its own data.

---

## 🏗️ Anatomy of a Python Class

```python
class Dog:                        # Class name (capital letter!)
    def __init__(self, name, breed):  # Constructor: runs when you create a Dog
        self.name = name          # Attribute: every dog has a name
        self.breed = breed        # Attribute: every dog has a breed

    def bark(self):               # Method: something a dog can do
        print(f"{self.name} says: Woof!")
```

- `__init__` → called automatically when you create a new Dog
- `self` → means "this specific object" (like saying "my own name")

---

## 🚀 Creating and Using Objects

```python
# Create two Dog objects from the same blueprint
max  = Dog("Max", "Labrador")
luna = Dog("Luna", "Poodle")

# Use their data (attributes)
print(max.name)   # Max
print(luna.breed) # Poodle

# Call their actions (methods)
max.bark()   # Max says: Woof!
luna.bark()  # Luna says: Woof!
```

> Same class, different data, different results.

---

## 4️⃣ The Four Pillars of OOP

You'll learn all four this year — today just learn the names:

| Pillar            | One-liner                                                |
| ----------------- | -------------------------------------------------------- |
| **Encapsulation** | Bundle data + actions together in one class              |
| **Inheritance**   | A new class can _inherit_ from an existing one           |
| **Polymorphism**  | Different classes, same method name, different behaviour |
| **Abstraction**   | Hide complex details, show only what's needed            |

> Today and next week: **Encapsulation**. The rest come later.

---

## ❓ Why OOP? Why Not Just Functions?

Without OOP — juggling everything separately:

```python
dog_name = "Max"
dog_breed = "Lab"
def bark(name): print(f"{name}: Woof!")
```

With OOP — everything belongs together:

```python
max = Dog("Max", "Lab")
max.bark()
```

> As programs get bigger, OOP keeps things **organized** and **reusable**.

---

## 🗓️ What's Coming This Year

| Weeks | Topic                                              |
| ----- | -------------------------------------------------- |
| 1     | Today — OOP intro + Python warmup                  |
| 2–5   | OOP, error handling, modules — with mini exercises |
| 6     | How AI works + using AI tools in VS Code           |
| 7–8   | 🌦️ **Project: AI Weather Mood App**                |
| 9–10  | 🗑️ **Project: AI Trash Sorter**                    |
| 11–12 | 🚀 **Project: TBD**                                |

> The projects are the payoff. Weeks 2–5 give you the tools to actually understand them.

---

## ✅ Before We Code — Check In

Can you answer these?

1. What is the difference between a **class** and an **object**?
2. What does `__init__` do?
3. What does `self` mean inside a class?

> If yes → open VS Code, let's code.  
> If no → ask now! There are no silly questions.
