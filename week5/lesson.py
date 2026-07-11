"""
Week 5 - Mini Project 1: Personal Data App (no AI)
Python102 | Math+Coding Academy

This is the code we build together in class. It combines everything from
Weeks 1-4:
  - Week 1: Python + VS Code basics
  - Week 2: Git and GitHub
  - Week 3: Lists and Dictionaries
  - Week 4: File I/O and Data Persistence

PROJECT: Contact Book
A command-line app that lets a user add, view, search, and delete contacts,
saving them to a file so the data survives after the program closes.

No AI/APIs this week - that starts in Week 6. This is a checkpoint to prove
the fundamentals are solid before we add AI on top of them.
"""

import json
import os

DATA_FILE = "contacts.json"


# ---------------------------------------------------------------
# STEP 1: Load existing contacts from disk when the app starts.
# We use a list of dictionaries: each contact is one dict.
# ---------------------------------------------------------------
def load_contacts():
    if not os.path.exists(DATA_FILE):
        return []  # no file yet, start with an empty list

    with open(DATA_FILE, "r") as f:
        return json.load(f)


# ---------------------------------------------------------------
# STEP 2: Save the current list of contacts back to disk.
# We call this after every change so nothing is lost.
# ---------------------------------------------------------------
def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=2)


# ---------------------------------------------------------------
# STEP 3: Add a new contact.
# Each contact is a dictionary with name, phone, and email.
# ---------------------------------------------------------------
def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"Added {name}.")


# ---------------------------------------------------------------
# STEP 4: View all contacts.
# We loop through the list and print each dictionary's values.
# ---------------------------------------------------------------
def view_contacts(contacts):
    if not contacts:
        print("No contacts saved yet.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")


# ---------------------------------------------------------------
# STEP 5: Search for a contact by name.
# This shows how to loop through a list of dicts and check a key.
# ---------------------------------------------------------------
def search_contact(contacts):
    query = input("Search name: ").lower()
    found = False

    for contact in contacts:
        if query in contact["name"].lower():
            print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
            found = True

    if not found:
        print("No matches found.")


# ---------------------------------------------------------------
# STEP 6: Delete a contact by number (shown in view_contacts).
# ---------------------------------------------------------------
def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    try:
        choice = int(input("Enter the number of the contact to delete: "))
        removed = contacts.pop(choice - 1)
        save_contacts(contacts)
        print(f"Deleted {removed['name']}.")
    except (ValueError, IndexError):
        print("That's not a valid contact number.")


# ---------------------------------------------------------------
# STEP 7: The menu loop that ties everything together.
# ---------------------------------------------------------------
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book ---")
        print("1. View contacts")
        print("2. Add contact")
        print("3. Search contacts")
        print("4. Delete contact")
        print("5. Quit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
