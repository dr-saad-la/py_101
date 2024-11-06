#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: builtin_function_utilities
#
# Description: This program demonstrates the use of built-in function
#              utilities in Python, such as `dir()`, `help()`, `callable()`,
#              `vars()`, `type()`, `isinstance()`, `getattr()`, `setattr()`,
#              and `hasattr()`. These functions provide introspection
#              capabilities and are useful for debugging and understanding
#              code dynamically.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Built-in Function Utilities in Python ==========")
    demonstrate_dir()
    demonstrate_help()
    demonstrate_callable()
    demonstrate_vars()
    demonstrate_type_isinstance()
    demonstrate_getattr_setattr_hasattr()

# Demonstrates the `dir()` function
def demonstrate_dir():
    class SampleClass:
        def __init__(self):
            self.value = 42
        def method(self):
            pass

    obj = SampleClass()
    print("\nUsing dir() to list attributes and methods of SampleClass:")
    print(dir(obj))  # Outputs a list of attributes and methods

# Demonstrates the `help()` function
def demonstrate_help():
    def sample_function(x, y):
        """This function adds two numbers."""
        return x + y

    print("\nUsing help() to display documentation of sample_function:")
    help(sample_function)  # Outputs the docstring and parameters of the function

# Demonstrates the `callable()` function
def demonstrate_callable():
    def sample_function():
        pass

    print("\nUsing callable() to check if an object is callable:")
    print(callable(sample_function))  # True, as it is a function
    print(callable(42))               # False, as an integer is not callable

# Demonstrates the `vars()` function
def demonstrate_vars():
    class SampleClass:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    obj = SampleClass(5, 10)
    print("\nUsing vars() to access the attribute dictionary of SampleClass:")
    print(vars(obj))  # Outputs {'a': 5, 'b': 10}

# Demonstrates the `type()` and `isinstance()` functions
def demonstrate_type_isinstance():
    num = 42
    print("\nUsing type() and isinstance() for type checks:")
    print(f"Type of num: {type(num)}")  # <class 'int'>
    print(f"Is num an instance of int? {isinstance(num, int)}")  # True

# Demonstrates the `getattr()`, `setattr()`, and `hasattr()` functions
def demonstrate_getattr_setattr_hasattr():
    class SampleClass:
        def __init__(self, value=0):
            self.value = value

    obj = SampleClass()
    print("\nUsing getattr(), setattr(), and hasattr() on SampleClass:")
    print(f"Initial value of 'value' attribute: {getattr(obj, 'value')}")  # Outputs 0

    setattr(obj, 'value', 100)
    print(f"Updated value of 'value' attribute: {obj.value}")  # Outputs 100

    print(f"Does 'value' attribute exist? {hasattr(obj, 'value')}")  # True

if __name__ == "__main__":
    main()
