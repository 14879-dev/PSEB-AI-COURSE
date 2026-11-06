
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 06-11-2026


# PART 2: CONDITIONS (




# WARM-UP


print("\n========== EVEN, ODD AND SIGN ==========")

number = int(input("Enter a number: "))

# Checking positive, negative or zero
if number > 0:
    print("The number is positive")

elif number < 0:
    print("The number is negative")

else:
    print("The number is zero")

# Checking even or odd
if number % 2 == 0:
    print("The number is even")

else:
    print("The number is odd")


# ------------------------------------------
# BUILD: GRADE CALCULATOR
# ------------------------------------------

print("\n========== GRADE CALCULATOR ==========")

marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 80:
    print("Grade: A")

elif marks >= 70:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

elif marks >= 33:
    print("Grade: D")

else:
    print("Grade: Fail")


# ------------------------------------------
# CHALLENGE: ELECTRICITY BILL
# ------------------------------------------

print("\n========== ELECTRICITY BILL ==========")

units = float(input("Enter electricity units used: "))

if units < 0:
    print("Invalid units")

else:

    if units <= 100:
        bill = units * 10

    elif units <= 200:
        bill = (100 * 10) + ((units - 100) * 15)

    else:
        bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)

    fixed_charges = 50

    total_bill = bill + fixed_charges

    print(f"Units consumed: {units}")
    print(f"Electricity charges: Rs. {bill:.2f}")
    print(f"Fixed charges: Rs. {fixed_charges:.2f}")
    print(f"Total bill: Rs. {total_bill:.2f}")

print("\n========== PROGRAM FINISHED ==========")
