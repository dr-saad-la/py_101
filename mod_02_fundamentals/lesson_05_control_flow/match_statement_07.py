#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Match Statement
#
# Description: Demonstrates the use of the `match` statement in Python,
#              introduced in Python 3.10 as a flexible alternative to
#              if/elif chains for decision-making. This program includes
#              basic and advanced examples of match for clear understanding.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	print("============ Match Statement Tutorial ============")
	
	# Basic Example
	print("\nBasic Example: Grading System")
	score = 85
	grade = get_grade(score)
	print(f"Score: {score} -> Grade: {grade}")
	
	# Advanced Example
	print("\nAdvanced Example: HTTP Status Code Handling")
	status_code = 404
	status_message = handle_response(status_code)
	print(f"Status Code: {status_code} -> Message: {status_message}")
	
	print("=" * 80)


# Function to demonstrate match statement with a grading system
def get_grade(score):
	"""
	Returns the grade for a given score using the match statement.

	Args:
		score (int): The score to evaluate.

	Returns:
		str: The grade based on the score.
	"""
	match score:
		case 90 | 100:
			return "A"
		case 80 | 89:
			return "B"
		case 70 | 79:
			return "C"
		case _:
			return "F"


# Function to demonstrate match statement for handling HTTP status codes
def handle_response(status_code):
	"""
	Returns a message based on the HTTP status code using the match statement.

	Args:
		status_code (int): The HTTP status code to evaluate.

	Returns:
		str: The message corresponding to the status code.
	"""
	match status_code:
		case 200:
			return "OK"
		case 404:
			return "Not Found"
		case 500:
			return "Internal Server Error"
		case _:
			return "Unknown Status"


if __name__ == "__main__":
	main()