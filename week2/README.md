# Week 2 — OOP in Practice

## 🔁 Quick Recap

You did Python101 a while ago, so here's a quick refresher before the new stuff.

### Variables & Types
```python
name = "Alex"       # str
age = 12            # int
height = 1.6        # float
is_student = True   # bool
```

### Functions
```python
def greet(name):          # define it
    return f"Hi, {name}!"

message = greet("Jordan") # call it
print(message)
```

### Conditionals
```python
score = 85
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")
```

> If any of these feel rusty, ask your instructor before moving on.

---

## 📚 New Concept: Building Real Classes

Last week you saw the *shape* of a class. This week you build one that actually does something useful.

Three things to get solid this week:

### 1. Attributes — the object's data
```python
self.name = name
self.health = 100
```
Each object gets its own copy of these values. `max.health` and `luna.health` are separate.

### 2. Methods — the object's actions
```python
def take_damage(self, amount):
    self.health -= amount
```
Methods can **read and change** the object's attributes using `self`.

### 3. Object interaction — objects can work with each other
```python
hero.attack(enemy)   # hero calls a method that affects enemy
```
Objects can be passed into methods just like any other value.

---

## 🔑 Key Terms

| Term | Meaning |
|------|---------|
| `class` | Blueprint for creating objects |
| `__init__` | Runs automatically when you create an object — sets up its attributes |
| `self` | The specific object calling the method right now |
| **attribute** | A variable that belongs to an object (`self.name`) |
| **method** | A function that belongs to a class (`def attack(self)`) |
| **instance** | One specific object created from a class (`hero = GameCharacter(...)`) |

---

## 📁 Files This Week

- `lesson.py` — build a `GameCharacter` class step by step, then make two characters fight
- `exercise.py` — build a `Superhero` class from scratch using the same ideas
