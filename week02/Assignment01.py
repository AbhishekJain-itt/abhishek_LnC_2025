import random

def is_valid_guess(user_input):
    return user_input.isdigit() and 1 <= int(user_input) <= 100


def main():
    secret_number = random.randint(1, 100)
    is_guessed = False
    guess_count = 0

    user_input = input("Guess a number between 1 and 100: ")

    while not is_guessed:
        if not is_valid_guess(user_input):
            user_input = input("Invalid input. Please enter a number between 1 and 100: ")
            continue

        guess = int(user_input)
        guess_count += 1

        if guess < secret_number:
            user_input = input("Too low. Guess again: ")
        elif guess > secret_number:
            user_input = input("Too high. Guess again: ")
        else:
            print(f"You guessed it in {guess_count} guesses!")
            is_guessed = True


main()
