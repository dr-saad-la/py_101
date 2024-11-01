#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: closures_01
#
# Description: Demonstrates the concept of closures in Python. Closures
#              allow a nested function to capture and retain access to
#              variables from its enclosing function's scope, even after
#              the outer function has completed execution.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Closures in Python ==========")
    print("A closure is a function that retains access to the variables in its enclosing scope,")
    print("even after the outer function has completed.")
    print("*" * 80)

    # Basic closure example
    basic_closure_example()
    # Counter example using closures
    counter_example()
    # Real-world example: Greeting message generator
    greeting_message_generator()

    print("*" * 80)

# Basic closure example
def basic_closure_example():
    """
    Demonstrates a basic closure where the inner function retains access
    to the variable `text` from the outer function `outer_function`.
    """
    def outer_function(text):
        def inner_function():
            print(text)
        return inner_function

    # Creating a closure
    closure_example = outer_function("Hello, world!")
    print("Basic Closure Example:")
    closure_example()  # Output: Hello, world!

# Counter example using closures
def counter_example():
    """
    Demonstrates a closure that acts as a simple counter.
    Each time the counter function is called, it remembers the current
    count and increments it.
    """
    def create_counter():
        count = 0  # Enclosing variable

        def increment():
            nonlocal count  # Access and modify the enclosing variable
            count += 1
            return count

        return increment

    # Using the closure
    counter = create_counter()
    print("\nCounter Example Using Closures:")
    print(counter())  # Output: 1
    print(counter())  # Output: 2
    print(counter())  # Output: 3

# Real-world example: Greeting message generator
def greeting_message_generator():
    """
    Creates a greeting generator function that takes a name as input
    and generates personalized greeting messages by retaining access
    to the initial greeting template in the closure.
    """
    def create_greeting(greeting_template):
        def greet(name):
            return f"{greeting_template}, {name}!"
        return greet

    # Using the closure to create personalized greetings
    morning_greeting = create_greeting("Good morning")
    evening_greeting = create_greeting("Good evening")

    print("\nReal-World Example: Greeting Message Generator")
    print(morning_greeting("Alice"))   # Output: Good morning, Alice!
    print(evening_greeting("Bob"))     # Output: Good evening, Bob!
    print(morning_greeting("Charlie")) # Output: Good morning, Charlie!

if __name__ == "__main__":
    main()
