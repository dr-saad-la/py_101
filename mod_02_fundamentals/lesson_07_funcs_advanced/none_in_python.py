#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: none_in_python
#
# Description: This program demonstrates the concept of `None` in Python,
#              showcasing its usage as a placeholder, default function
#              return value, and comparison techniques.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Exploring None in Python ==========")

    # 1. None as a Placeholder
    print("\nUsing None as a Placeholder")
    placeholder_variable = None  # Initializing variable with None
    print("Placeholder value:", placeholder_variable)

    # Check if a variable is None
    if placeholder_variable is None:
        print("The variable is currently None.")

    # 2. None as a Default Function Return Value
    print("\nFunction Returning None by Default")
    result = function_with_no_return()
    print("Result of calling function_with_no_return():", result)

    # 3. None as a Function Parameter Default Value
    print("\nUsing None as a Default Parameter in a Function")
    greet_user()  # Calls with default value None
    greet_user("Dr. Laouadi")  # Calls with a specific argument

    # 4. Comparisons with None
    print("\nComparing with None using is vs ==")
    test_var = None
    print("test_var is None:", test_var is None)  # Preferred way
    print("test_var == None:", test_var == None)  # Works, but less precise

    # 5. Using None in Conditional Checks
    print("\nConditional Checks with None")
    response = process_input(None)  # Pass None as input
    print("Response:", response)

# Function with no return statement
def function_with_no_return():
    """
    Demonstrates that a function without a return statement implicitly returns None.
    """
    print("This function has no explicit return statement.")

# Function with None as a default parameter value
def greet_user(name=None):
    """
    Greets a user if a name is provided; otherwise, it prompts for a name.

    Args:
        name (str or None): The name of the user. Defaults to None.
    """
    if name is None:
        print("Hello, guest! Please provide your name next time.")
    else:
        print(f"Hello, {name}!")

# Function that processes an input and returns a message
def process_input(user_input):
    """
    Processes user input and returns a message. If input is None, prompts for input.

    Args:
        user_input (str or None): User input.

    Returns:
        str: Processed message.
    """
    if user_input is None:
        return "No input provided, please enter some data."
    else:
        return f"Processing input: {user_input}"

if __name__ == "__main__":
    main()
