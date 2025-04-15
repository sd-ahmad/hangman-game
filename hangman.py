import words as words
import random

def choose_word():
    word = random.choice(words.words)
    return word

def output_word(word):
    output = ""
    for letter in word:
        output += " … "
    return output

word_to_guess = choose_word()
attempts = 7
running = True
guessed_letters = []

print("\n               HANGMAN                    ")
print(f"You have {attempts} attempts to guess the word.\n")
print(output_word(word_to_guess))

while running == True:

    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")

    elif guess in word_to_guess:
        guessed_letters.append(guess)
        print("Good guess.")
        print(f"Correct guess. Attempts remaining: {attempts}")

        new_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                new_word += letter
            else:
                new_word += " … "
        print(new_word)

        if " … " not in new_word:
            print(f"You won! The word was {word_to_guess}.")
            
            try:
                choice = input("\nDo you want to play again? [Yes] [No]\n").lower()
                if choice == "yes":
                    word_to_guess = choose_word()
                    attempts = 7
                    running = True
                    guessed_letters = []
                else:
                    running = False
            except ValueError: 
                print("Please answer correctly.")

    else:
        attempts -= 1
        guessed_letters.append(guess)
        print(f"Incorrect guess. Attempts remaining: {attempts}")

    if attempts == 0:
        print(f"You lost! The word was {word_to_guess}.")

        try:
            choice = input("\nDo you want to play again? [Yes] [No]\n").lower()
            if choice == "yes":
                word_to_guess = choose_word()
                attempts = 7
                running = True
                guessed_letters = []
            else:
                running = False
        except ValueError: 
            print("Please answer correctly.")