
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 11-11-2026

import pytest

from school.student import Student
from school.grades import calculate_average, calculate_grade, report_card
from school.storage import save_students, load_students


# Student tests

def test_student_creation() -> None:
    student = Student("Ali", "101")

    assert student.name == "Ali"
    assert student.roll_number == "101"
    assert student.marks == []


def test_add_mark() -> None:
    student = Student("Ali", "101")
    student.add_mark(85)

    assert student.marks == [85]


def test_invalid_mark() -> None:
    student = Student("Ali", "101")

    with pytest.raises(ValueError):
        student.add_mark(120)


def test_student_average() -> None:
    student = Student("Ali", "101")
    student.add_mark(80)
    student.add_mark(90)

    assert student.average() == 85.0


# Grade tests

def test_calculate_average() -> None:
    assert calculate_average([80, 90, 70]) == 80.0


def test_calculate_grade() -> None:
    assert calculate_grade(85) == "A"
    assert calculate_grade(75) == "B"
    assert calculate_grade(65) == "C"
    assert calculate_grade(40) == "D"
    assert calculate_grade(20) == "Fail"


def test_report_card() -> None:
    student = Student("Ali", "101")
    student.add_mark(90)
    student.add_mark(80)

    report = report_card(student)

    assert "Ali" in report
    assert "101" in report
    assert "Average: 85.00" in report
    assert "Grade: A" in report


# JSON storage tests

def test_save_and_load_students(tmp_path) -> None:
    student = Student("Ali", "101")
    student.add_mark(85)
    student.add_mark(90)

    file_path = tmp_path / "school.json"

    save_students([student], str(file_path))
    loaded_students = load_students(str(file_path))

    assert len(loaded_students) == 1
    assert loaded_students[0].name == "Ali"
    assert loaded_students[0].roll_number == "101"
    assert loaded_students[0].marks == [85, 90]


def test_load_missing_file(tmp_path) -> None:
    file_path = tmp_path / "missing.json"

    students = load_students(str(file_path))

    assert students == []
