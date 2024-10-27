#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: assignment_ops_01
#
# Description: Demonstrates assignment operators in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
def main():
	print_assignment_operators()
	assignment_ops()
	
def print_assignment_operators():
	print("Assignment Operators in Python:")
	print("=  : Assigns a value to a variable")
	print("+= : Adds the right operand to the left operand and assigns the result to the left operand")
	print("-= : Subtracts the right operand from the left operand and assigns the result to the left operand")
	print("*= : Multiplies the right operand by the left operand and assigns the result to the left operand")
	print("/= : Divides the left operand by the right operand and assigns the result to the left operand")


def assignment_ops():
	x = 5
	print("\nAssignment Operations Examples:")
	
	print(f"x = {x}")  # Initial value of x
	
	x += 3  # Equivalent to x = x + 3
	print(f"x += 3 -> {x}")  # 8
	
	x -= 2  # Equivalent to x = x - 2
	print(f"x -= 2 -> {x}")  # 6
	
	x *= 2  # Equivalent to x = x * 2
	print(f"x *= 2 -> {x}")  # 12
	
	x /= 4  # Equivalent to x = x / 4
	print(f"x /= 4 -> {x}")  # 3.0


if __name__ == "__main__":
	main()