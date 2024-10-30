#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: string Concatenation
#
# Description: Demonstrates string concatenation in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Demonstrating String Concatenation ============")
	print_concatenation_operators()
	print("*" * 72)
	
	print("Perform String Concatenation Operations".center(72))
	string_concat()
	print("*" * 72)


# Function to explain string concatenation
def print_concatenation_operators():
	"""
	Print explanation of the string concatenation operator.
	"""
	
	print("String Concatenation in Python:")
	print("+ : Concatenation (joins two or more strings together)")


# Function to demonstrate string concatenation
def string_concat():
	"""
	Demonstrate how string concatenation works.
	"""
	first_name = "Saad"
	last_name = "Laouadi"
	title = "Dr."
	full_name = title + " " + first_name + " " + last_name
	print("\nString Concatenation Example:")
	print(f"First Name: {first_name}")
	print(f"Last Name: {last_name}")
	print(f"Full Name: {full_name}")


if __name__ == "__main__":
	main()


