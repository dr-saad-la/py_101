#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: repr_usage
#
# Description: This program demonstrates the use of `repr()` in Python,
#              showing how it can provide a developer-friendly string
#              representation of various objects, including custom classes.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Using repr() in Python ==========")
    print("This program demonstrates how to use repr() to get detailed representations of objects.")
    print("*" * 80)

    # Demonstrating repr() on built-in types
    built_in_types_examples()

    # Demonstrating repr() on custom classes
    custom_class_example()

    print("*" * 80)


# Function to demonstrate repr() on built-in types
def built_in_types_examples():
    """
    Demonstrates the use of repr() on built-in Python types.
    """
    print("Built-in Types with repr():")

    text = "Hello, world!"
    number = 123.45
    collection = [1, 2, 3]
    dictionary = {"key": "value"}

    # Using repr() to get detailed string representations
    print(f"text: {repr(text)}")
    print(f"number: {repr(number)}")
    print(f"collection: {repr(collection)}")
    print(f"dictionary: {repr(dictionary)}")
    print()


# Custom class with __repr__ method
class Book:
    """
    Represents a Book with a title and author.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        """
        Returns a string representation of the Book instance, designed for developers.
        """
        return f"Book(title={repr(self.title)}, author={repr(self.author)})"


# Function to demonstrate repr() on custom classes
def custom_class_example():
    """
    Demonstrates the use of repr() with a custom class.
    """
    print("Custom Class with repr():")

    # Create an instance of Book
    book = Book("1984", "George Orwell")

    # Using repr() on the custom object
    print(f"book: {repr(book)}")


if __name__ == "__main__":
    main()
