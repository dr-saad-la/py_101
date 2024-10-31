#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: escape_characters_01
#
# Description: Demonstrates escape characters in Python, including
#              newlines, tabs, and backslashes.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Demonstrating Escape Characters ============")
	print_escape_character_concepts()
	print("*" * 80)
	
	print("Using Escape Characters in Python".center(80))
	escape_character_examples()
	print("*" * 80)


# Function to explain escape characters
def print_escape_character_concepts():
	"""
	Print explanations of escape characters.
	"""
	
	print("Escape Characters in Python:")
	print("\\n : Newline (moves the cursor to the next line)")
	print("\\t : Tab (inserts a tab space)")
	print("\\\\ : Backslash (allows inclusion of a literal backslash)")

# Function to demonstrate various escape characters
def escape_character_examples():
	
	# Newline Example
	print("\nUsing \\n for Newlines:")
	multiline_text = "Line 1\nLine 2\nLine 3"
	print("Multiline text using \\n:")
	print(multiline_text)  # Output:

	# Tab Example
	print("\nUsing \\t for Tabs:")
	print("Item\tPrice")
	print("Apple\t$1.00")
	print("Banana\t$0.50")
	
	# Backslash Example
	print("\nUsing \\\\ to Print a Literal Backslash:")
	backslash_example = "This is a backslash: \\"
	print(backslash_example)  # Output: This is a backslash: \


if __name__ == "__main__":
	main()