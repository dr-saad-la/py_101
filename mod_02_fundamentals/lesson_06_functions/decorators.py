#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: function_decorators
#
# Description: This program demonstrates the use of decorators in Python,
#              specifically a logging decorator that logs the function
#              name, arguments, and return value. Decorators allow us to
#              modify or enhance the behavior of functions or methods without
#              changing their code.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Function Decorators in Python ==========")
    print("This program uses a decorator to log function calls.")
    print("*" * 80)

    # Call the decorated function
    print("Calling the add function with arguments 2 and 3.")
    add(2, 3)

    print("*" * 80)

# Logger decorator function
def logger(func):
    """
    A decorator function that logs the name, arguments, and result of
    the decorated function.
    """
    def wrapper(*args, **kwargs):
        # Log the function call details
        print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        # Log the result of the function
        print(f"'{func.__name__}' returned {result}")
        return result
    return wrapper

# Decorate the add function with @logger
@logger
def add(x, y):
    """
    Adds two numbers and returns the result.
    """
    return x + y

if __name__ == "__main__":
    main()
