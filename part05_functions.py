
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 06-11-2026

# ==========================================
# PART 5: FUNCTIONS & COMPREHENSIONS



# ==========================================
# WARM-UP:


print("\n========== WARM-UP ==========")

# Function to calculate area of a circle
def area_of_circle(r):
    return 3.14159 * r * r


# Function to check whether a number is even
def is_even(n):
    return n % 2 == 0


# Function to greet in English or Urdu
def greet(name, lang="en"):
    if lang == "en":
        return f"Hello {name}!"
    elif lang == "ur":
        return f"Salaam {name}!"


# Calling each function 3 times

print("\nArea of Circle:")
print(area_of_circle(5))
print(area_of_circle(7))
print(area_of_circle(10))

print("\nEven Number Check:")
print(is_even(4))
print(is_even(7))
print(is_even(10))

print("\nGreetings:")
print(greet("Mudassir"))
print(greet("Ali", "ur"))
print(greet("Ahmed"))


# ==========================================
# BUILD: STUDENT REPORT
# ==========================================

print("\n========== STUDENT REPORT ==========")

# Function to calculate average marks
def average(marks):
    return sum(marks) / len(marks)


# Function to calculate grade
def grade(marks):
    avg = average(marks)

    if avg < 0 or avg > 100:
        return "Invalid Marks"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 33:
        return "D"
    else:
        return "Fail"


# Function to generate student report
def report(name, marks):
    avg = average(marks)
    student_grade = grade(marks)

    return f"{name} | Average: {avg:.2f} | Grade: {student_grade}"


# Three students
students = [
    ("Mudassir", [85, 90, 88]),
    ("Ali", [70, 75, 72]),
    ("Ahmed", [45, 50, 40])
]

# Generate reports
for name, marks in students:
    print(report(name, marks))


# ==========================================
# CHALLENGE: COMPREHENSIONS
# ==========================================

print("\n========== CHALLENGE ==========")

# 1. List comprehension: Squares from 1 to 10

squares = [number ** 2 for number in range(1, 11)]

print("\nSquares from 1 to 10:")
print(squares)


# 2. List comprehension: Names with more than 4 letters

names = ["Ali", "Ahmed", "Mudassir", "Sara", "Usman", "Ayesha"]

long_names = [name for name in names if len(name) > 4]

print("\nNames with more than 4 letters:")
print(long_names)


# 3. Dictionary comprehension: Student averages

student_marks = {
    "Mudassir": [85, 90, 88],
    "Ali": [70, 75, 72],
    "Ahmed": [45, 50, 40],
    "Usman": [25, 30, 35]
}

student_averages = {
    name: average(marks)
    for name, marks in student_marks.items()
}

print("\nStudent Averages:")
print(student_averages)


# 4. List comprehension: Passing students (average >= 33)

passing_students = [
    name
    for name, avg in student_averages.items()
    if avg >= 33
]

print("\nPassing Students:")
print(passing_students)


print("\n========== PROGRAM FINISHED ==========")
