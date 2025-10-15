import random

print("Welcome to the guessing game!")

# Random number between 1 and 10
secret_number = random.randint(1, 10)
attempts = 0

while attempts < 3:
    try:
        guessed_number = int(input("Guess a number from 1 to 10: "))
        attempts += 1

        if guessed_number < secret_number:
            print("Too low! Try again.")
        elif guessed_number > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} tries.")
            break

    except ValueError:
        print("Please enter a valid number!")

# If user fails after 3 attempts
if attempts == 3 and guessed_number != secret_number:
    print(f"Try again later! The correct number was {secret_number}.")

