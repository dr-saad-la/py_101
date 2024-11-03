#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: generator_functions
#
# Description: This program demonstrates generator functions in Python.
#              Generator functions use the `yield` keyword to return
#              values lazily, one at a time. This allows for efficient
#              processing of large data sets. Additionally, it showcases
#              the `yield from` syntax for delegating to a subgenerator.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Generator Functions in Python ==========")
    print("Generators allow efficient data processing by yielding values one at a time.")
    print("*" * 80)

    # Simple countdown generator using yield
    print("Countdown from 5:")
    for number in countdown(5):
        print(number)

    print("*" * 80)

    # Using yield from to delegate to another generator
    print("Nested countdown sequence using yield from:")
    for value in nested_countdown():
        print(value)

    print("*" * 80)

# Generator function for a countdown
def countdown(n):
    """
    A generator that counts down from n to 1.
    """
    while n > 0:
        yield n
        n -= 1

# Generator function that demonstrates `yield from`
def nested_countdown():
    """
    A generator that uses `yield from` to delegate yielding values from multiple subgenerators.
    """
    print("Starting countdown from 3:")
    yield from countdown(3)
    print("Starting countdown from 2:")
    yield from countdown(2)

if __name__ == "__main__":
    main()
