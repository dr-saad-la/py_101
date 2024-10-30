#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: line Continuation
#
# Description: Demonstrates line continuation techniques in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Demonstrating Different Line Continuation Techniques ============")
	print_line_continuation_methods()
	print("*" * 80)
	
	print("Using Line Continuation Methods in Python".center(80))
	line_continuation_examples()
	print("*" * 80)


# Function to explain different line continuation methods
def print_line_continuation_methods():
	"""
	Print explanations of different line continuation methods.
	"""
	
	print("Line Continuation Methods in Python:")
	print("\\ : Using backslash (\\) for explicit line continuation.")
	print("() : Using parentheses () to break up code across lines (implicit).")
	print("[] : Using square brackets [] for lists (implicit line continuation).")
	print("{} : Using curly braces {} for dictionaries or sets (implicit line continuation).")
	print("+ : Breaking up strings across lines using concatenation (+).")


# Function to demonstrate various line continuation techniques
def line_continuation_examples():
	
	# Line Continuation with Backslash
	print("\nExplicit Line Continuation using \\ :")
	total_sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15
	print(f"Sum using backslash: {total_sum}")
	
	# Line Continuation with Parentheses
	print("\nImplicit Line Continuation using () :")
	total_sum_parentheses = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15)
	print(f"Sum using parentheses: {total_sum_parentheses}")
	
	# Line Continuation with List and Square Brackets
	print("\nImplicit Line Continuation using [] :")
	numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print(f"List of numbers: {numbers_list}")
	
	# Line Continuation with Dictionary and Curly Braces
	print("\nImplicit Line Continuation using {} :")
	example_dict = {
			"one": 1, "two": 2, "three": 3, "four": 4
			}
	print(f"Dictionary of numbers: {example_dict}")
	
	# Line Continuation with String Concatenation
	print("\nLine Continuation with String Concatenation (+) :")
	long_string = "This is a very long string that we can break up " + "across multiple lines by using the concatenation " + "operator (+) for readability."
	print(long_string)


if __name__ == "__main__":
	main()