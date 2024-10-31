#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: String Indexing
#
# Description: Demonstrates string indexing in Python, including basic
#              indexing with positive and negative indices.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Demonstrating String Indexing Techniques ============")
	print_indexing_concepts()
	print("*" * 80)
	
	print("Performing String Indexing Operations".center(80))
	indexing_examples()
	print("*" * 80)


# Function to explain the concept of indexing
def print_indexing_concepts():
	"""
	Print explanations of string indexing techniques.
	"""
	
	print("String Indexing in Python:")
	print("[index] : Accesses a single character at the specified position.")
	print("Negative indices can be used to access characters from the end of the string.")


# Function to demonstrate various string indexing techniques
def indexing_examples():
	text = "Hello, World!"
	
	# Basic Indexing with Positive Indices
	print("\nBasic Indexing with Positive Indices:")
	letter = text[7]  # Accesses 'W'
	print(f"text[7] -> '{letter}'")  # Output: 'W'
	
	# Indexing with Negative Indices
	print("\nIndexing with Negative Indices:")
	negative_index_letter = text[-6]  # Accesses 'W' from the end
	print(f"text[-6] -> '{negative_index_letter}'")  # Output: 'W'
	
	# Accessing the First and Last Characters
	print("\nAccessing First and Last Characters:")
	first_character = text[0]  # Accesses the first character 'H'
	last_character = text[-1]  # Accesses the last character '!'
	print(f"First character: text[0] -> '{first_character}'")  # Output: 'H'
	print(f"Last character: text[-1] -> '{last_character}'")  # Output: '!'


# Out of Range Example (Uncommenting will cause an IndexError)
# print("\nAttempting to access an out-of-range index:")
# print(text[50])  # This would raise an IndexError as the index is out of range


if __name__ == "__main__":
	main()