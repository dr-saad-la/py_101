#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Multiline Strings
#
# Description: Demonstrates multiline strings in Python, including
#              creating and manipulating long text using triple quotes.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Demonstrating Multiline Strings ============")
	print_multiline_string_concepts()
	print("*" * 80)
	
	print("Using Multiline Strings in Python".center(80))
	multiline_string_examples()
	print("*" * 80)


# Function to explain multiline strings
def print_multiline_string_concepts():
	"""
	Print explanations of multiline strings.
	"""
	
	print("Multiline Strings in Python:")
	print("Triple quotes (''' or \"\"\") allow creating strings that span multiple lines.")
	print("Useful for paragraphs, documentation, or large blocks of text.")


# Function to demonstrate various uses of multiline strings
def multiline_string_examples():
	
	# Basic Multiline String Example
	print("\nCreating and Printing a Multiline String:")
	long_text = """This is a long string
    that spans multiple lines.
    You can write paragraphs of text
    using triple quotes."""
	print("Multiline text using triple quotes:")
	print(long_text)  # Prints the long text across multiple lines
	
	# Real-world String Manipulation Example
	print("\nReal-world Example of String Manipulation:")
	user_input = "  Hello, Python World!  "
	
	# Step 1: Strip whitespace
	cleaned_input = user_input.strip()
	print(f"Cleaned input: '{cleaned_input}'")
	
	# Step 2: Convert to lowercase
	lowercase_input = cleaned_input.lower()
	print(f"Lowercase: {lowercase_input}")
	
	# Step 3: Extract a specific part of the string ('python')
	extracted_word = lowercase_input[7:13]
	print(f"Extracted word: {extracted_word}")
	
	# Step 4: Replace 'python' with 'programming'
	replaced_input = lowercase_input.replace('python', 'programming')
	print(f"Replaced text: {replaced_input}")


if __name__ == "__main__":
	main()