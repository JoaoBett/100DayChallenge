import random
from words_hangman import word_list
from hangman_stages import HANGMANPICS

print("Welcome to the Hangman Game!!\n\n")

chosen_word=random.choice(word_list)
size_final_word=len(chosen_word)

end_of_game = False
lives = 6

blank_word=[]
#Fill blank word with "_"
for _ in range(size_final_word):
    blank_word+="_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in blank_word:
        print(f"You have already guessed {guess}!")

    #Check if the letter guessed is in the word
    for position in range(size_final_word):
        letter = chosen_word[position]
        if letter == guess:
            blank_word[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word! You lose a life.")

        lives -= 1
        if lives == 0:
            print("YOU LOST - GAMEOVER")
            end_of_game = True
        
    print(f"{''.join(blank_word)}")

    if "_" not in blank_word:
        print("YOU WON - GAME OVER")
        end_of_game = True
    
    print(HANGMANPICS[lives])