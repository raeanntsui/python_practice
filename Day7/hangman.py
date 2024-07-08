import random

print("""
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"                   
""")


"""
Notes:
Before guessing...
1. Have a log of words to choose from: words_list
    - winning_word = randomize a word from words_list
2. Have a lives tracker (5 lives)
3. Have a running list of the previous guesses to make sure the player does not repeat a guess: past_guesses
4. Have a guess_tracker => replace blanks with guesses from the user
    guess_tracker = "_ _ _ _ _"

If there are lives left (lives > 0), then prompt the user for guesses!

LOOP:
if lives > 0:
    ask the player for a guess
    if guess is correct aka guess matches one of the letters in winning_word:
        guess_tracker will update the underscores in place of the correct guess
    if guess is not correct:
        lives -= 1
        restart the loop to ask for a guess

if lives == 0:
    game over

"""
lives = 5
words_list = ["hello", "raeann", "yoyo", "potato", "tomato", "smiski", "sonny"]
hangman_word = random.choice(words_list) # pick a random word from the given list of words in "words_list"

print(hangman_word)
new_hangman_word = "_" * len(hangman_word)
# print(new_hangman_word)
guess = input("Please enter your guess! Enter one letter only please :)\n")

new_hangman_word_list = list(new_hangman_word)
# print("new hangman word is", new_hangman_word_list)

for idx, letter in enumerate(hangman_word): # print the placeholders for the length of the hangman_word
    if letter == guess:
        print(letter)
        hangman_word[idx] = guess
    else:
        print("_", end="")
print()
new_hangman_word = "".join(new_hangman_word_list)
print(new_hangman_word)