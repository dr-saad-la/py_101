#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: arbitrary_args_kwargs_01
#
# Description: Demonstrates the use of *args and **kwargs in Python to
#              handle variable numbers of arguments in a function. This
#              program shows how to define functions with *args for
#              arbitrary positional arguments and **kwargs for arbitrary
#              keyword arguments.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Arbitrary Arguments and Keyword Arguments in Python ==========")
    print("This lesson covers how to use *args and **kwargs for variable arguments.")
    print("*" * 80)

    # Basic example using *args and **kwargs
    print("1. Basic Example of *args and **kwargs")
    print_arguments(1, 2, 3, name="Alice", age=25)
    print("*" * 80)

    # Real-world example: Logging events with optional details
    print("2. Real-World Example: Event Logging with Variable Details")
    log_event("User login", username="Alice")
    log_event("File uploaded", filename="report.pdf", filesize="2MB")
    log_event("Error", code=404, message="Not Found", severity="High")
    print("*" * 80)


# Basic example function with *args and **kwargs
def print_arguments(*args, **kwargs):
    """
    Prints arbitrary positional and keyword arguments.

    Args:
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.
    """
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)


# Real-world example: Logging events with variable details
def log_event(event_type, *args, **kwargs):
    """
    Logs an event with additional details using *args and **kwargs.

    Args:
        event_type (str): Type of event being logged.
        *args: Additional positional information.
        **kwargs: Additional keyword information about the event.
    """
    print(f"Event: {event_type}")

    # Process positional arguments if any
    if args:
        print("Additional Info:", args)

    # Process keyword arguments if any
    if kwargs:
        for key, value in kwargs.items():
            print(f"{key.capitalize()}: {value}")
    print("-" * 40)


if __name__ == "__main__":
    main()
