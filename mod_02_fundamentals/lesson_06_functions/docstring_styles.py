#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: different_docstring_styles
#
# Description: This program demonstrates multiple docstring formats, including
#              Google, NumPy, and reStructuredText styles. These different styles
#              can be used to enhance the readability and organization of function
#              documentation.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== Different Docstring Styles in Python ==========")
    print("This program demonstrates different styles of function docstrings.")
    print("*" * 80)

    print(f"Addition Result: {add_google_style(3, 5)}")
    print("\nDocstring for 'add_google_style' function:")
    print(add_google_style.__doc__)

    print(f"Multiplication Result: {multiply_numpy_style(4, 6)}")
    print("\nDocstring for 'multiply_numpy_style' function:")
    print(multiply_numpy_style.__doc__)

    display_message_rst_style("Hello, world!")
    print("\nDocstring for 'display_message_rst_style' function:")
    print(display_message_rst_style.__doc__)

    print("*" * 80)

# Google-style docstring
def add_google_style(a, b):
    """
    Adds two numbers and returns the result.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.

    Returns:
        int or float: The sum of the two input numbers.

    Example:
        >>> add_google_style(3, 5)
        8
    """
    return a + b

# NumPy-style docstring
def multiply_numpy_style(a, b):
    """
    Multiply two numbers and return the result.

    Parameters
    ----------
    a : int or float
        The first number to multiply.
    b : int or float
        The second number to multiply.

    Returns
    -------
    int or float
        The product of `a` and `b`.

    Examples
    --------
    >>> multiply_numpy_style(3, 4)
    12
    """
    return a * b

# reStructuredText (reST) style docstring
def display_message_rst_style(message):
    """
    Display a message to the console.

    :param message: The message to display
    :type message: str

    :Example:

    >>> display_message_rst_style("Hello, world!")
    Hello, world!
    """
    print(message)

if __name__ == "__main__":
    main()
