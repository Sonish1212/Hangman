import random
import hangman_words
import hangman_art

print(hangman_art.logo)
rand_wordlist = random.choice(hangman_words.word_list)
print(rand_wordlist)
display = []
for letter in rand_wordlist:
    display += "_"
print(display)
position = "_"
lives = 6

end_of_game = False
while not end_of_game:
    guess = input("Enter a character you want to guess ")
    for position in range(len(rand_wordlist)):
        letter = rand_wordlist[position]
        if letter == guess:
            display[position] = letter

    if guess not in rand_wordlist:
        lives -= 1
        if lives == 0:
            print("Game over")
            end_of_game = True

    print(display)
    if "_" not in display:
        end_of_game = True
        print("you win")

    print(hangman_art.stages[lives])




