#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: callback_functions
#
# Description: Demonstrates the concept of callback functions in Python.
#              This program includes examples of basic callback usage and
#              real-world applications for asynchronous operations.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Callback Functions in Python ==========")
    print("This program demonstrates callback functions with basic and real-world examples.")
    print("*" * 80)

    # Example: Basic Callback
    print("Basic Callback Example:")
    perform_operation(5, 3, add, "Adding")  # Passing `add` as a callback
    perform_operation(10, 5, subtract, "Subtracting")  # Passing `subtract` as a callback

    print("\nReal-World Example: Simulated Asynchronous Operation")
    simulate_download("file1.zip", on_download_complete)  # Passing `on_download_complete` as a callback

    print("*" * 80)


# Basic mathematical functions to use as callbacks
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# Function that accepts a callback function
def perform_operation(x, y, callback, operation_name="Operation"):
    """
    Performs an operation on two numbers using a callback function.

    Args:
        x (int): The first number.
        y (int): The second number.
        callback (function): The callback function to apply on x and y.
        operation_name (str): A name to describe the operation.
    """
    result = callback(x, y)
    print(f"{operation_name} result of {x} and {y}: {result}")


# Real-world example: Simulate a download with a callback
import time

def simulate_download(file_name, callback):
    """
    Simulates a file download and triggers a callback upon completion.

    Args:
        file_name (str): Name of the file being downloaded.
        callback (function): Callback function to execute once download completes.
    """
    print(f"Starting download of '{file_name}'...")
    time.sleep(2)  # Simulate download time delay
    print(f"Download of '{file_name}' completed.")
    callback(file_name)  # Call the callback function


# Callback function for download completion
def on_download_complete(file_name):
    """
    Callback function that gets executed upon download completion.

    Args:
        file_name (str): Name of the file downloaded.
    """
    print(f"File '{file_name}' is ready for processing!")


if __name__ == "__main__":
    main()

