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

lives = ["♥", "♥", "♥", "♥", "♥"]
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