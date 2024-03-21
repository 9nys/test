import random


def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple"]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "*"
    return display


def play_game():
    word = choose_word()
    max_attempts = int(input("Enter the maximum number of attempts you want: "))
    attempts = max_attempts
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word:", display_word(word, guessed_letters))
    print("You have", attempts, "attempts remaining.")

    while attempts > 0:
        guess = input("Enter a letter or guess the whole word: ").lower()

        if len(guess) == 1:  # If the user guessed a letter
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                print("Correct guess!")
                print(display_word(word, guessed_letters))
            else:
                print("Sorry, that letter is not in the word.")
                attempts -= 1
        elif len(guess) == len(word):
            if guess == word:
                print("Congratulations! You guessed the word correctly:", word)
                return
            else:
                print("Sorry, that's not the word.")
                attempts = 0
        else:
            print("Invalid input. Please enter a single letter or the whole word.")

        if "*" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word correctly:", word)
            return

        print("You have", attempts, "attempts remaining.")

    print("Sorry, you've run out of attempts. The word was:", word)


play_game()
