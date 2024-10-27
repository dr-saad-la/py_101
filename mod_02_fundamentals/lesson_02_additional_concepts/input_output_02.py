#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: input_output_02
#
# Description: Demonstrates input, output, and formatted output in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
def main():
	# Explain print and input functions
	print_input_explanation()
	
	# Demonstrate print function examples
	print_examples()
	
	# Demonstrate input function examples
	input_examples()
	
	# Demonstrate formatted output examples
	formatted_output_examples()
	
# Function to explain basic print and input functions
def print_input_explanation():
	print("Input and Output Functions in Python:")
	print("print() : Outputs data to the standard output (console).")
	print("input() : Reads data from the standard input (user input).")


# Function demonstrating the use of print()
def print_examples():
	print("\nPrint Function Examples:")
	
	# Simple print with a string
	print("Hello, welcome to Python programming!")
	
	# Print with variables
	name = "Alice"
	age = 25
	print("Name:", name, "| Age:", age)
	
	# Print with separator and end parameters
	print("Using separator and end parameters:")
	print("Python", "Programming", "101", sep=" - ", end=".\n")


# Function demonstrating the use of input()
def input_examples():
	print("\nInput Function Examples:")
	
	# Asking for user input
	user_name = input("Enter your name: ")
	print("Hello,", user_name)
	
	# Reading and converting input to an integer
	age = int(input("Enter your age: "))
	print("Your age next year will be:", age + 1)


# Function demonstrating formatted output
def formatted_output_examples():
	print("\nFormatted Output Examples:")
	
	# Using f-strings for formatted output (Python 3.6+)
	name = "Alice"
	age = 25
	height = 1.68
	print(f"My name is {name}, I am {age} years old, and I am {height:.2f} meters tall.")
	
	# Using .format() method for formatting
	print("Hello, my name is {} and I am {} years old.".format(name, age))
	
	# Using formatted strings with specified width and alignment
	print(f"{'Item':<10} {'Price':>8}")
	print(f"{'Apples':<10} ${2.5:>8.2f}")
	print(f"{'Bananas':<10} ${1.75:>8.2f}")
	print(f"{'Cherries':<10} ${5.99:>8.2f}")


if __name__ == "__main__":
	main()