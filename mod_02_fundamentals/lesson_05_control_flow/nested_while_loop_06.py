#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Nested While Loops
#
# Description: Demonstrates the use of nested while loops in Python by
#              creating a customizable multiplication table. This program
#              is designed to show how to implement multi-dimensional looping
#              logic with nested while loops, with user input validation.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	print("============ Nested While Loops Tutorial ============")
	print("Nested while loops allow looping over multi-dimensional data structures.")
	print("In this example, we create a customizable multiplication table.")
	print("*" * 80)
	
	# Requesting table size from the user
	table_size = get_table_size()
	
	# Generate and display the multiplication table
	generate_multiplication_table(table_size)
	print("*" * 80)
	print(f"Multiplication table of size {table_size}x{table_size} generated successfully.")


# Function to prompt user for table size with validation
def get_table_size():
	"""
	Prompts the user to enter a positive integer for the multiplication table size.
	"""
	while True:
		try:
			size = int(input("Enter the size of the multiplication table (positive integer): "))
			if size > 0:
				return size
			else:
				print("Please enter a positive integer.")
		except ValueError:
			print("Invalid input. Please enter a valid integer.")


# Function to generate a multiplication table using nested while loops
def generate_multiplication_table(size):
	"""
	Generates a size x size multiplication table using nested while loops.

	Args:
		size (int): The size of the multiplication table.
	"""
	print(f"{size}x{size} Multiplication Table:")
	row = 1
	while row <= size:
		col = 1
		while col <= size:
			print(f"{row * col:3}", end=" ")  # :3 ensures three-character width for alignment
			col += 1
		print()  # Newline after each row
		row += 1
	print("Multiplication table generation completed.\n")


if __name__ == "__main__":
	main()