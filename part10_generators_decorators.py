
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 10-11-2026

# PART 10: ITERATORS, GENERATORS AND DECORATORS


# ==========================================
# WARM-UP: COUNTDOWN GENERATOR
# ==========================================

def countdown(n):
    while n > 0:
        yield n
        n -= 1


print("\n========== WARM-UP: COUNTDOWN ==========")

for number in countdown(5):
    print(number)


# ==========================================
# WARM-UP: EVEN NUMBERS GENERATOR
# ==========================================

def evens(limit):
    for number in range(0, limit + 1, 2):
        yield number


print("\n========== WARM-UP: EVEN NUMBERS ==========")

print(list(evens(10)))


# ==========================================
# BUILD: BIG FILE READER
# ==========================================

# Creating a text file with 50 lines

with open("server_logs.txt", "w") as file:

    for i in range(1, 51):

        if i % 5 == 0:
            file.write(f"Line {i}: ERROR - Something went wrong\n")

        else:
            file.write(f"Line {i}: System running normally\n")


# Generator to read file line by line

def read_lines(path):
    with open(path, "r") as file:
        for line in file:
            yield line


# Generator to filter ERROR lines

def only_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line


print("\n========== BUILD: BIG FILE READER ==========")

error_count = 0

for error in only_errors(read_lines("server_logs.txt")):
    print(error.strip())
    error_count += 1

print("\nTotal ERROR lines:", error_count)


# ==========================================
# CHALLENGE: OWN DECORATORS
# ==========================================

import time
from functools import wraps


# TIMER DECORATOR

def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = function(*args, **kwargs)

        end_time = time.time()

        print("Execution Time:", end_time - start_time, "seconds")

        return result

    return wrapper


# LOG CALLS DECORATOR

def log_calls(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Function Name:", function.__name__)
        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)

        result = function(*args, **kwargs)

        return result

    return wrapper


# FUNCTION USING BOTH DECORATORS

@timer
@log_calls
def calculate_sum(start, end):

    total = 0

    for number in range(start, end + 1):
        total += number

    return total


print("\n========== CHALLENGE: DECORATORS ==========")

result = calculate_sum(1, 1000000)

print("Sum from 1 to 1,000,000:", result)


print("\n========== PART 10 COMPLETED ==========")
