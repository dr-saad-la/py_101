#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: higher_order_functions_02
#
# Description: Demonstrates higher-order functions in Python, with each
#              example broken down into its own function. This includes
#              examples of custom higher-order functions as well as using
#              built-in functions like map(), filter(), and reduce().
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

from functools import reduce

def main():
    print("========== Higher-Order Functions in Python ==========")
    print("This lesson demonstrates custom and built-in higher-order functions in Python.")
    print("*" * 80)

    # Call each function demonstrating higher-order functions
    custom_higher_order_function_example()
    map_example()
    filter_example()
    reduce_example()
    real_world_reduce_example()

    print("*" * 80)

    # Built-in higher-order function examples
    print("2. Built-In Higher-Order Functions (map, filter, reduce)")
    built_in_higher_order_functions_example()
    print("*" * 80)


# Custom higher-order function that takes another function as an argument
def custom_higher_order_function_example():
    """
    Demonstrates a custom higher-order function that takes another
    function as an argument and applies it to inputs.
    """
    def apply_operation(func, x, y):
        """
        Applies a given operation (function) to x and y.
        """
        return func(x, y)

    # Using lambda to define a multiplication operation
    result = apply_operation(lambda a, b: a * b, 5, 6)
    print("Custom Higher-Order Function (Multiplication):", result)  # Output: 30

# Example using map() to square each number in a list
def map_example():
    """
    Demonstrates the use of the map() function to apply a transformation
    to each item in a list.
    """
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print("Squared Numbers using map():", squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example using filter() to get even numbers from a list
def filter_example():
    """
    Demonstrates the use of the filter() function to select items from
    a list based on a condition.
    """
    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even Numbers using filter():", even_numbers)  # Output: [2, 4]

# Example using reduce() to calculate the product of a list of numbers
def reduce_example():
    """
    Demonstrates the use of the reduce() function to accumulate a result
    from all items in a list.
    """
    numbers = [1, 2, 3, 4, 5]
    product_of_numbers = reduce(lambda x, y: x * y, numbers)
    print("Product of Numbers using reduce():", product_of_numbers)  # Output: 120

# Real-world example: Concatenating a list of strings using reduce()
def real_world_reduce_example():
    """
    Real-world example using reduce() to concatenate a list of words
    into a single sentence.
    """
    words = ["Higher-order", "functions", "are", "powerful"]
    concatenated_sentence = reduce(lambda a, b: a + " " + b, words)
    print("Concatenated Sentence using reduce():", concatenated_sentence)


# Built-in higher-order function examples: map, filter, reduce
def built_in_higher_order_functions_example():
    """
    Demonstrates the use of built-in higher-order functions map, filter, and reduce.
    """
    # Example using map() to square each number in a list
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print("Squared numbers using map():", squared_numbers)  # Output: [1, 4, 9, 16, 25]

    # Example using filter() to get even numbers from a list
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers using filter():", even_numbers)  # Output: [2, 4]

    # Example using reduce() to calculate the product of a list of numbers
    product_of_numbers = reduce(lambda x, y: x * y, numbers)
    print("Product of numbers using reduce():", product_of_numbers)  # Output: 120

    # Real-world example: Concatenating a list of strings using reduce()
    words = ["Higher-order", "functions", "are", "powerful"]
    concatenated_sentence = reduce(lambda a, b: a + " " + b, words)
    print("Concatenated sentence using reduce():", concatenated_sentence)



if __name__ == "__main__":
    main()
