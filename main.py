import random
from hangman_words import word_list
from hangman_art import stages, logo
import os

def clear():
    os.system('clear')

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

clear()
print(logo)

# TESTING CODE - COMMENT FOR PRODUCTION
# Uncomment to show the correct word at the start
print(f'Pssst, the solution is {chosen_word}.')

# CREATE BLANKS
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")

    # CHECK GUESSED LETTER
    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    # CHECK IF USER IS WRONG
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print(f"The word is {chosen_word}.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(stages[lives])

    # CHECK USER GOT ALL THE LETTERS
    if "_" not in display:
        end_of_game = True
        clear()
        print(f"The word is {chosen_word}.")
        print(stages[lives])
        print("YOU WIN!")
