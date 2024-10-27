#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: variable_types
#
# Description:
# **Dynamic Typing**:
#     - Python is dynamically typed, meaning the type of a variable is determined automatically
#      based on the value assigned to it.
#     - The same variable can store different types of data throughout its lifecycle.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	print("Example: Dynamic Typing in Python")
	
	create_vars_dynamic()
	
	print("Example: Type Annotations in Python")
	create_vars_with_type()


def create_vars_dynamic() -> None:
	"""
	Creates and displays different types of variables.
	"""
	# Integer variable
	age = 24
	
	# Floating-point variable
	distance = 52.3
	
	# String variables
	name = "Anas"
	course = "Statistics"
	
	# Boolean variable
	is_valid = True
	
	# Display variable values with formatted output
	print(f"Age: {age} years with type: {type(age)}")
	print(f"Distance: {distance} km  type: {type(distance)}")
	print(f"Name: {name} with type: {type(name)}")
	print(f"Course: {course} with type: {type(course)}")
	print(f"Is the value valid? {'Yes' if is_valid else 'No'}."
	      f"The type is: {type(is_valid)}")


def create_vars_with_type() -> None:
	"""
	Creates and displays different types of variables.
	"""
	# Integer variable
	age: int = 24
	
	# Floating-point variable
	distance: float = 52.3
	
	# String variables
	name: str = "Anas"
	course: str = "Statistics"
	
	# Boolean variable
	is_valid: bool = True
	
	# Display variable values with formatted output
	print(f"Age: {age} years")
	print(f"Distance: {distance} km")
	print(f"Name: {name}")
	print(f"Course: {course}")
	print(f"Is the value valid? {'Yes' if is_valid else 'No'}")


if __name__ == "__main__":
	main()
