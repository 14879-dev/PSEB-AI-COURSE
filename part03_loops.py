
# Name: Mudassir Munir
# PSEB ID: PSEB-2026-010784
# Date: 06-11-2026

# ==========================================
# PART 3: LOOPS (FOR / WHILE)
# ==========================================

import random


# ------------------------------------------
# WARM-UP: TIMES TABLE
# ------------------------------------------

print("\n========== TIMES TABLE ==========")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# ------------------------------------------
# BUILD: ATM PIN CHECK
# ------------------------------------------

print("\n========== ATM PIN CHECK ==========")

correct_pin = "4321"
attempts = 3

while attempts > 0:

    entered_pin = input("Enter your PIN: ")

    if entered_pin == correct_pin:
        print("Welcome!")
        break

    else:
        attempts = attempts - 1

        if attempts > 0:
            print("Incorrect PIN!")
            print(f"Tries left: {attempts}")

        else:
            print("Card blocked!")


# ------------------------------------------
# CHALLENGE: NUMBER GUESSING GAME
# ------------------------------------------

print("\n========== NUMBER GUESSING GAME ==========")

while True:

    secret_number = random.randint(1, 50)
    guesses = 0

    while True:

        guess = int(input("Guess a number between 1 and 50: "))
        guesses = guesses + 1

        if guess > secret_number:
            print("Too high!")

        elif guess < secret_number:
            print("Too low!")

        else:
            print(f"Got it in {guesses} guesses!")
            break

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break


print("\n========== PROGRAM FINISHED ==========")
