
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 10-11-2026

# MAIN PROGRAM

import school_tools

def main():
    print(school_tools.greet("Mudassir"))

    marks = [80, 75, 90, 85]

    average = school_tools.calculate_average(marks)

    print("Student Marks:", marks)
    print("Average Marks:", average)


if __name__ == "__main__":
    main()
