#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Function Parameters and Arguments
#
# Description: Demonstrates the use of positional, keyword, default, and
#              mixed arguments in Python. Each type of argument is shown
#              in individual functions, with a final example that combines
#              them for flexibility.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	print("========== Function Parameters and Arguments ==========")
	print("Examples of positional, keyword, default, and mixed arguments in Python.")
	print("*" * 80)
	
	# Function demonstrating positional arguments
	print("Example with Positional Arguments:")
	func_with_positional("Alice", "Teacher")
	print("*" * 80)
	
	# Function demonstrating keyword arguments
	print("Example with Keyword Arguments:")
	func_with_keyword_args(name="Bob", age=25, role="Engineer")
	print("*" * 80)
	
	# Function demonstrating default arguments
	print("Example with Default Arguments:")
	func_with_default("Carol")  # Uses default title
	func_with_default("Dave", title="Dr.")  # Custom title
	print("*" * 80)
	
	# Mixed examples combining positional, default, and keyword arguments
	print("Comprehensive Mixed Argument Examples:")
	introduce_mixed("John")  # Default title
	introduce_mixed("Alice", title="Dr.")  # Custom title
	describe_person("Emily", 30, profession="Designer", country="USA") # Mixed arguments
	describe_person("Liam", 27)  # Using default values for optional parameters
	
	greet_person("Saad")
	print("*"*80)


# Function demonstrating positional arguments
def func_with_positional(name, role):
	"""
	Function that takes positional arguments.

	Args:
		name (str): The person's name.
		role (str): The person's role.

	Returns:
		None
	"""
	print(f"{name} works as a {role}.")


# Function demonstrating keyword arguments
def func_with_keyword_args(name, age, role):
	"""
	Function that takes keyword arguments.

	Args:
		name (str): The person's name.
		age (int): The person's age.
		role (str): The person's role.

	Returns:
		None
	"""
	print(f"{name} is a {age}-year-old {role}.")


# Function demonstrating default arguments
def func_with_default(name, title="Mr./Ms."):
	"""
	Function that uses default arguments.

	Args:
		name (str): The person's name.
		title (str, optional): The person's title, default is "Mr./Ms.".

	Returns:
		None
	"""
	print(f"{title} {name}")


# Function combining positional, default, and keyword arguments
def introduce_mixed(name, title="Mr."):
	"""
	Introduce a person with a given title and name.

	Args:
		name (str): The person's name.
		title (str, optional): The person's title, default is "Mr.".

	Returns:
		str: The full title and name of the person.
	"""
	print(f"{title} {name}")


# Function demonstrating mixed arguments with more parameters
def describe_person(name, age, profession="Unknown", country="Unknown"):
	"""
	Describe a person with mixed argument types.

	Args:
		name (str): The person's name.
		age (int): The person's age.
		profession (str, optional): The person's profession, default is "Unknown".
		country (str, optional): The person's country, default is "Unknown".

	Returns:
		str: A formatted description of the person.
	"""
	print(f"{name}, aged {age}, is a {profession} from {country}.")
	
	
# Function with a keyword argument for a custom greeting
def greet_person(name, greeting="Hi"):
	"""
    Greet a person with a custom greeting.

    Args:
        name (str): The person's name.
        greeting (str, optional): Custom greeting, default is "Hi".

    Returns:
        str: The full greeting.
    """
	print(f"{greeting}, {name}!")


if __name__ == "__main__":
	main()