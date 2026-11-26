import random


def hangman():
    # 5 predefined words ki list (CodeAlpha requirement ke mutabiq)
    words = ["python", "code", "alpha", "game", "learn"]

    # Randomly ek word chunna
    word = random.choice(words)

    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6  # Maximum incorrect guesses ki limit

    print("Welcome to Hangman Game!")
    print(f"You have {max_incorrect} incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect:
        # Word ko underscores (_) ki shakal mein dikhana
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())

        # Check karna ke player jeet gaya ya nahi
        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word correctly!")
            break

        # User se letter lena
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Check karna ke guess theek hai ya galat
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            remaining = max_incorrect - incorrect_guesses
            print(f"Wrong guess! Incorrect guesses left: {remaining}")

    else:
        print(f"\n❌ Game Over! The word was '{word}'. Better luck next time!")


# Function ko call karna
if __name__ == "__main__":
    hangman()