#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: mapping
#
# Description:
# A demonstration of working with mapping types (dictionary) in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("Example Showing The Mapping Data Type")
    demonstrate_dictionary()


def demonstrate_dictionary() -> None:
    """
    Demonstrates how to work with dictionaries in Python.
    """
    # Dictionary example: Storing user information
    user_info = {"name": "Alice", "age": 25}
    print(f"Variable 'user_info' has value: {user_info} and type: {type(user_info)}")
    print(f"User's name is: {user_info['name']}")  # Accessing value by key
    print(f"User's age is: {user_info['age']}")

    # Adding a new key-value pair to the dictionary
    user_info["email"] = "alice@example.com"
    print(f"After adding an email, 'user_info' is now: {user_info}")

    # Updating the user's age
    user_info["age"] = 26
    print(f"After updating the age, 'user_info' is now: {user_info}")

    # Using the `get` method to access a key with a default value
    print(f"User's phone number: {user_info.get('phone', 'Not provided')}\n")


if __name__ == "__main__":
    main()