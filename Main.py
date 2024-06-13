import random
import hangman_art
import hangman_words
import os
stages = hangman_art.stages

lives = 6
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
display = []
print(hangman_art.logo)
for eachChosenLetter in chosen_word:
    display.append("_")
print(f"The chosen word is {chosen_word}")
blank = "_"
end_of_game = False
while not end_of_game:
    user_guess = input("Guess a letter: ").lower()
    os.system('cls')
    if user_guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == user_guess:
                display[i] = user_guess

    if user_guess in display:
        print("You already guessed this letter.")
        print(display)

    elif user_guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"{user_guess} is not in the word, you lost one life.")
        print(f"Total lives remaining : {lives}.")

    if blank not in display:
        end_of_game = True
        print("You Won")

    if lives == 0:
        end_of_game = True
        print("You Lost")
    print(display)
