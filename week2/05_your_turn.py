# WEEK 2 · ACTIVITY 5 · EXTRA
#
# Do this only after activities 1 to 4 print PASSED.
#
# You will learn:
#   How to add an object to a list stored on another object.
#
# What to do:
#   1. Run 05_lesson.py first if you have not already.
#   2. Find add_hero. Replace pass with one line.
#   3. Append hero onto the list self.members.
#   4. Run this file.
#   5. You are done when the last line says: Activity 5: PASSED
#
# Only edit add_hero. Leave the CHECK section alone.

class Hero:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_hero(self, hero):
        # TODO: add hero to the list self.members
        self.members.append(hero)
        pass

    def show(self):
        print("Team", self.name)
        for hero in self.members:
            print("-", hero.name)


team = Team("Night Owls")
team.add_hero(Hero("Mira"))
team.add_hero(Hero("Zed"))
team.show()

# CHECK — do not edit below this line
print("---")
if len(team.members) == 2 and team.members[0].name == "Mira" and team.members[1].name == "Zed":
    print("Activity 5: PASSED")
else:
    print("Activity 5: not yet.")
    print("The team should list Mira, then Zed.")
    print("Inside add_hero, use self.members.append(hero).")
