# Week 3 — Error Handling

## 🔁 Quick Recap

### for loops
```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

for i in range(5):   # 0, 1, 2, 3, 4
    print(i)
```

### while loops
```python
count = 0
while count < 3:
    print(count)
    count += 1
```

### Lists
```python
scores = [90, 85, 78]
scores.append(95)      # add to end
scores.remove(85)      # remove a value
print(scores[0])       # access by index
print(len(scores))     # how many items
```

### Dictionaries
```python
student = {"name": "Alex", "grade": 7}
student["score"] = 98         # add a key
print(student["name"])        # read a value
print("score" in student)     # check if key exists → True
```

> If any of these feel rusty, ask your instructor.

---

## 📚 New Concept: Error Handling

Right now, if a user types something unexpected, your program **crashes**. Error handling lets your program **deal with problems gracefully** instead of stopping.

### What is an Exception?

When Python hits a problem it can't continue from, it raises an **exception** — an error with a type and a message.

Common exceptions you'll see:

| Exception | When it happens |
|-----------|-----------------|
| `ValueError` | Wrong type of value (e.g. `int("hello")`) |
| `IndexError` | List index out of range (`mylist[99]` when list has 3 items) |
| `KeyError` | Dictionary key doesn't exist (`d["missing_key"]`) |
| `ZeroDivisionError` | Dividing by zero |
| `FileNotFoundError` | Trying to open a file that doesn't exist |

### try / except

Wrap risky code in a `try` block. If it fails, the `except` block runs instead of crashing.

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
```

### Raising your own exceptions

Your own classes can raise exceptions too — this is how you say "this is not allowed":

```python
def set_health(self, value):
    if value < 0:
        raise ValueError("Health cannot be negative.")
    self.health = value
```

The caller then decides whether to handle it or let it crash.

---

## 🔑 Key Terms

| Term | Meaning |
|------|---------|
| **exception** | An error that interrupts normal code execution |
| `try` | Block of code that might raise an exception |
| `except` | Block that runs *only if* the `try` block raises an exception |
| `raise` | Manually trigger an exception from your own code |
| `ValueError` | Exception for "wrong kind of value" |
| `IndexError` | Exception for "list index out of range" |

---

## 📁 Files This Week

- `lesson.py` — see what crashes look like, then fix them with `try/except`; add error handling to a class
- `exercise.py` — add error handling to your `Superhero` class from week 2, plus standalone challenges
