import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Select a random word from the list
random_word = random.choice(word_list)

# Initialize variables
guessed_letters = []
max_attempts = 6
attempts = 0

# Create a function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Main game loop
while True:
    # Display the current state of the word
    current_display = display_word(random_word, guessed_letters)
    print(current_display)

    # Check if the player has won
    if current_display == random_word:
        print("Congratulations! You've won. The word was:", random_word)
        break

    # Check if the player has used all their attempts
    if attempts >= max_attempts:
        print("Sorry, you've run out of attempts. The word was:", random_word)
        break

    # Ask the player for a guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is valid (a single letter)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the guess has already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guess is in the word
    if guess in random_word:
        print("Good guess!")
    else:
        print("Sorry, that letter is not in the word.")
        attempts += 1
        print("You have", max_attempts - attempts, "attempts left.")

# End of the game
print("Game over. Thanks for playing!")




