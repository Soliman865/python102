# Week 11 — Debugging AI Code

You've used AI tools (Gemini, Copilot, etc.) to help build things this term.
AI-written code has a specific problem plain code doesn't: it almost always
**runs without crashing**, and often **looks correct**, even when it isn't. A
typo announces itself with a crash. A subtly wrong AI-generated function just
quietly gives you the wrong answer and keeps running.

This week is about closing that gap: finding bugs that don't crash, and then
learning to check code automatically instead of by eye.

## Files in this folder

| File | What it covers |
|---|---|
| `lesson.py` | 6 rounds of "find the bug," done together in class, then an intro to `unittest` — writing a check once instead of eyeballing output every time |
| `exercise.py` | 4 more bugs to find on your own, writing your own tests, and (if you finish) auditing a function from one of your own AI-assisted projects |

## Read/do these in order

`lesson.py` first, as a class — each round is: read it, guess the bug, run
it to confirm, fix it. Don't skip to `exercise.py` until you've seen the
`unittest` section at the bottom of `lesson.py`; the exercises assume you
already know how to write a `TestCase`.

## What you need before starting

- Comfortable with: functions, lists, dictionaries, `if`/`elif`/`else`,
  `for`/`while` loops (Weeks 1–5)
- Some experience having AI help write code for a project (Weeks 6–10)
- Your GitHub repo, ready to `add`, `commit`, and `push` your work this week too

## The three ways AI code goes wrong

> **Confidently wrong** — it runs and gives a plausible-looking answer that's
> just incorrect (off-by-one errors, flipped comparisons).
>
> **Silently wrong** — it hides a problem instead of surfacing it, so the
> program keeps running with bad data and nobody notices.
>
> **Over-engineered** — it works, but does more than you asked for or can
> explain, which makes it hard to trust or maintain.

Every bug in this week's files is one of these three. Part of the exercise
is naming which one you're looking at — that's what makes you faster at
spotting the same pattern next time.

## The one rule to remember

> If you can't explain what a line of code does and why it's there, that's
> the line to test first — not the line to trust because it ran.

## Last class

This term you went from writing code alone to reading code written by AI, questioning it, breaking it on purpose, and proving it actually works. That's the real skill now: not writing every line yourself, but knowing when to trust what you're given and when to check it.

Keep questioning what AI hands you. That habit will matter more than any single project you built this term.
