# William Froehlich
# CIS261
# Week 10 VIBE Coding
# Student Grade Calculator

# VIBE AI-assisted coding process: building the grade calculator step by step.

students = []


def calculate_average(score1, score2, score3):
	"""Calculate the average of three test scores."""
	return (score1 + score2 + score3) / 3


def determine_letter_grade(average):
	"""Return a letter grade based on the student's average."""
	if average >= 90:
		return "A"
	if average >= 80:
		return "B"
	if average >= 70:
		return "C"
	if average >= 60:
		return "D"
	return "F"


def get_valid_score(prompt):
	"""Get a non-blank numeric score from 0 through 100."""
	# VIBE testing found that a blank score caused a ValueError, so validation was added.
	while True:
		score_text = input(prompt).strip()
		if not score_text:
			print("Error: Test score cannot be blank. Please try again.")
			continue

		try:
			score = float(score_text)
		except ValueError:
			print("Error: Test score must be a number from 0 through 100. Please try again.")
			continue

		if not 0 <= score <= 100:
			print("Error: Test score must be between 0 and 100. Please try again.")
			continue

		return score


def add_student():
	"""Get student information, calculate the grade, and add the student."""
	name = input("Enter student name: ")
	student_id = input("Enter student ID: ")
	score1 = get_valid_score("Enter test score 1: ")
	score2 = get_valid_score("Enter test score 2: ")
	score3 = get_valid_score("Enter test score 3: ")

	average = calculate_average(score1, score2, score3)
	letter_grade = determine_letter_grade(average)

	student = {
		"name": name,
		"student_id": student_id,
		"score1": score1,
		"score2": score2,
		"score3": score3,
		"average": average,
		"letter_grade": letter_grade,
	}
	students.append(student)
	# VIBE testing showed that calculated results were stored but not displayed after adding.
	print(f"{name} was added successfully.")
	print(f"Name: {student['name']}")
	print(f"Student ID: {student['student_id']}")
	print(f"Average: {student['average']:.2f}")
	print(f"Letter Grade: {student['letter_grade']}")


def display_students():
	"""Display all students in a formatted table."""
	if not students:
		print("No students have been added yet.")
		return

	print("\nStudent Grade Report")
	print("-" * 85)
	print(
		f"{'Name':<20}{'Student ID':<15}{'Test 1':>10}"
		f"{'Test 2':>10}{'Test 3':>10}{'Average':>10}{'Grade':>10}"
	)
	print("-" * 85)
	for student in students:
		print(
			f"{student['name']:<20}{student['student_id']:<15}"
			f"{student['score1']:>10.2f}{student['score2']:>10.2f}"
			f"{student['score3']:>10.2f}{student['average']:>10.2f}"
			f"{student['letter_grade']:>10}"
		)
	print("-" * 85)


def main():
	"""Run the student grade calculator menu."""
	print("Student Grade Calculator")

	while True:
		print("\nMain Menu")
		print("1. Add New Student")
		print("2. Display All Students")
		print("3. Search Student by Name")
		print("4. View Class Statistics")
		print("5. Save and Exit")

		choice = input("Enter your choice: ")

		if choice == "1":
			add_student()
		elif choice == "2":
			display_students()
		elif choice == "3":
			print("Search Student by Name will be added in a later VIBE iteration.")
		elif choice == "4":
			print("Class Statistics will be added in a later VIBE iteration.")
		elif choice == "5":
			print("Thank you for using the Student Grade Calculator.")
			break
		else:
			print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
	main()
