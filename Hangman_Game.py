import random

def select_random_word():
    # List of words to choose from
    words = ["python", "hangman", "programming", "developer", "algorithm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Show the word with guessed letters revealed and the rest as underscores
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Welcome to Hangman!")
    
    word_to_guess = select_random_word()
    guessed_letters = set()
    attempts_remaining = 6  # Limit on incorrect guesses
    
    while attempts_remaining > 0:
        print("\nWord: ", display_word(word_to_guess, guessed_letters))
        print(f"Attempts remaining: {attempts_remaining}")
        print("Guessed letters: ", " ".join(sorted(guessed_letters)))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            attempts_remaining -= 1
        
        # Check if the player has guessed the word
        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nCongratulations! You've guessed the word:", word_to_guess)
            break
    else:
        print("\nGame Over! The word was:", word_to_guess)

# Run the game
hangman()