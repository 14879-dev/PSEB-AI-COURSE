
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 11-11-2026

import json
from pathlib import Path

from school.student import Student


def save_students(
    students: list[Student],
    path: str = "school.json"
) -> None:
    data = []

    for student in students:
        data.append({
            "name": student.name,
            "roll_number": student.roll_number,
            "marks": student.marks
        })

    file_path = Path(path)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_students(path: str = "school.json") -> list[Student]:
    file_path = Path(path)

    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        students: list[Student] = []

        for item in data:
            student = Student(
                name=item["name"],
                roll_number=item["roll_number"]
            )

            for mark in item["marks"]:
                student.add_mark(mark)

            students.append(student)

        return students

    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Could not load student data: {error}")
        return []
