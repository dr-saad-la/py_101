#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: logical_ops_01
#
# Description: Demonstrates logical operators in Python.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
def main():
    print_logical_operators()
    logical_ops()


def print_logical_operators():
    print("Logical Operators in Python:")
    print("and : Returns True if both statements are true")
    print("or  : Returns True if at least one statement is true")
    print("not : Reverses the result, returns False if the result is true")

def logical_ops():
    a = True
    b = False
    print("\nLogical Operations Examples:")
    print(f"{a} and {b} -> {a and b}")    # Logical AND
    print(f"{a} or {b} -> {a or b}")      # Logical OR
    print(f"not {a} -> {not a}")          # Logical NOT



if __name__ == "__main__":
    main()