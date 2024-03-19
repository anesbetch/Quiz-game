import random

def play_number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try guessing a higher number.")
            else:
                print("Too high! Try guessing a lower number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    play_number_guessing_game()
