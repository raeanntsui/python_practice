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
    populate the guess_tracker here
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
words_list = ["hello", "paradise", "parade", "random", "python"]
winning_word = random.choice(words_list) # pick a random word from the given list of words in "words_list"
past_guesses = []
guess_tracker = len(winning_word) * ["_"]
print(f"Word to guess = {' '.join(guess_tracker)}")
# print(winning_word)

while lives > 0:
    print(f"You currently have {lives} lives.")
    guess = input("Please enter your guess! If you want to go ahead and guess the whole word, please type exactly: 'guess now'.\n")
    if guess == 'guess now':
        guess_now = input("Take your guess now!\n")
        if guess_now == winning_word:
            print("Congratulations! You win the game!")
            break
        else:
            lives -= 1
            print("Please try again! That was not the correct word :(")
            continue
    if guess in winning_word:
        print("You got one!")
        for index, letter in enumerate(winning_word):
            if guess == letter:
                guess_tracker[index] = guess
                print(f"Guess tracker: {' '.join(guess_tracker)}")
    elif not guess in winning_word:
        print(f"There is no '{guess}'... try again.")
        lives -= 1
        print(f"Guess tracker: {' '.join(guess_tracker)}")

if lives == 0:
    print(f"Game over! The winning word was '{winning_word}'.")                  