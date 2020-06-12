# Game of Hangman!
# Obtains a word from a (for now) hard-coded list for user to guess. Program
# gets user input in form of a letter and checks to see if the letter is in the
# word. The user gets 5 chances to guess incorrectly. They win if the entire word
# is guessed, and lose when all 5 chances run out.

import random
import sys

# # get a random word from an input file of words?
# def get_words(input_file):
#     word_file = open(input_file, "r")
#     content = word_file.read()
#     word_file.close()
#     return content.split()

# an input is valid if it is 1 length character and a/A-z/Z
def valid_input(input):
    if len(input) > 1:
            print("1 letter at a time!")
            return False;
    elif not input.isalpha():
            print("not a valid letter! aA-zZ pls")
            return False;
    return True;

# to-do: find another way to get words. input file or another source to be self-reliant
# words = get_words("words.txt")
words = ["example", "truancy", "utopia", "potato", "rhythm", "astronomical", "pinstripe", "stupendous"]
keep_playing = True

# Program Start!
while words and keep_playing:
    guesses_remaining = 5
    word_list = list(random.choice(words))
    word = ''.join(word_list)
    user_word_list = list("_" * len(word))
    ic_guesses_list = []

    print("\nStarting hangman game! (enter \"quit\" to exit game)")

    while (guesses_remaining > 0):
        user_word = ''.join(user_word_list)
        ic_guesses = ''.join(ic_guesses_list)

        print(f'\nYour word is {user_word} [{ic_guesses}]')
        print(f'You have {guesses_remaining} strikes left')

        guess = input("Take a guess :) ").lower()
        if guess == "quit":
            exit();
        elif  len(guess) != 0 and valid_input(guess):
            if guess in user_word_list or guess in ic_guesses_list:
                print("you've already guessed this letter! try another")
            elif guess in word: # get indices of guess from word and update guess
                indices = []
                count = 0

                for i in range(len(word)):
                    if word[i] == guess:
                        user_word_list.pop(i)
                        user_word_list.insert(i, guess)
                        count += 1

                single = "is"
                s = ""
                if count > 1:
                    single = "are"
                    s = "\'s"
                print(f'There {single} {count} {guess}{s}')
                if user_word_list == word_list:
                    words.pop(words.index(word))

                    print(f"\nThe word is {word}!")
                    print("YOU WIN!")
                    again = input("Play again? (y for yes): ")
                    if again.lower() != "y":
                        keep_playing = False
                    break
            else: # incorrect guess
                ic_guesses_list.append(guess)
                guesses_remaining -= 1
                print(f'{guess} is not in the word :(')
                if guesses_remaining == 0:
                    again = input("\nOut of guesses X( Try again? (y for yes):")
                    if again.lower() != "y":
                        keep_playing = False
                    break
