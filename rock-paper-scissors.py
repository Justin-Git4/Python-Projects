import random

# Rock
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

images = [rock, paper, scissors]

print('Are you ready for some Rock Paper Scissors ? \n')

computer_choice = random.randint(1,3)

user_choice = input('What do you choose ? Type "1" for Rock, "2" for Paper or "3" for Scissors. \n')
user_choice = int(user_choice)
print('\n')

print (f'You chose {user_choice}')
print(images[user_choice - 1])
print('\n')

print (f'The computer chose {computer_choice}')
print(images[computer_choice - 1])

if user_choice >= 4 or user_choice < 1:
    print('You tuped in an invalid number. YOU LOSE !\n')
elif user_choice == computer_choice:
    print('It\'s a DRAW !\n')
elif user_choice == 1 and computer_choice == 3:
    print('You WIN !\n')
elif computer_choice == 1 and user_choice == 3:
    print('You LOSE !\n')
elif computer_choice > user_choice:
    print('You LOSE !\n')
elif user_choice > computer_choice:
    print('You WIN !\n')