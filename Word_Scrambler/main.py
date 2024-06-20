import random

# Import the word list from word_list.py
from word_list import word_list

# Import the logo from word_scrambler.py
from word_scrambler import logo
print(logo)

# Choose a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Scramble the chosen word
scrambled_word = ''.join(random.sample(chosen_word, len(chosen_word)))

# Print the scrambled word
print(f"Scrambled word: {scrambled_word}")

end_of_game = False
attempts = 3

while not end_of_game:
    guess = input("Guess the unscrambled word: ").lower()

    if guess == chosen_word:
        print("You win!")
        end_of_game = True
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect! You have {attempts} attempts left. Try again.")
        else:
            print(f"You lose. The correct word was '{chosen_word}'.")
            end_of_game = True


end_of_game = False
attempts = 3

while not end_of_game:
    guess = input("Guess the unscrambled word: ").lower()

    if guess == chosen_word:
        print("You win!")
        end_of_game = True
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect! You have {attempts} attempts left. Try again.")
        else:
            print(f"You lose. The correct word was '{chosen_word}'.")
            end_of_game = True
