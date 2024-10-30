#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: string Line Continuation
#
# Description: Demonstrates different techniques for handling long strings
#              and string concatenation across multiple lines in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Demonstrating Different String Continuation Techniques ============")
	print_string_continuation_methods()
	print("*" * 80)
	
	print("Using String Continuation Methods in Python".center(80))
	string_continuation_examples()
	print("*" * 80)


# Function to explain different string continuation methods
def print_string_continuation_methods():
	"""
	Print explanations of different string continuation methods.
	"""
	
	print("String Continuation Methods in Python:")
	print("\\ : Using backslash (\\) for explicit line continuation in strings.")
	print("() : Using parentheses () for implicit continuation when combining multiple strings.")
	print("''' ''' : Using triple quotes for multi-line strings (recommended for readability).")
	print("+ : Breaking up strings across lines using concatenation (+).")
	print("f-strings : Using f-strings for multi-line string interpolation.")


# Function to demonstrate various string continuation techniques
def string_continuation_examples():
	
	# Line Continuation with Backslash
	print("\nExplicit Line Continuation using \\ :")
	long_string_backslash = "This is a very long string that we can continue " \
	                        "onto the next line using a backslash."
	print(f"String using backslash: {long_string_backslash}")
	
	# Line Continuation with Parentheses
	print("\nImplicit Line Continuation using () :")
	long_string_parentheses = (
			"This is a very long string that we can continue "
			"on to the next line by wrapping it in parentheses."
	)
	
	print(f"String using parentheses: {long_string_parentheses}")
	
	# Line Continuation with Triple Quotes (Multi-line String)
	print("\nUsing Triple Quotes (''' ''' or \"\"\" \"\"\") for Multi-line Strings:")
	long_string_triple_quotes = '''This is a very long string that
    spans multiple lines using triple quotes, allowing us to
    keep the format as-is, making it ideal for large blocks of text.'''
	print("String using triple quotes:")
	print(long_string_triple_quotes)
	
	# Line Continuation with String Concatenation
	print("\nLine Continuation with String Concatenation (+) :")
	long_string_concat = ("This is a very long string that we can break up " +
	                      "across multiple lines by using the concatenation " +
	                      "operator (+) for readability."
	                      )
	print(long_string_concat)
	
	# Line Continuation with Multi-line f-strings
	print("\nUsing Multi-line f-strings for String Interpolation:")
	name = "Saad"
	age = 30
	long_string_fstring = (f"My name is {name} and I am {age} years old. "
	                       f"This allows us to interpolate variables within "
	                       f"multi-line strings easily.")
	print(f"String using multi-line f-strings: {long_string_fstring}")


if __name__ == "__main__":
	main()