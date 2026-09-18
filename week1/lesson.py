# Week 1 — Lesson: Python Warmup + Your First Class
# We write this together in class. Read the comments as we go.

# ============================================================
# PART 1: Quick Python Recap (5 min)
# ============================================================

# Variables — storing values
name = "Alex"
age = 12
height = 1.52  # in metres

print(name, "is", age, "years old")

# Functions — reusable blocks
def greet(person_name):
    return f"Hello, {person_name}! Welcome to Python102."

print(greet("Jordan"))

# Lists — ordered collections
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Dictionaries — key-value pairs
student = {"name": "Riley", "grade": 7, "score": 95}
print(student["name"], "got", student["score"])


# ============================================================
# PART 2: The Problem With Just Functions (2 min)
# ============================================================

# Imagine tracking 3 dogs with just variables + functions:
dog1_name = "Max"
dog1_breed = "Labrador"

dog2_name = "Luna"
dog2_breed = "Poodle"

def bark(dog_name):
    print(f"{dog_name} says: Woof!")

bark(dog1_name)
bark(dog2_name)

# This works for 2 dogs. What about 100 dogs? Messy!
# OOP solves this.


# ============================================================
# PART 3: Your First Class — Dog (10 min)
# ============================================================

class Dog:
    # __init__ runs automatically when you create a new Dog.
    # Think of it as "set up this dog's details."
    def __init__(self, name, breed):
        self.name = name    # Each dog remembers its own name
        self.breed = breed  # Each dog remembers its own breed

    # A method — something a Dog can DO
    def bark(self):
        print(f"{self.name} says: Woof!")

    # Another method
    def describe(self):
        print(f"I am {self.name} and I am a {self.breed}.")


# Creating Dog objects from the blueprint:
max = Dog("Max", "Labrador")
luna = Dog("Luna", "Poodle")

# Accessing attributes (data):
print(max.name)    # Max
print(luna.breed)  # Poodle

# Calling methods (actions):
max.bark()
luna.bark()
max.describe()
luna.describe()


# ============================================================
# PART 4: Let's Add More to the Class Together (10 min)
# ============================================================

class Dog2:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age        # New attribute: age in years

    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"I am {self.name}, a {self.breed}, {self.age} years old.")

    def is_puppy(self):
        # Returns True if the dog is 2 years old or younger
        return self.age <= 2


buddy = Dog2("Buddy", "Beagle", 1)
rex = Dog2("Rex", "German Shepherd", 5)

buddy.describe()
rex.describe()

print(f"Is {buddy.name} a puppy? {buddy.is_puppy()}")  # True
print(f"Is {rex.name} a puppy? {rex.is_puppy()}")      # False
