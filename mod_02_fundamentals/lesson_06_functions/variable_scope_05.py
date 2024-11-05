#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: variable_scope_01
#
# Description: Demonstrates variable scope in Python, explaining the concepts
#              of local and global variables. This includes examples of accessing
#              and modifying global variables from within functions and
#              the scope limitations of local variables.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

# Global variable
global_var = 100  # Accessible throughout the entire script

def main():
    print("========== Variable Scope in Python ==========")
    print("In this lesson, we explore how Python handles local and global variables.")
    print("*" * 60)
    
    # Call functions demonstrating local and global scope
    demonstrate_local_scope()
    demonstrate_global_scope()
    demonstrate_global_modification()
    
    print("*" * 60)

# Function demonstrating local scope
def demonstrate_local_scope():
    """
    Demonstrates the concept of local scope, where variables
    are only accessible within the function they are defined in.
    """
    local_var = 50  # Local variable; accessible only within this function
    print("Inside demonstrate_local_scope():")
    print(f"Local variable (local_var): {local_var}")
    print(f"Global variable (global_var) accessible here: {global_var}")
    
    # Trying to return a modified version of the global variable as a local one
    modified_global_as_local = global_var + 10
    print(f"Modified global_var as local (modified_global_as_local): {modified_global_as_local}")

# Function demonstrating global scope
def demonstrate_global_scope():
    """
    Shows that a global variable can be accessed within a function,
    and demonstrates what happens when you try to reassign it without
    declaring it global.
    """
    global global_var  # Now referring to the global `global_var`
    print("\nInside demonstrate_global_scope():")
    print(f"Global variable (global_var) before reassignment: {global_var}")
    
    # Modify the global variable
    global_var = 200  # Modify the actual global variable
    print(f"Global variable (global_var) after reassignment: {global_var}")

# Function modifying a global variable using the `global` keyword
def demonstrate_global_modification():
    """
    Uses the `global` keyword to modify the global variable `global_var`
    from within the function.
    """
    global global_var  # Declaring that we intend to modify the global variable
    print("\nInside demonstrate_global_modification():")
    print(f"Original global variable (global_var): {global_var}")
    
    global_var += 10  # Modifies the global variable
    print(f"Modified global variable (global_var): {global_var}")

if __name__ == "__main__":
    main()
