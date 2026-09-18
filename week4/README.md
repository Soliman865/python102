# Week 4 — Modules & the Standard Library

## 🔁 Quick Recap: File I/O

Reading from a file:
```python
with open("scores.txt", "r") as f:
    content = f.read()
    print(content)
```

Writing to a file:
```python
with open("scores.txt", "w") as f:
    f.write("Alex: 95\n")
    f.write("Jordan: 88\n")
```

Appending (without erasing):
```python
with open("scores.txt", "a") as f:
    f.write("Riley: 91\n")
```

> `"r"` = read, `"w"` = write (overwrites), `"a"` = append

---

## 📚 New Concept: Modules & the Standard Library

A **module** is a file full of ready-made functions and tools. Python comes with hundreds of them — you just `import` the ones you need.

### Importing a module
```python
import math
import random
import datetime
import os
import json
```

### The modules you'll use most this year

#### `math` — maths functions
```python
import math
print(math.sqrt(25))    # 5.0 — square root
print(math.floor(3.9))  # 3   — round down
print(math.ceil(3.1))   # 4   — round up
print(math.pi)          # 3.14159...
```

#### `random` — randomness
```python
import random
print(random.randint(1, 6))         # random int between 1 and 6 (like a dice)
print(random.choice(["red", "blue", "green"]))  # random item from a list
random.shuffle(my_list)             # shuffle a list in place
```

#### `datetime` — dates and times
```python
import datetime
now = datetime.datetime.now()
print(now)                          # 2026-09-18 12:00:00.123456
print(now.strftime("%Y-%m-%d"))     # "2026-09-18"
print(now.strftime("%H:%M"))        # "12:00"
```

#### `json` — save and load Python data as text
```python
import json

data = {"name": "Alex", "score": 95}

# Save to file:
with open("data.json", "w") as f:
    json.dump(data, f)

# Load from file:
with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded["name"])   # Alex
```

> JSON is how most web APIs and save files store data. You'll use it a lot in the project weeks.

#### `os` — talk to the operating system
```python
import os
print(os.getcwd())          # current folder path
print(os.path.exists("data.json"))  # True/False — does the file exist?
os.makedirs("saves", exist_ok=True) # create a folder (no crash if it already exists)
```

---

## 🔑 Key Terms

| Term | Meaning |
|------|---------|
| **module** | A file of reusable Python code you can import |
| **standard library** | The collection of modules that come built into Python |
| `import` | Load a module so you can use its tools |
| **JSON** | A text format for storing data (like a Python dict, saved to a file) |
| `json.dump()` | Write Python data to a JSON file |
| `json.load()` | Read a JSON file back into Python |

---

## 📁 Files This Week

- `lesson.py` — tour of `math`, `random`, `datetime`, `os`, and `json` with real examples
- `exercise.py` — use these modules to build small programs
