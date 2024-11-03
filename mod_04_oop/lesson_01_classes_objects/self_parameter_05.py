#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Self Parameter Example
#
# Description: This program demonstrates the use of the `self` parameter in class
#              methods. The `Rectangle` class uses `self` to reference instance
#              attributes `width` and `height` and to calculate the area of
#              the rectangle for each instance independently.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
    print("========== The `self` Parameter in Python Classes ==========")
    print("This program demonstrates how the `self` parameter allows access to instance attributes.")
    print("*" * 80)

    # Create two instances of the Rectangle class
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(7, 3)

    # Calculate and display areas of both rectangles
    print(f"Area of rect1 (5 x 10): {rect1.area()}")  # Expected output: 50
    print(f"Area of rect2 (7 x 3): {rect2.area()}")    # Expected output: 21

    print("*" * 80)

# Define the Rectangle class
class Rectangle:
    """
    A class to represent a rectangle, using `self` to handle instance attributes.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle using `self` to access instance attributes.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

if __name__ == "__main__":
    main()
