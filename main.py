# import required modules
import random
from hangman_art import stages, logo
from hangman_words import word_list


# printing logo at top of game
print(f"{logo}\n")


# create variable to keep track of number of lives and start by setting it to 6
number_lives = 6


# choose random word from word list
chosen_word = random.choice(word_list)


# create an empty list called display and add a "_" to the list for each letter in chosen_word
display = []
for letter in chosen_word:
    display.append("_")


# print display before user makes any guesses
print(f"{display}\n")


# create an empty list to keep track of guessed letter
letters_guessed = []


while "_" in display:
    # get user input for a guess and add it to letters_guessed list
    guess = input("Guess a letter: ").lower()

    if guess in letters_guessed:
        print(f"You already guessed the letter {guess}.")
    else:
        letters_guessed.append(guess)

        # create variable to keep track if there is a match in the word from the guess and start by setting it to False
        match_found = False

        # replace "_" with guess at correct position if guess is in chosen_word
        display_index = 0
        for letter in chosen_word:
            if letter == guess:
                display[display_index] = letter
                match_found = True
            display_index += 1

        # deduct a life if no match was found
        if match_found == False:
            number_lives -= 1
            print(f"The letter '{guess}' is not in the word. You lost a life.")

        # print ASCII art corresponding to number of lives
        print(stages[number_lives])

        # game over if no lives left
        if number_lives == 0:
            print("Game over. You lose.")
            print(f"The correct word was '{chosen_word}'.")
            break

        # output current display to user
        print(display)

# if player guessed all letters in word print win message with lives left
if number_lives > 0:
    print("You guessed the word. You win!")
