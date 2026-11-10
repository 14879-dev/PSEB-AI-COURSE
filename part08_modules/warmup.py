
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 10-11-2026

# PART 8: MODULES, PACKAGES & PROJECTS
# WARM-UP: STANDARD LIBRARY TOUR

import math
import random
import datetime
import statistics

# 1. MATH MODULE
print("\n========== MATH MODULE ==========")

print("Square root of 144:", math.sqrt(144))


# 2. RANDOM MODULE
print("\n========== RANDOM MODULE ==========")

students = ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"]

selected_student = random.choice(students)

print("Randomly selected student:", selected_student)


# 3. DATETIME MODULE
print("\n========== DATETIME MODULE ==========")

today = datetime.date.today()

year_end = datetime.date(today.year, 12, 31)

days_remaining = (year_end - today).days

print("Today's date:", today)
print("Days until December 31:", days_remaining)


# 4. STATISTICS MODULE
print("\n========== STATISTICS MODULE ==========")

marks = [70, 80, 90, 85, 75]

print("Marks:", marks)
print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))


print("\n========== PROGRAM FINISHED ==========")
