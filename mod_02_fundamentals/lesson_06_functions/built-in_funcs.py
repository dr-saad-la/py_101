#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: built_in_functions_02
#
# Description: This program demonstrates a wide range of useful built-in
#              functions in Python, including len(), enumerate(), map(),
#              filter(), reversed(), and type(), among others.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Expanded Demonstration of Built-in Functions in Python ==========")
    check_all()
    check_any()
    calculate_sum()
    find_max_and_min()
    sort_items()
    zip_example()
    check_length()
    enumerate_example()
    map_example()
    filter_example()
    reversed_example()
    type_example()
    absolute_value_example()
    rounding_example()
    instance_check_example()
    any_with_mixed_data_example()
    all_with_strings_example()
    max_with_key_example()
    custom_sorting_example()
    print("===========================================================================")

# Function demonstrating `all()` usage
def check_all():
    numbers = [2, 4, 6, 8, 10]
    result = all(num % 2 == 0 for num in numbers)
    print("\nUsing `all()` - Are all numbers even?", result)  # Output: True


# Function demonstrating `any()` usage
def check_any():
    numbers = [1, 3, 5, 8, 11]
    result = any(num % 2 == 0 for num in numbers)
    print("\nUsing `any()` - Is there any even number?", result)  # Output: True


# Function demonstrating `sum()` usage
def calculate_sum():
    expenses = [200, 150, 300, 50]
    total = sum(expenses)
    print("\nUsing `sum()` - Total expenses:", total)  # Output: 700


# Function demonstrating `max()` and `min()` usage
def find_max_and_min():
    scores = [82, 91, 78, 99, 88]
    highest = max(scores)
    lowest = min(scores)
    print("\nUsing `max()` - Highest score:", highest)  # Output: 99
    print("Using `min()` - Lowest score:", lowest)  # Output: 78


# Function demonstrating `sorted()` usage
def sort_items():
    names = ["Charlie", "Alice", "Eve", "Bob"]
    sorted_names = sorted(names)
    sorted_names_reverse = sorted(names, reverse=True)
    print("\nUsing `sorted()` - Names in ascending order:", sorted_names)
    print("Using `sorted()` with reverse=True - Names in descending order:", sorted_names_reverse)


# Function demonstrating `zip()` usage
def zip_example():
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 90, 78]
    combined = list(zip(names, scores))
    print("\nUsing `zip()` - Combined names and scores:", combined)


# Function demonstrating `len()` usage
def check_length():
    items = ["apple", "banana", "cherry"]
    length = len(items)
    print("\nUsing `len()` - Number of items:", length)  # Output: 3


# Function demonstrating `enumerate()` usage
def enumerate_example():
    items = ["apple", "banana", "cherry"]
    print("\nUsing `enumerate()` - Indexed items:")
    for index, item in enumerate(items):
        print(f"Index {index}: {item}")


# Function demonstrating `map()` usage
def map_example():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print("\nUsing `map()` - Squared numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]


# Function demonstrating `filter()` usage
def filter_example():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("\nUsing `filter()` - Even numbers:", even_numbers)  # Output: [2, 4, 6, 8]


# Function demonstrating `reversed()` usage
def reversed_example():
    items = ["apple", "banana", "cherry"]
    reversed_items = list(reversed(items))
    print("\nUsing `reversed()` - Items in reverse order:", reversed_items)  # Output: ['cherry', 'banana', 'apple']


# Function demonstrating `type()` usage
def type_example():
    variable = 10.5
    variable_type = type(variable)
    print("\nUsing `type()` - Type of variable:", variable_type)  # Output: <class 'float'>

# Function demonstrating `abs()` usage
def absolute_value_example():
    number = -10
    absolute_value = abs(number)
    print("\nUsing `abs()` - Absolute value of -10:", absolute_value)  # Output: 10


# Function demonstrating `round()` usage
def rounding_example():
    value = 3.14159
    rounded_value = round(value, 2)
    print("\nUsing `round()` - Rounded value of 3.14159 to 2 decimal places:", rounded_value)  # Output: 3.14


# Function demonstrating `isinstance()` usage
def instance_check_example():
    number = 5
    is_integer = isinstance(number, int)
    print("\nUsing `isinstance()` - Is 5 an integer?", is_integer)  # Output: True


# Function demonstrating `any()` with mixed data types
def any_with_mixed_data_example():
    items = [0, "", None, True, False]
    has_true_value = any(items)
    print("\nUsing `any()` with mixed data types - Any truthy value?", has_true_value)  # Output: True


# Function demonstrating `all()` with strings
def all_with_strings_example():
    words = ["apple", "banana", "cherry"]
    all_non_empty = all(words)
    print("\nUsing `all()` with strings - All non-empty strings?", all_non_empty)  # Output: True


# Function demonstrating `max()` with key argument
def max_with_key_example():
    fruits = ["apple", "banana", "cherry", "blueberry"]
    longest_fruit = max(fruits, key=len)
    print("\nUsing `max()` with `key` - Longest fruit name:", longest_fruit)  # Output: blueberry


# Function demonstrating `sorted()` with custom sorting using key argument
def custom_sorting_example():
    fruits = ["apple", "banana", "cherry", "blueberry"]
    sorted_by_length = sorted(fruits, key=len)
    print("\nUsing `sorted()` with `key` - Fruits sorted by length:", sorted_by_length)  # Output: ['apple', 'banana', 'cherry', 'blueberry']


if __name__ == "__main__":
    main()
