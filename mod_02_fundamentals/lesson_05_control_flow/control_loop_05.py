#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Control Loops with Break and Continue
#
# Description: Demonstrates controlling loops in Python using `break` and
#              `continue` statements in both `for` and `while` loops,
#              including real-world applications.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	print("============ Loop Control with Break and Continue ============")
	
	print("Example 1: Using `break` in a Loop (Exit Prematurely)")
	break_example()
	print("-" * 80)
	
	print("Example 2: Using `continue` in a Loop (Skip Iterations)")
	continue_example()
	print("-" * 80)
	
	print("Example 3: Real-World Example - Cart Limit in Online Shopping")
	cart_limit_example()
	print("-" * 80)
	
	print("Example 4: Real-World Example - Processing Only Available Items")
	stock_availability_example()
	print("-" * 80)
	
	print("Example 5: Controlled While Loop Using Break and Continue")
	controlled_while_loop()
	print("=" * 80)


# Example 1: Using `break` in a Loop
def break_example():
	"""
	Demonstrates the use of `break` to exit a loop when a specific condition is met.
	"""
	print("Breaking the loop when number equals 5.")
	for number in range(1, 10):
		if number == 5:
			print(f"Number is {number}, exiting the loop.")
			break  # Exit the loop when number is 5
		print(f"Current number: {number}")
	print("Loop exited with `break`.\n")


# Example 2: Using `continue` in a Loop
def continue_example():
	"""
	Demonstrates the use of `continue` to skip certain iterations in a loop.
	"""
	print("Skipping even numbers.")
	for number in range(1, 10):
		if number % 2 == 0:
			continue  # Skip even numbers
		print(f"Odd number: {number}")
	print("Loop completed with `continue`.\n")


# Example 3: Real-World Example - Cart Limit in Online Shopping
def cart_limit_example():
	"""
	A real-world example where `break` is used to stop processing items
	once the cart total exceeds a certain value.
	"""
	print("Processing cart items until the total exceeds 100.")
	cart = [10, 20, 30, 50, 100]
	total = 0
	
	for price in cart:
		total += price
		print(f"Added ${price}. Current total: ${total}")
		if total > 100:
			print("Cart limit exceeded. Stopping further processing.")
			break
	print("Cart processing completed.\n")


# Example 4: Real-World Example - Processing Only Available Items
def stock_availability_example():
	"""
	A real-world example where `continue` is used to skip items that are out of stock.
	"""
	print("Processing items in stock only.")
	items_in_stock = [True, False, True, True]  # True means available, False means out of stock
	
	for index, item_available in enumerate(items_in_stock, start=1):
		if not item_available:
			print(f"Item {index} is out of stock, skipping.")
			continue  # Skip unavailable items
		print(f"Processing available item {index}")
	print("Stock processing completed.\n")


# Example 5: Controlled While Loop Using Break and Continue
def controlled_while_loop():
	"""
	Demonstrates using break and continue statements within a while loop.
	"""
	print("Using 'break' to stop the loop when count equals 3.")
	count = 0
	while count < 5:
		if count == 3:
			print("Breaking the loop as count reached 3.")
			break
		print(f"Count is: {count}")
		count += 1
	
	print("\nUsing 'continue' to skip when count equals 2.")
	count = 0
	while count < 5:
		count += 1
		if count == 2:
			print("Skipping this iteration as count equals 2.")
			continue
		print(f"Count is: {count}")
	print("Controlled while loop with break and continue completed.\n")


if __name__ == "__main__":
	main()