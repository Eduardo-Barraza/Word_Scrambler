
1. **Choosing and Scrambling the Word**:
   - A random word is selected from the `word_list` and scrambled.

2. **Handling User Guesses**:
   - The user is prompted to guess the unscrambled word.
   - If the guess is correct, the user wins and the game ends.
   - If the guess is incorrect, the number of attempts is decreased.
   - If the user runs out of attempts, the game ends and the correct word is revealed.

### Full Directory Structure

Ensure your project directory looks like this:

```
/project_directory
    word_list.py
    word_scrambler.py
    main.py
```

#### 1. `word_list.py`

```python
word_list = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
```

#### 2. `word_scrambler.py`

```python
logo = '''
 _    _               _  _                    _____                 _           
| |  | |             | |(_)                  / ____|               | |          
| |  | |  __ _   ___ | | _  _ __    __ _    | (___   _ __    __ _  | | __   __ _ 
| |  | | / _` | / __|| || || '_ \  / _` |    \___ \ | '__|  / _` | | |/ /  / _` |
| |__| || (_| || (__ | || || | | || (_| |    ____) || |    | (_| | |   <  | (_| |
 \____/  \__,_| \___||_||_||_| |_| \__, |   |_____/ |_|     \__,_| |_|\_\  \__,_|
                                    __/ |                                         
                                   |___/                                          
'''

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
```


1. **Choosing and Scrambling the Word**:
   - A random word is selected from the `word_list` and scrambled.

2. **Handling User Guesses**:
   - The user is prompted to guess the unscrambled word.
   - If the guess is correct, the user wins and the game ends.
   - If the guess is incorrect, the number of attempts is decreased.
   - If the user runs out of attempts, the game ends and the correct word is revealed.

### Full Directory Structure

Ensure your project directory looks like this:

```
/project_directory
    word_list.py
    word_scrambler.py
    main.py
```

#### 1. `word_list.py`

```python
word_list = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
```

#### 2. `word_scrambler.py`

```python
logo = '''
 _    _               _  _                    _____                 _           
| |  | |             | |(_)                  / ____|               | |          
| |  | |  __ _   ___ | | _  _ __    __ _    | (___   _ __    __ _  | | __   __ _ 
| |  | | / _` | / __|| || || '_ \  / _` |    \___ \ | '__|  / _` | | |/ /  / _` |
| |__| || (_| || (__ | || || | | || (_| |    ____) || |    | (_| | |   <  | (_| |
 \____/  \__,_| \___||_||_||_| |_| \__, |   |_____/ |_|     \__,_| |_|\_\  \__,_|
                                    __/ |                                         
                                   |___/                                          
'''
