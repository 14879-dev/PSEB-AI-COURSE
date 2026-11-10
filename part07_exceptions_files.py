
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 09-11-2026

import csv
import json
from datetime import date

# ==========================================
# PART 7: EXCEPTIONS & FILES
# ==========================================


# ==========================================
# WARM-UP: SAFE DIVISION
# ==========================================

print("\n========== WARM-UP: SAFE DIVISION ==========")

while True:

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 / num2

        print(f"Result: {result}")
        break

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    except ZeroDivisionError:
        print("Cannot divide by zero! Try again.")


# ==========================================
# BUILD: DIARY APP
# ==========================================

print("\n========== BUILD: DIARY APP ==========")

diary_file = "diary.txt"

while True:

    print("\n1. Add Diary Entry")
    print("2. Read Diary Entries")
    print("3. Exit Diary")

    choice = input("Enter your choice: ")

    # Add diary entry
    if choice == "1":

        note = input("Write your diary note: ")

        current_date = date.today()

        with open(diary_file, "a") as file:
            file.write(f"{current_date}: {note}\n")

        print("Diary entry saved successfully!")

    # Read diary entries
    elif choice == "2":

        try:
            with open(diary_file, "r") as file:
                content = file.read()

                if content:
                    print("\nYour Diary Entries:")
                    print(content)
                else:
                    print("No entries yet")

        except FileNotFoundError:
            print("No entries yet")

    # Exit
    elif choice == "3":
        print("Exiting Diary...")
        break

    else:
        print("Invalid choice! Try again.")


# ==========================================
# CHALLENGE: CSV AND JSON RESULT SHEET
# ==========================================

print("\n========== CHALLENGE: RESULT SHEET ==========")

# Same students and marks from Part 4
result_sheet = {
    "Ali": [75, 80, 65],
    "Ahmed": [90, 85, 95],
    "Sara": [55, 60, 70],
    "Usman": [30, 45, 35],
    "Ayesha": [88, 92, 90]
}

# Save result sheet to CSV
with open("result_sheet.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Student", "Subject 1", "Subject 2",
                     "Subject 3", "Total", "Average"])

    for student, marks in result_sheet.items():

        total = sum(marks)
        average = total / len(marks)

        writer.writerow([
            student,
            marks[0],
            marks[1],
            marks[2],
            total,
            round(average, 2)
        ])

print("Result sheet saved to CSV successfully!")


# Save result sheet to JSON
with open("result_sheet.json", "w") as file:

    json.dump(result_sheet, file, indent=4)

print("Result sheet saved to JSON successfully!")


# Read CSV and find topper
highest_total = -1
topper = ""

with open("result_sheet.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        total = int(row["Total"])

        if total > highest_total:
            highest_total = total
            topper = row["Student"]


# Display topper
print("\n========== CLASS TOPPER ==========")

print(f"Topper: {topper}")
print(f"Total Marks: {highest_total}")


print("\n========== PROGRAM FINISHED ==========")
