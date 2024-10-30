#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: String Concatenation Advanced
#
# Description: Demonstrates multiple techniques for string concatenation in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Demonstrating Multiple String Concatenation Techniques ============")
	print_concatenation_techniques()
	print("*" * 80)
	
	print("Performing Various String Concatenation Operations".center(80))
	string_concat()
	print("*" * 80)


# Function to explain different string concatenation techniques
def print_concatenation_techniques():
	"""
	Print explanation of different string concatenation techniques.
	"""
	
	print("String Concatenation Techniques in Python:")
	print("+ : Concatenation using + operator (joins two or more strings)")
	print("join() : Concatenation using the join() method (efficient for multiple strings)")
	print("f-string : Concatenation using f-strings (format strings for easy readability)")
	print("format() : Concatenation using the format() method (alternative for formatting)")


# Function to demonstrate various string concatenation techniques
def string_concat():
	first_name = "Saad"
	last_name = "Laouadi"
	
	# Concatenation using +
	full_name_plus = first_name + " " + last_name
	print("\nConcatenation using + operator:")
	print(f"Full Name: {full_name_plus}")
	
	# Concatenation using join()
	full_name_join = " ".join([first_name, last_name])
	print("\nConcatenation using join() method:")
	print(f"Full Name: {full_name_join}")
	
	# Concatenation using f-strings
	full_name_fstring = f"{first_name} {last_name}"
	print("\nConcatenation using f-strings:")
	print(f"Full Name: {full_name_fstring}")
	
	# Concatenation using format()
	full_name_format = "{} {}".format(first_name, last_name)
	print("\nConcatenation using format() method:")
	print(f"Full Name: {full_name_format}")


if __name__ == "__main__":
	main()