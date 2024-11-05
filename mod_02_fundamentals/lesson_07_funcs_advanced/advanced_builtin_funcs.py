#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: advanced_builtin_utilities
#
# Description: This program demonstrates advanced utility functions in
#              Python, such as `eval()`, `exec()`, `locals()`, `globals()`,
#              and `type()`. These utilities allow dynamic code execution,
#              scope inspection, and type checking.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def demonstrate_eval():
    """
    Demonstrates the use of eval() to evaluate expressions from strings.
    """
    expression = "2 * 3 + 5"
    result = eval(expression)
    print(f"Evaluating '{expression}' gives: {result}")

def demonstrate_exec():
    """
    Demonstrates the use of exec() to execute dynamically generated code.
    """
    code = '''
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
    '''
    print("Executing code:\n", code)
    exec(code)

def demonstrate_locals():
    """
    Demonstrates the use of locals() to inspect local scope variables.
    """
    x = 10
    y = 20
    print("Local variables in this function:", locals())

def demonstrate_globals():
    """
    Demonstrates the use of globals() to inspect global scope variables.
    """
    print("Global variables accessible in this script:", globals())

def demonstrate_type():
    """
    Demonstrates the use of type() to check the types of different objects.
    """
    number = 42
    text = "Hello"
    print(f"The type of {number} is {type(number)}")
    print(f"The type of '{text}' is {type(text)}")

def main():
    print("========== Advanced Built-in Utility Functions in Python ==========")
    demonstrate_eval()
    print("*" * 80)
    demonstrate_exec()
    print("*" * 80)
    demonstrate_locals()
    print("*" * 80)
    demonstrate_globals()
    print("*" * 80)
    demonstrate_type()
    print("*" * 80)

if __name__ == "__main__":
    main()
