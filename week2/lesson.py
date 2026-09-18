# Week 2 — Lesson: OOP in Practice
# We build this together in class. Read every comment.

# ============================================================
# PART 1: Quick Recap — Variables, Functions, Conditionals
# ============================================================

# Variables — Python remembers values for you
player_name = "Alex"
player_score = 0
is_alive = True

# Function — reusable block of code
def show_status(name, score):
    print(f"{name} | Score: {score}")

show_status(player_name, player_score)

# Conditional — make decisions
if is_alive:
    print(f"{player_name} is still in the game.")
else:
    print(f"{player_name} is out!")


# ============================================================
# PART 2: The Problem With Just Variables (2 min)
# ============================================================

# If we have two players using only variables, it gets messy fast:
p1_name = "Alex"
p1_health = 100
p1_attack = 15

p2_name = "Jordan"
p2_health = 100
p2_attack = 20

# What if we have 10 players? 100? That's 300+ variables. 
# OOP solves this with classes.


# ============================================================
# PART 3: The GameCharacter Class (15 min)
# ============================================================

class GameCharacter:
    def __init__(self, name, health, attack_power):
        # These three attributes belong to every GameCharacter
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        # Returns True if this character still has health
        return self.health > 0

    def take_damage(self, amount):
        # Reduce health by amount, but never go below 0
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {amount} damage! Health: {self.health}")

    def heal(self, amount):
        # Restore some health
        self.health += amount
        print(f"{self.name} healed {amount} HP! Health: {self.health}")

    def status(self):
        # Print a summary of this character's current state
        alive_str = "alive" if self.is_alive() else "defeated"
        print(f"[{self.name}] HP: {self.health} | ATK: {self.attack_power} | {alive_str}")


# Create two characters
hero = GameCharacter("Alex", 100, 15)
villain = GameCharacter("Dark Lord", 80, 25)

# Read their attributes
print(hero.name)          # Alex
print(villain.attack_power)  # 25

# Call their methods
hero.status()
villain.status()

hero.take_damage(30)
villain.heal(10)

hero.status()
villain.status()


# ============================================================
# PART 4: Objects Interacting — a Simple Battle (10 min)
# ============================================================

class GameCharacter2:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def attack(self, other):
        # 'other' is another GameCharacter2 object — we can call its methods!
        if not self.is_alive():
            print(f"{self.name} is defeated and can't attack.")
            return
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")
        other.take_damage(self.attack_power)
        if not other.is_alive():
            print(f"{other.name} has been defeated!")

    def status(self):
        state = "alive" if self.is_alive() else "defeated"
        print(f"[{self.name}] HP: {self.health} | ATK: {self.attack_power} | {state}")


# Let them fight!
knight = GameCharacter2("Knight", 100, 18)
dragon = GameCharacter2("Dragon", 150, 30)

print("=== Battle Start ===")
knight.status()
dragon.status()
print()

# Round 1
knight.attack(dragon)
dragon.attack(knight)
print()

# Round 2
knight.attack(dragon)
dragon.attack(knight)
print()

knight.status()
dragon.status()


# ============================================================
# PART 5: __str__ — Make Objects Print Nicely (5 min)
# ============================================================

# Right now, if you print an object directly you get something ugly:
# print(knight)  →  <__main__.GameCharacter2 object at 0x10a3f2e10>
#
# __str__ lets you control what print() shows for your object.

class GameCharacter3:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def __str__(self):
        # This runs automatically when you do print(character) or str(character)
        state = "alive" if self.is_alive() else "defeated"
        return f"[{self.name}] HP:{self.health} ATK:{self.attack_power} ({state})"


hero3 = GameCharacter3("Aria", 90, 22)
boss3 = GameCharacter3("Golem", 200, 12)

print(hero3)   # [Aria] HP:90 ATK:22 (alive)
print(boss3)   # [Golem] HP:200 ATK:12 (alive)

hero3.take_damage(200)
print(hero3)   # [Aria] HP:0 ATK:22 (defeated)


# ============================================================
# PART 6: Class Attributes vs Instance Attributes (5 min)
# ============================================================

# Instance attribute: belongs to ONE specific object  (self.name)
# Class attribute:    belongs to the CLASS — shared by ALL objects

class GameCharacter4:
    max_health = 100   # CLASS attribute — same for every character

    def __init__(self, name, attack_power):
        self.name = name                          # instance attribute — unique per object
        self.health = GameCharacter4.max_health   # start at the class max
        self.attack_power = attack_power

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def __str__(self):
        return f"{self.name} | HP:{self.health}/{GameCharacter4.max_health}"


c1 = GameCharacter4("Mage", 20)
c2 = GameCharacter4("Rogue", 35)
print(c1)   # Mage | HP:100/100
print(c2)   # Rogue | HP:100/100

# Change the class attribute — all future objects use the new value
GameCharacter4.max_health = 150
c3 = GameCharacter4("Paladin", 18)
print(c3)   # Paladin | HP:100/150


# ============================================================
# PART 7: A Container Class — Party (10 min)
# ============================================================
# A class can hold a LIST of other objects as an attribute.
# This is a very common pattern: one object "owns" a collection of others.

class Party:
    def __init__(self, name):
        self.name = name
        self.members = []    # list of GameCharacter3 objects

    def add_member(self, character):
        self.members.append(character)
        print(f"{character.name} joined {self.name}!")

    def roll_call(self):
        print(f"\n=== {self.name} ===")
        if not self.members:
            print("  (empty)")
        for member in self.members:
            print(f"  {member}")   # __str__ is called automatically here

    def is_wiped_out(self):
        # True only if EVERY member has been defeated
        return all(not m.is_alive() for m in self.members)

    def alive_count(self):
        return sum(1 for m in self.members if m.is_alive())


# Build a party
party = Party("The Brave Ones")
party.add_member(GameCharacter3("Aria", 90, 22))
party.add_member(GameCharacter3("Borin", 120, 18))
party.add_member(GameCharacter3("Zara", 75, 30))

party.roll_call()
print(f"Alive: {party.alive_count()}")
print(f"Wiped out? {party.is_wiped_out()}")

# Defeat everyone and check again
for member in party.members:
    member.take_damage(999)

party.roll_call()
print(f"Wiped out? {party.is_wiped_out()}")
