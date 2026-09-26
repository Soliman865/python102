# Week 2 — Teacher notes

Students start at `README.md`. This file is for you.

## Why this shape

Week 1 asked students to build a class in a blank `YOUR CODE HERE` block after a long file. They did not know where to start or when they were finished.

This week each activity is one idea, one lesson file, and one your-turn file. The your-turn file already contains the class. Students edit only the `TODO`. The file prints `PASSED` or a specific "not yet" message.

## Class plan (about 70 minutes)

Say this, then stop talking and let them work:

> Last week a class was a blueprint and an object was one thing made from it. Today there are 4 short activities. For each one, run the lesson file, then the your-turn file. You are done with that activity when you see PASSED. Then go to the next number. Ask me if you are stuck. Do not skip.

| Minutes | What you do |
|---------|-------------|
| 0–5 | Show `README.md`. Point at the table. Run `01_lesson.py` together. Point at `self.health = self.health - amount` and say the object's own number changed. |
| 5–15 | They do `01_your_turn.py`. Stay until most of the room sees `Activity 1: PASSED`. |
| 15–20 | Run `02_lesson.py` together. Say: `other` is a second hero, and `other.take_damage(...)` changes that hero. |
| 20–35 | They do `02_your_turn.py`. |
| 35–50 | They do activity 3 on their own (lesson, then your turn). Walk the room. |
| 50–65 | They do activity 4 on their own. |
| 65–70 | Early finishers start activity 5. Everyone else stops at activity 4. |

Do not lecture class attributes or `__str__` before they open the file. The lesson file is the explanation.

If the class is slow, stop after activity 3. Activity 4 still belongs to this week; start next class with it before week 3.

## Answer key

Activity 1, inside `heal`:

```python
self.health = self.health + amount
print(f"{self.name} healed {amount}. Health is now {self.health}.")
```

Activity 2, inside `attack`:

```python
other.take_damage(self.power)
print(f"{self.name} hits {other.name} for {self.power} damage.")
```

Activity 3, inside `__str__`:

```python
return f"{self.name} | health: {self.health}"
```

Activity 4, inside `__init__`, after `self.name = name`:

```python
Hero.heroes_made = Hero.heroes_made + 1
```

Activity 5, inside `add_hero`:

```python
self.members.append(hero)
```

Wording of the `print` in activities 1 and 2 can vary. `PASSED` checks the number, not the sentence. Activity 3 must match the string exactly.

## Stuck points to watch for

- They edit the lesson file. Point them at `your_turn`.
- They forget to delete `pass`, or their new lines are not indented with the `TODO`.
- Activity 2: they damage `self` instead of `other`, or they type `take_damage(10)` instead of `take_damage(self.power)`.
- Activity 3: missing spaces, or they return the words `Mira | health: 80` from the lesson instead of using `self.name` and `self.health`.
- Activity 4: they write `self.heroes_made` instead of `Hero.heroes_made`. The "not yet" message already says this.
- Activity 5: they write `append` on the hero instead of on `self.members`.
