
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 11-11-2026

from school.student import Student


def calculate_average(marks: list[int]) -> float:
    if not marks:
        return 0.0

    return sum(marks) / len(marks)


def calculate_grade(average: float) -> str:
    if average < 0 or average > 100:
        raise ValueError("Average must be between 0 and 100")

    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 33:
        return "D"
    else:
        return "Fail"


def report_card(student: Student) -> str:
    average = calculate_average(student.marks)
    student_grade = calculate_grade(average)

    return (
        f"\n===== REPORT CARD =====\n"
        f"Name: {student.name}\n"
        f"Roll Number: {student.roll_number}\n"
        f"Marks: {student.marks}\n"
        f"Average: {average:.2f}\n"
        f"Grade: {student_grade}\n"
        f"=======================\n"
    )
