import random

print('welcome to the Password Generator !\n')

number_of_letters = int(input('How many letters would you like in your password ?\n'))
print('\n')

number_of_numbers = int(input('How many numbers would you like in your password ?\n'))
print('\n')

number_of_symbols = int(input('How many symbols would you like in your password ?\n'))
print('\n')

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

password_list = []

for character in range(0, number_of_letters ):
    password_list.append(random.choice(letters))

for number in range(0, number_of_numbers ):
    password_list.append(random.choice(numbers))

for symbol in range(0, number_of_symbols ):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ''

for value in password_list:
    password += value
print(f'Your password is : {password}\n')