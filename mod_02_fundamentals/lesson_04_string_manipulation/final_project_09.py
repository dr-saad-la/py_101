#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: String Real World Use Cases
#
# Description: Demonstrates real-world examples of string manipulation
#              in Python, including data cleaning, URL encoding,
#              customer review processing, and log file data extraction.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	
	print("============ Demonstrating Real-World String Manipulation Examples ============")
	print_real_world_concepts()
	print("*" * 80)
	
	print("Using String Manipulation in Real-World Scenarios".center(80))
	data_cleaning_example()
	print("-" * 80)
	url_encoding_example()
	print("-" * 80)
	text_cleaning_example()
	print("-" * 80)
	review_processing_example()
	print("-" * 80)
	data_extraction_example()
	print("*" * 80)


# Function to explain real-world use cases of string manipulation
def print_real_world_concepts():
	"""
	Print explanations of real-world string manipulation applications.
	"""
	
	print("Real-World Applications of String Manipulation in Python:")
	print("1. Standardizing and cleaning data entries (e.g., names in a database).")
	print("2. URL encoding to prepare URLs for web requests.")
	print("3. Text cleaning and normalization for data analysis.")
	print("4. Processing customer reviews to clean and format text.")
	print("5. Extracting useful information from log files or datasets.")


# Project 1: Data Cleaning for a Database
def data_cleaning_example():
	"""
	Cleans a sample name by stripping whitespace and capitalizing first letters.
	"""
	print("\nProject 1: Data Cleaning for a Database")
	name = "  john doe  "
	clean_name = name.strip().title()
	print(f"Formatted name: '{clean_name}'")  # Output: 'John Doe'


# Project 2: URL Encoding for Web Development
def url_encoding_example():
	"""
	Encodes a sample URL by replacing spaces with '%20'.
	"""
	print("\nProject 2: URL Encoding for Web Development")
	url = "https://example.com/users?name=john doe&age=30"
	encoded_url = url.replace(" ", "%20")
	print(f"Encoded URL: '{encoded_url}'")  # Output: 'https://example.com/users?name=john%20doe&age=30'


# Project 3: Text Cleaning for Data Analysis
def text_cleaning_example():
	"""
	Cleans and normalizes a sample text by stripping whitespace and converting to lowercase.
	"""
	print("\nProject 3: Text Cleaning for Data Analysis")
	review = "   this product is amazing! highly recommend.   "
	clean_review = review.strip().lower()
	print(f"Cleaned review: '{clean_review}'")  # Output: 'this product is amazing! highly recommend.'


# Project 4: Processing Customer Reviews
def review_processing_example():
	"""
	Cleans, formats, and replaces specific words in a customer review.
	"""
	print("\nProject 4: Processing Customer Reviews")
	review = "   This product is AMAZING!!!   "
	cleaned_review = review.strip().lower().replace("amazing", "great")
	print(f"Cleaned review: '{cleaned_review}'")  # Output: 'this product is great!!!'


# Project 5: Data Extraction from Log Files
def data_extraction_example():
	"""
	Extracts specific information from a log entry.
	"""
	print("\nProject 5: Data Extraction from Log Files")
	log_entry = "ERROR 404: Page not found"
	error_code = log_entry.split()[1]  # Extracts '404'
	print(f"Error code: '{error_code}'")  # Output: '404'


if __name__ == "__main__":
	main()