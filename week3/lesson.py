# Week 3 — Lesson: Error Handling
# We build this together in class. Read every comment.

# ============================================================
# PART 1: Quick Recap — Loops, Lists, Dicts
# ============================================================

# for loop — go through a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# range loop — count through numbers
for i in range(1, 4):      # 1, 2, 3
    print(f"Round {i}")

# while loop — keep going until a condition is False
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

# Lists — add, remove, access
scores = [90, 85, 78]
scores.append(95)           # add 95 to the end
print(scores[0])            # first item → 90
print(len(scores))          # how many items → 4

# Dicts — key-value pairs
student = {"name": "Alex", "grade": 7}
student["score"] = 98       # add a new key
print(student["name"])      # read a value → Alex


# ============================================================
# PART 2: What Happens Without Error Handling
# ============================================================

# Try running each of these lines one at a time.
# They all crash. Notice the error TYPE and the line number.

# int("hello")               # ValueError
# [1, 2, 3][99]              # IndexError
# {"a": 1}["missing"]        # KeyError
# 10 / 0                     # ZeroDivisionError

print("These lines are commented out — they would crash if uncommented.")


# ============================================================
# PART 3: try / except — Handling Errors Gracefully
# ============================================================

# Without error handling:
# user_input = input("Enter a number: ")
# number = int(user_input)  # crashes if user types "hello"

# With error handling:
def safe_int(prompt):
    """Ask for a number, keep asking until the user gives one."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid number. Try again.")


# Catching multiple different exceptions:
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: can't divide by zero.")
        return None
    except TypeError:
        print("Error: both inputs must be numbers.")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # prints error, returns None
print(safe_divide(10, "x")) # prints error, returns None


# ============================================================
# PART 4: Raising Exceptions in Your Own Classes
# ============================================================

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # We decide: depositing 0 or less makes no sense
        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive, got {amount}.")
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(f"Withdrawal amount must be positive, got {amount}.")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Balance: ${self.balance}, requested: ${amount}.")
        self.balance -= amount
        print(f"Withdrew ${amount}. Balance: ${self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")


# Normal usage works fine:
account = BankAccount("Alex", 100)
account.deposit(50)
account.withdraw(30)
account.show_balance()

# Now handle bad input from a caller:
print("\n--- Handling errors when calling BankAccount ---")
try:
    account.withdraw(500)           # More than the balance
except ValueError as e:
    print(f"Caught an error: {e}")

try:
    account.deposit(-10)            # Negative deposit
except ValueError as e:
    print(f"Caught an error: {e}")

print("Program kept running — no crash!")
account.show_balance()


# ============================================================
# PART 5: else and finally in try/except (5 min)
# ============================================================

# else:    runs ONLY if the try block succeeded (no exception)
# finally: ALWAYS runs — even if there was an exception

def read_number_from_string(text):
    try:
        number = int(text)
    except ValueError:
        print(f"  Couldn't convert '{text}' to a number.")
    else:
        # Only reaches here if int(text) worked
        print(f"  Success! Got the number: {number}")
    finally:
        # Always runs — good for cleanup messages
        print(f"  (finished processing '{text}')")

print("\n--- else / finally demo ---")
read_number_from_string("42")       # else runs, then finally
read_number_from_string("hello")    # except runs, then finally


# ============================================================
# PART 6: Custom Exception Classes (10 min)
# ============================================================

# You can create your OWN exception types by inheriting from Exception.
# This makes your error messages more descriptive and lets callers
# catch YOUR specific error instead of a generic ValueError.

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""
    pass   # No extra code needed — inheriting from Exception is enough


class NegativeAmountError(Exception):
    """Raised when a negative amount is passed to deposit or withdraw."""
    pass


class BetterBankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError(f"Amount must be positive, got {amount}.")
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError(f"Amount must be positive, got {amount}.")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Need ${amount}, only have ${self.balance}."
            )
        self.balance -= amount
        print(f"Withdrew ${amount}. Balance: ${self.balance}")


print("\n--- Custom exceptions demo ---")
acct = BetterBankAccount("Jordan", 200)

# Now callers can catch specific error types:
try:
    acct.withdraw(500)
except InsufficientFundsError as e:
    print(f"Funds error: {e}")
except NegativeAmountError as e:
    print(f"Amount error: {e}")

try:
    acct.deposit(-50)
except InsufficientFundsError as e:
    print(f"Funds error: {e}")
except NegativeAmountError as e:
    print(f"Amount error: {e}")


# ============================================================
# PART 7: Handling Errors in Real Situations (5 min)
# ============================================================

# Pattern 1: safely get a value from a dict
def safe_get(dictionary, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default

config = {"theme": "dark", "font_size": 14}
print("\n--- safe dict access ---")
print(safe_get(config, "theme"))       # dark
print(safe_get(config, "language"))    # None (key missing, no crash)
print(safe_get(config, "language", "English"))  # English (custom default)


# Pattern 2: safely read a file that might not exist
def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

print("\n--- safe file read ---")
content = read_file_safe("this_file_does_not_exist.txt")
print(f"Content: {content}")   # None, no crash
