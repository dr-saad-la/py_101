#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: global_variable_tracking_01
#
# Description: Demonstrates modifying a global variable in a function
#              by simulating page visit tracking. Each function call
#              increments a global counter, representing the number of
#              page visits.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

# Global variable to track page visits
visit_count = 0  # Initial visit count, accessible globally

def main():
    print("========== Page Visit Tracking Example ==========")
    print("This program tracks the number of page visits using a global counter.")
    print("*" * 60)

    # Simulating multiple page visits
    simulate_visits()

    print("*" * 60)

# Function to simulate page visit tracking
def visit_page():
    """
    Increments the global visit_count variable each time
    this function is called, simulating a page visit.
    """
    global visit_count  # Declare that we're modifying the global variable
    visit_count += 1
    print(f"Visit count: {visit_count}")

def simulate_visits():
    """
    Calls visit_page multiple times to simulate consecutive page visits.
    """
    visit_page()  # First visit: visit_count should be 1
    visit_page()  # Second visit: visit_count should be 2
    visit_page()  # Third visit: visit_count should be 3

if __name__ == "__main__":
    main()