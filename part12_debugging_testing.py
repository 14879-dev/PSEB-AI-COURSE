
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 11-11-2026

# =====================================================
# PART 12: DEBUGGING AND TESTING
# =====================================================

# =====================================================
# WARM-UP: DEBUGGING
# =====================================================

print("\n========== WARM-UP: DEBUGGING ==========")

marks = [90, 25, 70]
passing = []

for m in range(len(marks)):
    if marks[m] > 33:
        passing.append(marks[m])

average_marks = sum(passing) / len(passing)

print("All Marks:", marks)
print("Passing Marks:", passing)
print("Average Passing Marks:", average_marks)


# Three bugs fixed:
# 1. range(len(marks) - 1) skipped the last mark.
# 2. passing = [marks[m]] replaced the list instead of appending.
# 3. Average was divided by all marks instead of passing marks.


# =====================================================
# BUILD: GRADE FUNCTION AND PYTEST TESTS
# =====================================================

print("\n========== BUILD: GRADE FUNCTION ==========")

def grade(mark: int) -> str:
    if mark < 0 or mark > 100:
        raise ValueError("Marks must be between 0 and 100")

    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 33:
        return "D"
    else:
        return "Fail"


# Demonstrate grade function
test_marks = [32, 33, 59, 60, 69, 70, 79, 80]

for mark in test_marks:
    print(f"Marks: {mark} | Grade: {grade(mark)}")


# =====================================================
# CHALLENGE: BANK ACCOUNT CLASS
# =====================================================

print("\n========== CHALLENGE: BANK ACCOUNT ==========")

class BankAccount:

    def __init__(self, balance: float):
        if balance < 0:
            raise ValueError("Starting balance cannot be negative")

        self.balance = balance
        self.history = []

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.balance += amount
        self.history.append(f"Deposited Rs. {amount}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        self.history.append(f"Withdrawn Rs. {amount}")


# Demonstrate bank account
account = BankAccount(1000)

print("Starting Balance:", account.balance)

account.deposit(500)
print("After Deposit:", account.balance)

account.withdraw(200)
print("After Withdrawal:", account.balance)

print("Transaction History:")
for transaction in account.history:
    print(transaction)


# =====================================================
# PYTEST TESTS
# Run using: python -m pytest -v
# =====================================================

import pytest


# BUILD TESTS: Grade function

@pytest.mark.parametrize(
    "mark, expected",
    [
        (32, "Fail"),
        (33, "D"),
        (59, "D"),
        (60, "C"),
        (69, "C"),
        (70, "B"),
        (79, "B"),
        (80, "A")
    ]
)
def test_grade_boundaries(mark, expected):
    assert grade(mark) == expected


def test_marks_above_100():
    with pytest.raises(ValueError):
        grade(105)


def test_negative_marks():
    with pytest.raises(ValueError):
        grade(-5)


# CHALLENGE TESTS: Bank Account

@pytest.fixture
def account():
    return BankAccount(1000)


def test_deposit(account):
    account.deposit(500)
    assert account.balance == 1500


def test_withdraw(account):
    account.withdraw(300)
    assert account.balance == 700


def test_history(account):
    account.deposit(500)
    account.withdraw(200)
    assert len(account.history) == 2


def test_invalid_deposit(account):
    with pytest.raises(ValueError):
        account.deposit(-100)


def test_insufficient_balance(account):
    with pytest.raises(ValueError):
        account.withdraw(2000)
