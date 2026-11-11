
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 11-11-2026

# ==========================================
# PART 12: DEBUGGING AND TESTING
# WARM-UP: FIX 3 BUGS
# ==========================================

print("\n========== PART 12 WARM-UP ==========")

marks = [90, 25, 70]

passing = []

# FIX 1: Include the last element
for m in range(len(marks)):

    # Check passing marks
    if marks[m] > 33:

        # FIX 2: Append instead of replacing the list
        passing.append(marks[m])


print("All Marks:", marks)
print("Passing Marks:", passing)

# FIX 3: Divide by the number of passing students
average_marks = sum(passing) / len(passing)

print("Average Passing Marks:", average_marks)


# ==========================================
# BUG EXPLANATIONS
# ==========================================

print("\n========== BUG EXPLANATIONS ==========")

print("Bug 1: Off-by-one / loop boundary error")
print("The loop skipped the last element.")

print("\nBug 2: Logical error")
print("The list was replaced instead of appending new marks.")

print("\nBug 3: Calculation error")
print("The average was divided by all marks instead of passing marks.")

print("\n========== PROGRAM FINISHED ==========")
