#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: while_loops_01
#
# Description: Comprehensive guide on using the while loop in Python.
#              This program demonstrates basic while loops, real-world
#              scenarios, and advanced concepts using break and continue.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	print("============ Python While Loops Tutorial ============")
	print("Exploring While Loops in Python".center(80))
	print("The while loop repeats a block of code as long as a condition is True.")
	print("It's particularly useful when the number of iterations is unknown.")
	print("*" * 80)
	
	basic_while_loop()
	print("-" * 80)
	user_input_password_check()
	print("-" * 80)

# Example 1: Basic While Loop
def basic_while_loop():
	"""
	Demonstrates a basic while loop that increments a counter.
	"""
	print("Example 1: Basic While Loop (Counting to 5)")
	count = 0
	while count < 5:
		print(f"Count is: {count}")
		count += 1
	print("Basic while loop completed.\n")


# Example 2: Real-World Scenario - Password Check
def user_input_password_check():
	"""
	A real-world example using a while loop to validate user input for a password.
	"""
	print("Example 2: Real-World Password Check Using a While Loop")
	correct_password = "secret123"
	password = ""
	
	# Continuously prompt the user until the correct password is entered
	while password != correct_password:
		password = input("Enter the password: ")
	
	print("Access granted!\n")

if __name__ == "__main__":
	main()