#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Essential String Methods
#
# Description: Demonstrates common string manipulation methods in Python,
#              including upper(), lower(), strip(), replace(), split(),
#              and join().
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Demonstrating Common String Methods ============")
	print_string_method_concepts()
	print("*" * 80)
	
	print("Using String Methods in Python".center(80))
	string_method_examples()
	print("*" * 80)


# Function to explain common string methods
def print_string_method_concepts():
	"""
	Print explanations of common string manipulation methods.
	"""
	
	print("Common String Methods in Python:")
	print("upper() : Converts the entire string to uppercase.")
	print("lower() : Converts the entire string to lowercase.")
	print("strip() : Removes leading and trailing spaces (or specified characters).")
	print("replace() : Replaces all occurrences of a substring with another substring.")
	print("split() : Splits a string into a list based on a delimiter.")
	print("join() : Joins elements of a list into a string with a specified separator.")


# Function to demonstrate various string methods
def string_method_examples():
	message = "Hello, World!"
	
	# Convert to uppercase
	print("\nUsing upper() to Convert to Uppercase:")
	print(f"Original message: '{message}'")
	print(f"Uppercase: '{message.upper()}'")  # Output: 'HELLO, WORLD!'
	
	# Convert to lowercase
	print("\nUsing lower() to Convert to Lowercase:")
	print(f"Lowercase: '{message.lower()}'")  # Output: 'hello, world!'
	
	# Strip whitespace
	padded_string = "   Hello   "
	print("\nUsing strip() to Remove Leading and Trailing Whitespace:")
	print(f"Padded string: '{padded_string}'")
	print(f"Stripped: '{padded_string.strip()}'")  # Output: 'Hello'
	
	# Replace characters
	sentence = "I love apples."
	print("\nUsing replace() to Replace Substrings:")
	new_sentence = sentence.replace("apples", "bananas")
	print(f"Original sentence: '{sentence}'")
	print(f"Modified sentence: '{new_sentence}'")  # Output: 'I love bananas.'
	
	# Split into a list
	phrase = "Python is fun"
	print("\nUsing split() to Split a String into a List:")
	words = phrase.split()  # Splits by spaces by default
	print(f"Original phrase: '{phrase}'")
	print(f"List of words: {words}")  # Output: ['Python', 'is', 'fun']
	
	# Join a list into a string
	words_list = ["Python", "is", "fun"]
	print("\nUsing join() to Join a List into a String:")
	joined_sentence = " ".join(words_list)
	print(f"List of words: {words_list}")
	print(f"Joined sentence: '{joined_sentence}'")  # Output: 'Python is fun'


if __name__ == "__main__":
	main()