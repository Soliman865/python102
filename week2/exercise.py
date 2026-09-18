# Week 2 — Exercises: OOP in Practice
# Try these on your own. Don't look at lesson.py until you've given each one a real go.

# ============================================================
# EXERCISE 1: Build a Superhero class (20 min)
# ============================================================
# Create a Superhero class with these attributes:
#   name        — string
#   power       — string (e.g. "laser vision", "super speed")
#   health      — int (start at 100)
#   energy      — int (start at 50)
#
# And these methods:
#   use_power()
#       → if energy > 0:  print "{name} uses {power}!" and decrease energy by 10
#       → if energy == 0: print "{name} is too tired to use their power!"
#
#   rest()
#       → increase energy by 20 (but never above 50)
#       → print "{name} rested. Energy: {energy}"
#
#   status()
#       → print "[{name}] HP: {health} | Energy: {energy} | Power: {power}"
#
# Then:
# 1. Create two Superhero objects
# 2. Call use_power() 6 times on one of them and watch the energy run out
# 3. Call rest() and try use_power() again

# YOUR CODE HERE:


# ============================================================
# EXERCISE 2: Add an attack() method (10 min)
# ============================================================
# Add a method to your Superhero class:
#
#   attack(other)
#       → if the hero has energy > 0:
#           deal 20 damage to 'other' (call other.take_damage if you added it, or just other.health -= 20)
#           decrease this hero's energy by 10
#           print "{name} attacks {other.name} for 20 damage!"
#       → if no energy:
#           print "{name} has no energy to attack!"
#
# Test: make two heroes fight until one runs out of energy.

# YOUR CODE HERE:


# ============================================================
# EXERCISE 3: A different class — you choose (10 min)
# ============================================================
# Design a class for something YOU care about. It must have:
#   - at least 3 attributes set in __init__
#   - at least 3 methods
#   - at least 1 method that returns a boolean
#   - at least 1 method that changes an attribute
#
# Ideas: Song, Spaceship, Animal, Recipe, Pokemon, Car, BubbleTea order...

# YOUR CODE HERE:


# ============================================================
# EXERCISE 4: Add __str__ to your Superhero (5 min)
# ============================================================
# Add a __str__ method to your Superhero class so that
# print(my_hero) outputs something like:
#   ⚡ Thunderbolt | HP: 100 | Energy: 50 | Power: lightning strike
#
# Test: create a hero and print it directly (not via status()).

# YOUR CODE HERE (modify your Superhero class above):


# ============================================================
# EXERCISE 5: Team class — container of Superheroes (15 min)
# ============================================================
# Create a Team class:
#   __init__(name)         → stores team name and starts with empty members list
#   add_member(hero)       → appends a Superhero; print "{hero.name} joined {team.name}!"
#   remove_member(name)    → removes the hero with that name; print a message if not found
#   roll_call()            → prints every member using their __str__
#   team_energy()          → returns the TOTAL energy of all members added together
#   strongest()            → returns the member with the highest attack (or energy — you pick)
#
# Then:
# 1. Create a team, add 3 superheroes
# 2. Print the team roll call
# 3. Print the total team energy
# 4. Print who the strongest member is
# 5. Remove one member and print roll call again

# YOUR CODE HERE:


# ============================================================
# EXERCISE 6: Class attribute — shared counter (10 min)
# ============================================================
# Add a CLASS attribute called total_created to your Superhero class.
# Every time __init__ runs (i.e. every time a new hero is created),
# increase total_created by 1.
#
# Test:
#   print(Superhero.total_created)   # 0 (before any heroes exist)
#   hero1 = Superhero(...)
#   hero2 = Superhero(...)
#   print(Superhero.total_created)   # 2

# YOUR CODE HERE (modify your Superhero class above):


# ============================================================
# BONUS 1: Battle simulator (if you finish early)
# ============================================================
# Write a function run_battle(fighter1, fighter2) that:
#   - Alternates attacks between the two fighters each "round"
#   - Prints the round number and both fighters' status after each round
#   - Stops when one fighter is defeated (health <= 0)
#   - Prints who won
#
# Use your Superhero class (or GameCharacter from lesson.py).

# YOUR CODE HERE:


# ============================================================
# BONUS 2: Pokémon-style class (if you STILL have time)
# ============================================================
# Build a Pokemon class:
#   Attributes: name, type (e.g. "fire"), hp, moves (a list of move names)
#   Methods:
#     use_move(move_name) → prints "{name} used {move_name}!" if in moves list,
#                           else prints "{name} doesn't know {move_name}!"
#     take_damage(amount) → reduces hp, never below 0
#     is_fainted()        → returns True if hp == 0
#     __str__             → e.g. "Charmander (fire) | HP: 45"
#
# Create 3 Pokémon, put them in a list, and loop through printing each one.

# YOUR CODE HERE:
