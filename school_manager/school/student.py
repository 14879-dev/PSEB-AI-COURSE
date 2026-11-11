
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 11-11-2026

from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    roll_number: str
    marks: list[int] = field(default_factory=list)

    def add_mark(self, mark: int) -> None:
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")

        self.marks.append(mark)

    def average(self) -> float:
        if not self.marks:
            return 0.0

        return sum(self.marks) / len(self.marks)

    def __str__(self) -> str:
        return (
            f"{self.name} (Roll {self.roll_number}): "
            f"Average {self.average():.1f}"
        )
