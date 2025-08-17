import random

print("Number Guessing Challenge!")
print("Guess the secret number between 1 and 100.")

number = random.randint(1, 100)  # secret number
tries = 0

while True:
    guess = int(input("Your guess: "))
    tries += 1

    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print(f"You got it! The number was {number}. Attempts taken: {tries}")
        break
