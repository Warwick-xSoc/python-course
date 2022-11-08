# Guessing game
from random import randint
from time import sleep

answer = randint(1, 1000)  # My random number

attempts = 0
guess = 0
while True:
    sleep(0.2)

    guess = input("Guess a number between 1 and 1000: ")
    if not guess.isdigit() or int(guess) < 1 or int(guess) > 1000:
        continue

    attempts += 1
    if int(guess) > answer:
        print(f"{guess} is too high...")
    elif int(guess) < answer:
        print(f"{guess} is too low...")
    else:
        break

print(f"Correct! The number was {guess}.")
print(f"This took you {attempts} attempts.")