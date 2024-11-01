#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Function Arguments Advanced
#
# Description: Demonstrates advanced function arguments in Python, including
#              positional-only, arbitrary, keyword-only, and combinations of
#              these types in a single function.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	print("=========== Advanced Function Arguments in Python ===========")
	print("In this lesson, we explore advanced options for function arguments.")
	print("*" * 80)
	
	# Positional-only arguments
	print("Example 1: Positional-Only Arguments")
	print(positional_only(10, 20))  # Valid usage
	print("*" * 80)
	
	# Arbitrary arguments with *args
	print("Example 2: Arbitrary Arguments (*args)")
	arbitrary_args(1, 2, 3, 4, 5)
	print("*" * 80)
	
	# Keyword-only arguments
	print("Example 3: Keyword-Only Arguments")
	keyword_only(1, 2, keyword_arg="Must be keyword")
	print("*" * 80)
	
	# Arbitrary keyword arguments with **kwargs
	print("Example 4: Arbitrary Keyword Arguments (**kwargs)")
	arbitrary_keyword_args(name="Alice", age=30, location="Paris")
	print("*" * 80)
	
	# Mixing all types of arguments in one function
	print("Example 5: Combining Positional, *args, Keyword, **kwargs")
	combined_arguments(1, 2, 3, 4, keyword_arg1="Hello",
            keyword_arg2="World")
	
	# Demonstration of combined argument types in one function
	print("Example: Combining Positional-Only, *args, Keyword-Only, **kwargs")
	combined_all_args_types(10, 20, 30, 40, 50,
            keyword_arg1="Example", keyword_arg2="Demo", extra1="Extra",
			extra2="Additional")
	print("*" * 80)


# Function with positional-only arguments
def positional_only(x, y, /):
	"""
	Accepts positional-only arguments.

	Args:
		x (int): First integer (positional-only).
		y (int): Second integer (positional-only).

	Returns:
		int: Sum of x and y.
	"""
	return x + y


# Function with arbitrary arguments (*args)
def arbitrary_args(*args):
	"""
	Demonstrates arbitrary arguments with *args.

	Args:
		*args: Variable-length argument list.

	Returns:
		None
	"""
	print("Arguments received (using *args):", args)
	total = sum(args)
	print(f"Sum of all arguments: {total}")


# Function with keyword-only arguments
def keyword_only(x, y, *, keyword_arg):
	"""
	Demonstrates keyword-only arguments.

	Args:
		x (int): Positional argument.
		y (int): Positional argument.
		keyword_arg (str): Must be provided as a keyword argument.

	Returns:
		None
	"""
	print(f"x: {x}, y: {y}, keyword_arg: {keyword_arg}")


# Function with arbitrary keyword arguments (**kwargs)
def arbitrary_keyword_args(**kwargs):
	"""
	Demonstrates arbitrary keyword arguments with **kwargs.

	Args:
		**kwargs: Arbitrary keyword arguments.

	Returns:
		None
	"""
	print("Keyword arguments received (using **kwargs):", kwargs)
	for key, value in kwargs.items():
		print(f"{key}: {value}")


# Function combining positional, *args, keyword-only, and **kwargs
def combined_arguments(x, y, *args, keyword_arg1, keyword_arg2, **kwargs):
	"""
	Combines positional, *args, keyword-only, and **kwargs arguments.

	Args:
		x (int): Positional argument.
		y (int): Positional argument.
		*args: Arbitrary positional arguments.
		keyword_arg1 (str): Must be provided as a keyword argument.
		keyword_arg2 (str): Must be provided as a keyword argument.
		**kwargs: Arbitrary keyword arguments.

	Returns:
		None
	"""
	print("Positional arguments:", x, y)
	print("Arbitrary arguments (*args):", args)
	print("Keyword-only arguments:", keyword_arg1, keyword_arg2)
	print("Additional keyword arguments (**kwargs):", kwargs)
	# Example usage of all arguments
	if args:
		print("Sum of *args:", sum(args))
	print("Keyword arg1:", keyword_arg1)
	print("Keyword arg2:", keyword_arg2)
	for key, value in kwargs.items():
		print(f"{key}: {value}")


# Function combining positional-only, *args, keyword-only, and **kwargs
def combined_all_args_types(pos_only1, pos_only2, /, *args, keyword_arg1, keyword_arg2, **kwargs):
	"""
	Combines positional-only, arbitrary *args, keyword-only, and **kwargs arguments.

	Args:
		pos_only1 (int): Positional-only argument.
		pos_only2 (int): Positional-only argument.
		*args: Arbitrary positional arguments.
		keyword_arg1 (str): Must be provided as a keyword argument.
		keyword_arg2 (str): Must be provided as a keyword argument.
		**kwargs: Arbitrary keyword arguments.

	Returns:
		None
	"""
	print("Positional-only arguments:", pos_only1, pos_only2)
	print("Arbitrary arguments (*args):", args)
	print("Keyword-only arguments:", keyword_arg1, keyword_arg2)
	print("Additional keyword arguments (**kwargs):", kwargs)
	
	# Example usage of all arguments
	if args:
		print("Sum of *args:", sum(args))
	print(f"Keyword arg1: {keyword_arg1}")
	print(f"Keyword arg2: {keyword_arg2}")
	for key, value in kwargs.items():
		print(f"{key}: {value}")


if __name__ == "__main__":
	main()
