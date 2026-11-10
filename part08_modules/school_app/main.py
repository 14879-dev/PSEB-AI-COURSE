
from school.grades import calculate_grade
from school.attendance import attendance_percentage


def main():
    marks = 85
    grade = calculate_grade(marks)

    attendance = attendance_percentage(18, 20)

    print("Student Marks:", marks)
    print("Student Grade:", grade)
    print("Attendance:", attendance, "%")


if __name__ == "__main__":
    main()
