import random

HANGMAN = [
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]


print('\nWelcome to the man that hangs game !\n')

lives = 6
not_game_over = True

words = ['ponytail', 'clouds', 'mountain']
chosen_word = random.choice(words)

guess_word = ''
correct_letters = []

for letter in chosen_word:
    guess_word += '_'

print(HANGMAN[lives])
print(guess_word)
print('\n')

while not_game_over:
    display = ''

    if lives >= 2:
        print(f"You have {lives} lifes left")
    elif lives == 1:
        print(f"You have {lives} life left")

    user_letter = input('Select a letter : ').lower()

    for letter in chosen_word:
        if letter == user_letter :
            display += letter
            correct_letters.append(user_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'
    
    print('\n')
    print(HANGMAN[lives])
    print(display)
    print('\n')

    if user_letter not in chosen_word:
        lives -= 1

    if lives == 0:
        print(f"Game over the correct word was -> {chosen_word}\n")
        not_game_over = False

    if '_' not in display:
        print('You won\n')
        not_game_over = False