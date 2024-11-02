#!/usr/bin/env python3
# =========================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Basic Classes Objects
#
# Description: This program introduces the basic concepts of classes and
#              objects in Python, including defining a simple class,
#              creating objects, and using instance attributes and methods.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =========================================================================

class Person:
    """
    A simple class representing a person with a name and age.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    """

    def __init__(self, name: str, age: int):
        """
        Initialize a new Person instance with a name and age.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def greet(self) -> None:
        """
        Print a greeting from the person, including their name and age.
        """
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

def main():
    print("=== Introduction to Classes and Objects in Python ===\n")

    # Creating instances of the Person class
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)

    # Using the greet method to display information about each person
    person1.greet()
    person2.greet()

if __name__ == "__main__":
    main()
