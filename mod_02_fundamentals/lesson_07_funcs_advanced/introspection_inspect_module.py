#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: introspection_inspect_module
#
# Description: Demonstrates the use of the inspect module for examining
#              function details, including argument names, default values,
#              and annotations. Useful for debugging and dynamic code analysis.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

import inspect

def main():
    print("========== Introspection with the inspect Module ==========")
    print("This program demonstrates how to use the inspect module to examine functions.")
    print("*" * 80)

    # Example functions to examine
    def example_function(param1, param2: int = 10, param3: str = "default") -> str:
        """Example function for introspection."""
        return f"{param1}, {param2}, {param3}"

    # Call function to examine function details
    examine_function(example_function)

    print("*" * 80)

# Function to examine details of a given function using inspect
def examine_function(func):
    """
    Examines the details of a function, including its name, docstring,
    parameters, default values, and annotations.

    Args:
        func (callable): The function to examine.

    Returns:
        None
    """
    print(f"Examining function: {func.__name__}")
    print(f"Docstring: {inspect.getdoc(func)}\n")

    # Retrieve function signature
    signature = inspect.signature(func)
    print("Function Signature:", signature)

    # Iterate over function parameters
    print("\nParameters and Details:")
    for name, param in signature.parameters.items():
        print(f"- Name: {name}")
        print(f"  Kind: {param.kind}")
        print(f"  Default: {param.default if param.default != inspect.Parameter.empty else 'No default'}")
        print(f"  Annotation: {param.annotation if param.annotation != inspect.Parameter.empty else 'No annotation'}")
    print()

    # Show return annotation, if available
    if signature.return_annotation != inspect.Signature.empty:
        print("Return Type:", signature.return_annotation)
    else:
        print("Return Type: No return annotation")

# Another example function to analyze
def compute_area(length: float, width: float = 10.0) -> float:
    """
    Computes the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle. Defaults to 10.0.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

# Additional function call to examine compute_area function
def examine_additional_function():
    """
    Examines the compute_area function using inspect to show how to retrieve
    function annotations, arguments, and default values.
    """
    print("\n--- Examining Additional Function: compute_area ---\n")
    examine_function(compute_area)

if __name__ == "__main__":
    main()
    examine_additional_function()
