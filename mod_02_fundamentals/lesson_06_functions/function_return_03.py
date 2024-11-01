#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: return_values_04
#
# Description: Demonstrates the use of return values in Python functions.
#              Shows how functions can return values for computations or
#              return specific data types like strings or None if not specified.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	print("=========== Return Values in Python Functions ===========")
	print("Functions can return values back to the caller using the 'return' statement.")
	print("*" * 80)
	
	# Demonstrating a basic function with return value
	print("Example 1: Returning a Value from a Function")
	result = add_numbers(5, 3)
	print(f"5 + 3 = {result}")  # Output: 8
	print("*" * 80)
	
	# Demonstrating a function that returns a specific part of data
	print("Example 2: Returning Part of a Name from a Function")
	first_name = get_first_name("Alice Johnson")
	print(f"First name extracted: {first_name}")  # Output: Alice
	print("*" * 80)
	
	# Advanced example: Returning multiple values as a tuple
	print("Example 3: Returning Multiple Values from a Function")
	square, cube = calculate_powers(4)
	print(f"Square of 4: {square}, Cube of 4: {cube}")
	print("*" * 80)
	
	# Example with no explicit return value (returns None by default)
	print("Example 4: Function with No Return Value")
	message = greet("Dr. Saad")
	print(f"Returned value: {message}")  # Output: None
	print("*" * 80)


# Function returning the sum of two numbers
def add_numbers(a, b):
	"""
	Adds two numbers and returns the result.

	Args:
		a (int or float): The first number.
		b (int or float): The second number.

	Returns:
		int or float: The sum of a and b.
	"""
	return a + b


# Function that extracts and returns the first name from a full name
def get_first_name(full_name):
	"""
	Returns the first name from a full name.

	Args:
		full_name (str): The person's full name.

	Returns:
		str or None: The first name if available, otherwise None.
	"""
	parts = full_name.split()
	return parts[0] if len(parts) > 0 else None


# Function returning multiple values (square and cube of a number)
def calculate_powers(number):
	"""
	Calculates and returns the square and cube of a number.

	Args:
		number (int): The number to calculate.

	Returns:
		tuple: A tuple containing the square and cube of the number.
	"""
	square = number ** 2
	cube = number ** 3
	return square, cube


# Function without an explicit return value (returns None by default)
def greet(name):
	"""
	Greets the person by printing a message.

	Args:
		name (str): The person's name.

	Returns:
		None
	"""
	print(f"Hello, {name}!")


if __name__ == "__main__":
	main()