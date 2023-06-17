import random

def select_character():
    with open('characters.txt', 'r') as file:
        characters = file.read().splitlines()
    return random.choice(characters)

def play_game():
    character = select_character()
    guessed = False
    guesses = []

    print("Welcome to the MCU Character Guessing Game!")
    print("Guess the name of the character from the MCU.")
    print("The name contains only letters and spaces.")
    print("Let's begin!")

    while not guessed:
        guess = input("\nEnter your guess: ").strip().lower()

        if guess == character.lower():
            guessed = True
        else:
            if guess in guesses:
                print("You've already guessed that. Try again.")
            else:
                guesses.append(guess)
                print("Incorrect guess. Try again.")

    print("\nCongratulations! You guessed the character correctly!")
    print("The character was:", character)

play_game()
