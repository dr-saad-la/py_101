#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Control Flow
#
# Description: Demonstrates control flow statements in Python,
#              The if statement, if-else and if-elif-else statements
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Demonstrating Control Flow Statements ============")
	print("Overview of Control Flow in Python".center(80))
	print("Control flow allows decision-making in programs using conditional statements.")
	print("1. Using ```if``` statement to evaluate a single condition.")
	print("2. Using ```if-else``` statement for two conditional outcomes.")
	print("3. Using ```if-elif-else``` statement for multiple conditions.")
	print("*" * 80)
	
	basic_if_statement()
	print("-" * 80)
	basic_if_else_statement()
	print("-" * 80)
	basic_if_elif_else_statement()
	print("-" * 80)
	check_user_eligibility()
	print("*" * 80)


# Function to illustrate an if statement
def basic_if_statement():
	"""
	Illustrates a basic if statement.
	"""
	print("Example: Using an if statement")
	age = 20
	if age >= 18:
		print("Access granted. You are an adult.")  # Only executes if age >= 18


# Function to illustrate an if-else statement
def basic_if_else_statement():
	"""
	Illustrates an if-else statement.
	"""
	print("Example: Using an if-else statement")
	age = 16
	if age >= 18:
		print("Access granted. You are an adult.")
	else:
		print("Access denied. You are a minor.")  # Executes if age < 18


# Function to illustrate an if-elif-else statement
def basic_if_elif_else_statement():
	"""
	Illustrates an if-elif-else statement.
	"""
	print("Example: Using an if-elif-else statement")
	age = 18
	if age < 18:
		print("You are a minor.")
	elif age == 18:
		print("You just became an adult!")
	else:
		print("You are an adult.")


# Real-world scenario function: User eligibility based on age
def check_user_eligibility():
	"""
	Determines eligibility for different user plans based on age.
	"""
	print("Real-World Scenario: Eligibility Check for Service Plans")
	age = int(input("Enter your age: "))
	
	if age < 13:
		print("You are eligible for the children's plan.")
	elif 13 <= age < 18:
		print("You are eligible for the teen plan.")
	else:
		print("You are eligible for the adult plan.")


if __name__ == "__main__":
	main()