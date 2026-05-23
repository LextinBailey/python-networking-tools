import random

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt} of {max_attempts}")

        while True:
            try:
                guess = int(input("Enter your guess: "))

                if guess < 1 or guess > 100:
                    print("Guess must be between 1 and 100.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.")
            
        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")
        
        else:
            print("You guessed the number!")
            break

    if guess != secret_number:
        print(f"\nYou lost! The number was {secret_number}")

while True:
    play_game()

    again = input("\nPlay again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break