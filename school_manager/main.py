
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 11-11-2026

from school.student import Student
from school.grades import report_card
from school.storage import save_students, load_students


def add_student(students: list[Student]) -> None:
    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()

    if not name or not roll_number:
        print("Name and roll number cannot be empty.")
        return

    if any(student.roll_number == roll_number for student in students):
        print("A student with this roll number already exists.")
        return

    student = Student(name, roll_number)
    students.append(student)

    print(f"Student {name} added successfully!")


def find_student(
    students: list[Student],
    roll_number: str
) -> Student | None:
    for student in students:
        if student.roll_number == roll_number:
            return student

    return None


def add_marks(students: list[Student]) -> None:
    roll_number = input("Enter student roll number: ").strip()

    student = find_student(students, roll_number)

    if student is None:
        print("Student not found.")
        return

    try:
        mark = int(input("Enter marks (0-100): "))
        student.add_mark(mark)
        print("Marks added successfully!")

    except ValueError as error:
        print(f"Invalid input: {error}")


def show_report(students: list[Student]) -> None:
    roll_number = input("Enter student roll number: ").strip()

    student = find_student(students, roll_number)

    if student is None:
        print("Student not found.")
        return

    print(report_card(student))


def class_ranking(students: list[Student]) -> None:
    if not students:
        print("No students available.")
        return

    ranked_students = sorted(
        students,
        key=lambda student: student.average(),
        reverse=True
    )

    print("\n========== CLASS RANKING ==========")

    for position, student in enumerate(ranked_students, start=1):
        print(
            f"{position}. {student.name} | "
            f"Roll: {student.roll_number} | "
            f"Average: {student.average():.2f}"
        )

    print("===================================")


def main() -> None:
    try:
        students: list[Student] = load_students()
        print(f"Loaded {len(students)} student(s).")

    except (OSError, ValueError) as error:
        print(f"Could not load student data: {error}")
        students = []

    while True:
        print("\n===== SCHOOL MANAGER =====")
        print("1. Add student")
        print("2. Add marks")
        print("3. Show report card")
        print("4. Class ranking")
        print("5. Save and exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            add_marks(students)

        elif choice == "3":
            show_report(students)

        elif choice == "4":
            class_ranking(students)

        elif choice == "5":
            try:
                save_students(students)
                print("Student data saved successfully!")

            except OSError as error:
                print(f"Could not save student data: {error}")

            print("Exiting School Manager...")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
