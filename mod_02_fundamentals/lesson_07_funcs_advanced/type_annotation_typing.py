#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: type_annotations_typing_module
#
# Description: This program demonstrates the use of type annotations
#              with the `typing` module. Type annotations enhance
#              readability, aid debugging, and ensure clarity for
#              expected function input and output types.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

from typing import List, Dict, Optional, Callable

def main():
    print("========== Type Annotations with typing Module ==========")
    print("This program demonstrates type annotations for clarity and debugging.")
    print("*" * 80)

    # Demonstrate annotated functions
    students = ["Alice", "Bob", "Charlie"]
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

    print("Average score:", calculate_average(scores))
    print("Greeting:", greet("Alice"))
    print("Processed scores:", process_scores(scores, round_score))
    print("*" * 80)

# Function using List and Dict types for precise argument annotations
def calculate_average(grades: Dict[str, int]) -> float:
    """
    Calculate the average score from a dictionary of grades.

    Args:
        grades (Dict[str, int]): A dictionary with student names as keys and scores as values.

    Returns:
        float: The average score of all students.
    """
    total = sum(grades.values())
    count = len(grades)
    return total / count if count else 0.0

# Function with Optional and List annotations
def greet(name: Optional[str] = None) -> str:
    """
    Generate a greeting message. If no name is provided, returns a default greeting.

    Args:
        name (Optional[str]): The name of the person to greet. Defaults to None.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!" if name else "Hello, guest!"

# Function using Callable as a parameter type
def process_scores(grades: Dict[str, int], operation: Callable[[int], int]) -> Dict[str, int]:
    """
    Apply a given operation to each student's score.

    Args:
        grades (Dict[str, int]): Dictionary with student names and scores.
        operation (Callable[[int], int]): Function to apply to each score.

    Returns:
        Dict[str, int]: Dictionary with student names and processed scores.
    """
    return {name: operation(score) for name, score in grades.items()}

# Helper function to demonstrate Callable usage
def round_score(score: int) -> int:
    """
    Rounds the given score to the nearest multiple of 10.

    Args:
        score (int): The original score.

    Returns:
        int: The rounded score.
    """
    return round(score / 10) * 10

if __name__ == "__main__":
    main()
