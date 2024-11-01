#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: lambda_functions_01
#
# Description: Demonstrates the use of lambda functions (anonymous functions)
#              in Python. This includes defining lambda functions for short
#              operations, as well as examples of using them in real-world
#              scenarios like filtering and sorting data.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Lambda Functions (Anonymous Functions) in Python ==========")
    print("This lesson demonstrates lambda functions, their syntax, and real-world uses.")
    print("*" * 80)

    # Basic examples of lambda functions
    print("1. Basic Lambda Function Examples")
    basic_lambda_examples()
    print("*" * 80)

    # Real-world example: Sorting and filtering with lambda
    print("2. Real-World Examples Using Lambda Functions")
    lambda_real_world_examples()
    print("*" * 80)


# Basic examples of lambda functions
def basic_lambda_examples():
    """
    Demonstrates simple lambda functions for common tasks.
    """
    # Simple addition lambda function
    add = lambda x, y: x + y
    print("Addition using lambda (3 + 5):", add(3, 5))  # Output: 8

    # Lambda function to calculate the square of a number
    square = lambda x: x * x
    print("Square of 4 using lambda:", square(4))  # Output: 16

    # Lambda function to extract last name from a full name
    get_last_name = lambda name: name.split()[-1]
    print("Extract last name from 'John Michael Doe':", get_last_name("John Michael Doe"))  # Output: Doe


# Real-world examples of using lambda functions
def lambda_real_world_examples():
    """
    Demonstrates real-world use cases of lambda functions,
    such as filtering and sorting data.
    """
    # Sorting a list of tuples based on the second item (age) using lambda
    people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
    sorted_people = sorted(people, key=lambda person: person[1])
    print("People sorted by age using lambda:", sorted_people)  # Output: [('Bob', 20), ('Alice', 25), ('Charlie', 30)]

    # Filtering a list to find even numbers using lambda
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("Filtered even numbers using lambda:", even_numbers)  # Output: [2, 4, 6]

    # Lambda function to check if a word is longer than 4 characters, used with filter
    words = ["Python", "is", "fun", "for", "coding"]
    long_words = list(filter(lambda word: len(word) > 4, words))
    print("Words with more than 4 characters:", long_words)  # Output: ['Python', 'coding']


if __name__ == "__main__":
    main()
