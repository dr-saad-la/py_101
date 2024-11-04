#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Variable Scope Shadowing
#
# Description: This program demonstrates variable shadowing and modification
#              of global variables in Python. We show how local variables
#              can shadow global variables and how to modify global variables
#              within a function using the `global` keyword.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

# Global variable
GLOBAL_VAR = 10  # Accessible throughout the script

def main():
    print("========== Variable Shadowing and Global Variable Modification in Python ==========")
    print("This program demonstrates the concept of variable shadowing and modifying global variables.")
    print("*" * 80)

    # Call functions to demonstrate shadowing and modifying global variables
    demonstrate_shadowing_example()
    demonstrate_global_modification_example()
    demonstrate_shadowing_with_direct_global_access()

    print("*" * 80)

# Function demonstrating shadowing with a local variable
def demonstrate_shadowing_example():
    """
    Demonstrates variable shadowing, where a local variable has
    the same name as a global variable but does not affect it.
    """
    GLOBAL_VAR = 5  # Local variable, shadowing the global `GLOBAL_VAR`
    print("\nInside demonstrate_shadowing_example():")
    print(f"Local variable GLOBAL_VAR (shadowing global): {GLOBAL_VAR}")  # Outputs local value, 5

    # Global variable remains unchanged outside this function
    print(f"Accessing the global GLOBAL_VAR outside this function: {globals()['GLOBAL_VAR']}")

# Function demonstrating modifying a global variable using `global`
def demonstrate_global_modification_example():
    """
    Modifies a global variable within a function by declaring it global.
    """
    global GLOBAL_VAR  # Declare that we're referring to the global `GLOBAL_VAR`
    print("\nInside demonstrate_global_modification_example():")
    print(f"Global variable GLOBAL_VAR before modification: {GLOBAL_VAR}")  # Outputs the current global value, 10

    GLOBAL_VAR = 5  # Modify the global variable
    print(f"Global variable GLOBAL_VAR after modification: {GLOBAL_VAR}")  # Outputs modified value, 5

# Function demonstrating shadowing with direct access to the global variable using globals()
def demonstrate_shadowing_with_direct_global_access():
    """
    Shows how to shadow a global variable with a local one while still
    accessing the global version using the globals() dictionary.
    """
    GLOBAL_VAR = 300  # Local variable shadowing the global variable
    print("\nInside demonstrate_shadowing_with_direct_global_access():")
    print(f"Local variable shadowed as GLOBAL_VAR: {GLOBAL_VAR}")  # Prints the shadowed local variable, 300

    # Show that the global variable remains unchanged outside this scope
    print("Global variable (GLOBAL_VAR) outside this function remains unchanged.")
    # Access the actual global variable using globals()
    print(f"Global variable GLOBAL_VAR accessed directly: {globals()['GLOBAL_VAR']}")  # Uses globals() to get the global GLOBAL_VAR

if __name__ == "__main__":
    main()

    # Print final value of GLOBAL_VAR after calling the functions
    print("\nFinal value of global GLOBAL_VAR after all functions:", GLOBAL_VAR)