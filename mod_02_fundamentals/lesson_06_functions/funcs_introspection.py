#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: function_introspection
#
# Description: This program demonstrates function introspection in Python.
#              It showcases how to retrieve information about function
#              parameters, annotations, default values, and more, using
#              the built-in `inspect` module.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import inspect

def main():
    print("========== Function Introspection in Python ==========")
    print("This program demonstrates how to gather information about functions at runtime.\n")

    # Display introspection details for sample functions
    introspect_function(example_function)
    print("\n" + "=" * 80 + "\n")
    introspect_function(annotated_function)


# Example function with parameters and default values
def example_function(a, b=10, c=5):
    """
    Example function to demonstrate introspection of parameters and default values.

    Args:
        a (int): First parameter, required.
        b (int): Second parameter with a default value.
        c (int): Third parameter with a default value.
    """
    return a + b + c


# Function with type annotations
def annotated_function(x: int, y: int = 2) -> int:
    """
    Adds two numbers, with annotations.

    Args:
        x (int): First number.
        y (int): Second number with a default of 2.

    Returns:
        int: The sum of x and y.
    """
    return x + y


# Function to introspect and display function details
def introspect_function(func):
    """
    Displays introspection details of a given function, including its
    name, parameters, default values, annotations, and documentation.

    Args:
        func (function): The function to introspect.
    """
    print(f"Introspecting function '{func.__name__}':\n")
    print("Signature:", inspect.signature(func))
    print("Documentation:", func.__doc__)
    print("Annotations:", func.__annotations__)

    # Inspect parameters
    parameters = inspect.signature(func).parameters
    print("\nParameters:")
    for param_name, param in parameters.items():
        print(f"  Name: {param_name}")
        print(f"    Kind: {param.kind}")
        print(f"    Default: {param.default if param.default != inspect.Parameter.empty else 'No default'}")
        print(f"    Annotation: {param.annotation if param.annotation != inspect.Parameter.empty else 'No annotation'}")


if __name__ == "__main__":
    main()
