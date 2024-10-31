#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: String Slicing
#
# Description: Demonstrates string slicing in Python, including basic
#              slicing with positive and negative indices.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Demonstrating String Slicing Techniques ============")
	print_slicing_concepts()
	print("*" * 80)
	
	print("Performing String Slicing Operations".center(80))
	slicing_examples()
	print("*" * 80)


# Function to explain the concept of slicing
def print_slicing_concepts():
	"""
	Print explanations of string slicing techniques.
	"""
	
	print("String Slicing in Python:")
	print("[start:end] : Extracts substring from start index up to, but not including, end index.")
	print("[start:end:step] : Allows slicing with a step value to skip characters.")
	print("Negative indices can be used to count from the end of the string.")


# Function to demonstrate various string slicing techniques
def slicing_demo():
	text = "Hello, World!"
	
	# Basic Slicing with Start and End
	print("\nBasic Slicing with [start:end]:")
	sliced_text = text[0:5]                      # Extracts 'Hello'
	print(f"text[0:5] -> '{sliced_text}'")
	
	# Slicing with Negative Indices
	print("\nSlicing with Negative Indices:")
	negative_slice = text[-6:]                 # Extracts 'World!'
	print(f"text[-6:] -> '{negative_slice}'")
	
	# Slicing with Step
	print("\nSlicing with Step [start:end:step]:")
	step_slice = text[::2]               # Extracts every second character
	print(f"text[::2] -> '{step_slice}'")
	
	# Reversing a String Using Slicing
	print("\nReversing a String with Slicing:")
	reversed_text = text[::-1]  # Reverses the entire string
	print(f"text[::-1] -> '{reversed_text}'")  # Output: '!dlroW ,olleH'

# utility functions
def show_indexing(text: str)-> None:
	for idx, elem in enumerate(text):
		print(f"Character: {elem}, has Index: {idx}")

def show_negative_indexing(text: str)->None:
	for idx, char in enumerate(text):
		neg_idx = idx - len(text)
		print(f"Character: {char}, Positive Index: {idx}, Negative Index: {neg_idx}")


if __name__ == "__main__":
	main()