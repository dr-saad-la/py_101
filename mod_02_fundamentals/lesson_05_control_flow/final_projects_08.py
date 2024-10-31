#!/usr/bin/env python3
# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-201
# Lesson: Real World Projects
#
# Description: Demonstrates real-world applications of control flow and
#              loops in a fitness tracking app. This program provides feedback
#              on steps taken, hydration level, and calorie intake, helping users
#              meet their fitness goals.
#
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================

def main():
	print("=========== Fitness Tracker: Daily Goals Check ===========")
	
	# Case 1: Step Tracking
	print("\nStep Tracking:")
	track_steps()
	
	# Case 2: Hydration Tracking
	print("\nHydration Tracking:")
	track_hydration()
	
	# Case 3: Calorie Intake Tracking
	print("\nCalorie Intake Tracking:")
	track_calories()
	
	print("=" * 80)
	
	evaluate_student_performance()
	print("*"*80)


# Case 1: Step Tracking
def track_steps():
	"""
	Tracks daily steps and checks if the user meets their step goal.
	"""
	steps = [800, 1000, 1200, 2000, 2500]  # Step count over the week
	step_goal = 1500
	
	for daily_steps in steps:
		if daily_steps >= step_goal:
			print(f"Great! You walked {daily_steps} steps, meeting your goal!")
		else:
			print(f"You only walked {daily_steps} steps. Keep going!")


# Case 2: Hydration Tracking
def track_hydration():
	"""
	Tracks daily water intake and checks if the user meets their hydration goal.
	"""
	water_intake = [1.2, 1.5, 1.8, 2.0, 1.0]  # Daily water intake in liters
	hydration_goal = 2.0  # Liters
	
	for daily_water in water_intake:
		if daily_water >= hydration_goal:
			print(f"Good job! You drank {daily_water}L of water, meeting your hydration goal.")
		else:
			print(f"You only drank {daily_water}L of water. Try to reach {hydration_goal}L tomorrow.")


# Case 3: Calorie Intake Tracking
def track_calories():
	"""
	Tracks daily calorie intake and checks if the user is within their calorie target.
	"""
	calorie_intake = [1800, 2200, 2000, 2500, 1900]  # Daily calorie intake
	calorie_target = 2000  # Calorie target
	
	for daily_calories in calorie_intake:
		if daily_calories <= calorie_target:
			print(f"Great! You consumed {daily_calories} calories, staying within your target.")
		else:
			print(f"You consumed {daily_calories} calories, exceeding your target. Be mindful of your intake.")


def evaluate_student_performance():
    """
    Evaluates student performance based on scores using a match statement
    for grading and an if statement to flag failing students.
    """
    print("=========== Student Performance Evaluation ===========")

    # List of students and their respective scores
    students_scores = [("Alice", 85), ("Bob", 92), ("Charlie", 67), ("Diana", 75)]

    # Loop through each student and their score
    for student, score in students_scores:
        # Determine the grade using match statement
        match score:
            case score if score >= 90:
                grade = "A"
            case score if 80 <= score < 90:
                grade = "B"
            case score if 70 <= score < 80:
                grade = "C"
            case score if 60 <= score < 70:
                grade = "D"
            case _:
                grade = "F"

        # Display the student's name, score, and grade
        print(f"{student} received a grade of {grade}.")

        # Check if the student has failed
        if grade == "F":
            print(f"{student} failed the course.")

    print("=" * 80)


if __name__ == "__main__":
	main()