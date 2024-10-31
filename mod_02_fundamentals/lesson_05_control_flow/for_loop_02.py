#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: For loops
#
# Description: Demonstrates various uses of loops in Python, including
#              iterating over lists, strings, and real-world applications.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Python Loops Tutorial ============")
	print("Introduction to Loops in Python".center(80))
	print("Loops allow repeating a block of code multiple times,")
	print("either for a set number of iterations or while a condition holds true.")
	print("*" * 80)
	
	loop_through_list()
	print("-" * 80)
	loop_through_string()
	print("-" * 80)
	range_based_loop()
	print("-" * 80)
	customer_email_simulation()
	print("*" * 80)


# Example 1: Looping Through a List
def loop_through_list():
	"""
	Demonstrates a basic for loop iterating over a list of numbers.
	"""
	print("Example 1: Iterating Over a List of Numbers")
	numbers = [1, 2, 3, 4, 5]
	print("Iterating through list of numbers:")
	for num in numbers:
		print(f"Number: {num}")
	print("End of list iteration.\n")


# Example 2: Looping Through a String
def loop_through_string():
	"""
	Demonstrates a for loop iterating over each character in a string.
	"""
	print("Example 2: Iterating Over Each Character in a String")
	text = "Python"
	print(f"String to iterate: '{text}'")
	for char in text:
		print(f"Character: {char}")
	print("End of string iteration.\n")


# Example 3: Looping Using Range
def range_based_loop():
	"""
	Demonstrates using a for loop with a range of numbers.
	"""
	print("Example 3: Iterating Using a Range of Numbers")
	print("Numbers from 1 to 5:")
	for i in range(1, 6):  # Loops from 1 to 5
		print(f"Range number: {i}")
	print("End of range-based loop.\n")


# Real-World Scenario: Sending Emails to a List of Customers
def customer_email_simulation():
	"""
	Simulates sending emails to a list of customers using a for loop.
	"""
	print("Real-World Example: Email Notification to Customers")
	customers = ["Alice", "Bob", "Charlie"]
	for customer in customers:
		print(f"Sending email to {customer}")
	print("All emails sent successfully.\n")


if __name__ == "__main__":
	main()