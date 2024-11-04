#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: positional_keyword_parameters_01
#
# Description: Demonstrates the use of positional-only and keyword-only
#              parameters in Python. This program shows how to define functions
#              with positional-only and keyword-only arguments, providing
#              greater control over how arguments are passed.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Positional-Only and Keyword-Only Parameters in Python ==========")
    print("Python allows specifying positional-only and keyword-only parameters for better control.")
    print("*" * 80)

    # Basic example with positional-only and keyword-only parameters
    print("1. Basic Example of Positional-Only and Keyword-Only Parameters")
    print_parameters(1, 2, kw_only=3)
    print("*" * 80)

    # Real-world example: Function for processing customer orders
    print("2. Real-World Example: Processing Customer Orders")
    process_order("Alice", "Standard Shipping", quantity=2, expedite=True)
    print("*" * 80)


# Basic example function with positional-only and keyword-only parameters
def print_parameters(pos_only, /, standard, *, kw_only):
    """
    Prints the values of positional-only, standard, and keyword-only parameters.

    Args:
        pos_only: Positional-only parameter.
        standard: Standard parameter (can be positional or keyword).
        kw_only: Keyword-only parameter.
    """
    print("Positional-Only Parameter:", pos_only)
    print("Standard Parameter:", standard)
    print("Keyword-Only Parameter:", kw_only)


# Real-world example: Processing an order with specific requirements
def process_order(customer_name, shipping_type, /, *, quantity=1, expedite=False):
    """
    Processes an order with specified options for a customer.

    Args:
        customer_name (str): Name of the customer (positional-only).
        shipping_type (str): Type of shipping (positional-only).
        quantity (int, optional): Quantity of items. Default is 1.
        expedite (bool, optional): Expedited shipping option. Default is False.
    """
    print(f"Processing order for {customer_name}")
    print(f"Shipping Type: {shipping_type}")
    print(f"Quantity: {quantity}")
    print(f"Expedite: {'Yes' if expedite else 'No'}")


if __name__ == "__main__":
    main()
