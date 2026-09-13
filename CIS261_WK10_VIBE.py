# William Froehlich
# CIS261
# Week 10 VIBE Coding
# Student Grade Calculator

# VIBE AI-assisted coding process: building the grade calculator step by step.

FILE_NAME = "student_grades.txt"
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


def display_student_details(student):
	"""Display all details for one student."""
	print(f"Name: {student['name']}")
	print(f"Student ID: {student['student_id']}")
	print(f"Test 1: {student['score1']:.2f}")
	print(f"Test 2: {student['score2']:.2f}")
	print(f"Test 3: {student['score3']:.2f}")
	print(f"Average: {student['average']:.2f}")
	print(f"Letter Grade: {student['letter_grade']}")


def search_student():
	"""Search for students by name without considering letter case."""
	search_name = input("Enter student name to search: ").strip().lower()
	found_students = [
		student for student in students
		if student["name"].lower() == search_name
	]

	if not found_students:
		print("Student not found.")
		return

	for student in found_students:
		print("\nStudent Found")
		display_student_details(student)


def display_class_statistics():
	"""Display average, highest, and lowest student averages."""
	if not students:
		print("No students are available for class statistics.")
		return

	class_average = sum(student["average"] for student in students) / len(students)
	highest_student = max(students, key=lambda student: student["average"])
	lowest_student = min(students, key=lambda student: student["average"])

	print("\nClass Statistics")
	print(f"Class Average: {class_average:.2f}")
	print(
		f"Highest Student Average: {highest_student['average']:.2f} "
		f"({highest_student['name']})"
	)
	print(
		f"Lowest Student Average: {lowest_student['average']:.2f} "
		f"({lowest_student['name']})"
	)


def save_students():
	"""Save all student records to the grade file."""
	try:
		with open(FILE_NAME, "w", encoding="utf-8") as file:
			for student in students:
				file.write(
					f"{student['name']}|{student['student_id']}|"
					f"{student['score1']}|{student['score2']}|{student['score3']}|"
					f"{student['average']}|{student['letter_grade']}\n"
				)
		return True
	except OSError as error:
		print(f"Error saving student records: {error}")
		return False


def load_students():
	"""Load student records from the grade file when it exists."""
	try:
		with open(FILE_NAME, "r", encoding="utf-8") as file:
			for line_number, line in enumerate(file, start=1):
				fields = line.rstrip("\n").split("|")
				if len(fields) != 7:
					print(f"Skipping invalid record on line {line_number}.")
					continue

				try:
					student = {
						"name": fields[0],
						"student_id": fields[1],
						"score1": float(fields[2]),
						"score2": float(fields[3]),
						"score3": float(fields[4]),
						"average": float(fields[5]),
						"letter_grade": fields[6],
					}
				except ValueError:
					print(f"Skipping invalid record on line {line_number}.")
					continue

				students.append(student)
	except FileNotFoundError:
		# The file may not exist on the first run.
		pass
	except OSError as error:
		print(f"Error loading student records: {error}")


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
	# VIBE development added file loading so saved records are available at startup.
	load_students()
	print("Student Grade Calculator")

	while True:
		print("\nMain Menu")
		print("1. Add New Student")
		print("2. Display All Students")
		print("3. Search Student by Name")
		print("4. View Class Statistics")
		print("5. Save and Exit")

		try:
			choice = input("Enter your choice: ").strip()
		except (EOFError, KeyboardInterrupt):
			choice = "5"

		if choice == "1":
			add_student()
		elif choice == "2":
			display_students()
		elif choice == "3":
			search_student()
		elif choice == "4":
			display_class_statistics()
		elif choice == "5":
			if save_students():
				print(f"Student records saved to {FILE_NAME}.")
			print("Thank you for using the Student Grade Calculator. Goodbye!")
			break
		elif choice == "\x1b":
			if save_students():
				print(f"Student records saved to {FILE_NAME}.")
			print("ESC pressed. Student Grade Calculator is exiting.")
			break
		else:
			print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
	main()
