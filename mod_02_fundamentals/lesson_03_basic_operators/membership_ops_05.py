#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: membership_ops_05
#
# Description: Demonstrates membership operators and combining multiple operators in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
def main():
	print_membership_operators()
	membership_ops()
	combined_ops_example()
	
	
# Function to print membership operators and their descriptions
def print_membership_operators():
	print("Membership Operators in Python:")
	print("in      : Returns True if a value is found in the sequence")
	print("not in  : Returns True if a value is not found in the sequence")


# Function to demonstrate membership operations
def membership_ops():
	my_list = [1, 2, 3, 4, 5]
	print("\nMembership Operations Examples:")
	print(f"3 in my_list -> {3 in my_list}")  # True
	print(f"6 not in my_list -> {6 not in my_list}")  # True


# Function to demonstrate combining multiple operators
def combined_ops_example():
	x = 10
	y = 20
	z = 5
	print("\nCombining Multiple Operators Example:")
	
	# Example of combining arithmetic, comparison, and logical operators
	result = (x + y > z) and (y % z == 0)
	print(f"(x + y > z) and (y % z == 0) -> {result}")  # True


if __name__ == "__main__":
	main()