print("Welcome to the Treasure Island. \n")
print("Your mission is to find the treasure \n")
choice1 = input('You\'ve come a crossroad, where do you wan to go ? Type "Left" or "Right". \n').lower()
if choice1 == "left":
    choice2 = input('You have come to a lake, there is a island in the middle of the lake. Type "Swim" to swim accross or "Wait" to wait for a boat. \n').lower()
    if choice2 == "wait":
        choice3 = input('You are on the ship now, You arrived at the issland unharmed, There is a house with 3 doors, one Red, one Yellow and one Black. Which door will you choose ? \n')
        if choice3 == "red":
            print('You fell into a birning ring of fire. Game Over')
        elif choice3 == "yellow":
            print('There ia fake Pot of gold, shame on you. Game over')
        elif choice3 == "Black":
            print('There in the dark room shines the Gold Treasure. You win')
    elif choice2 == "swim":
        print('You are attacked and torn appart by a Pufferfish. Game over')
elif choice1 == "right":
    print('Now you are on a endless road to no where. Game over')