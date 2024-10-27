#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: type_conversion_01
#
# Description: Demonstrates type conversion in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
def main():
	# Print type conversion functions and their descriptions
	print_type_conversions()
	# Call type conversion examples function
	type_conversion_examples()
	
# Function to print type conversion functions and their descriptions
def print_type_conversions():
	print("Type Conversion Functions in Python:")
	print("int()   : Converts a value to an integer.")
	print("float() : Converts a value to a float.")
	print("str()   : Converts a value to a string.")
	print("list()  : Converts a sequence to a list.")
	print("tuple() : Converts a sequence to a tuple.")
	print("set()   : Converts a sequence to a set.")


# Function to demonstrate type conversion examples
def type_conversion_examples():
	print("\nType Conversion Examples:")
	
	# Integer to float conversion
	integer_value = 10
	float_value = float(integer_value)
	print(f"float({integer_value}) -> {float_value}")  # 10.0
	
	# Float to integer conversion
	float_value = 7.9
	int_value = int(float_value)
	print(f"int({float_value}) -> {int_value}")  # 7
	
	# Integer to string conversion
	str_value = str(integer_value)
	print(f"str({integer_value}) -> '{str_value}'")  # '10'
	
	# String to integer conversion
	string_number = "42"
	int_value_from_str = int(string_number)
	print(f"int('{string_number}') -> {int_value_from_str}")  # 42
	
	# List to set conversion
	list_value = [1, 2, 3, 3, 4]
	set_value = set(list_value)
	print(f"set({list_value}) -> {set_value}")  # {1, 2, 3, 4}
	
	# List to tuple conversion
	tuple_value = tuple(list_value)
	print(f"tuple({list_value}) -> {tuple_value}")  # (1, 2, 3, 3, 4)

if __name__ == "__main__":
	main()