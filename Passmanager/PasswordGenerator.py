import random
import GenerateVars

# Create lists for letters number and symbol options.

letters = GenerateVars.letters_list()
numbers = GenerateVars.numbers_list()
symbols = GenerateVars.symbols_list()

# ToDo strip symbols that are not accepted by passwords from the list, and strip O's or 0's?

# print(f'Letters: {letters}\nNumbers: {numbers}\nSymbols: {symbols}')

def generate_password():
  # Get the number of letters numbers and symbols wanted in generated password

  # ToDo create a while loop and try statement to make sure only numbers are input

  nr_letters = int(input('\nHow many letters would you like in your password: '))
  nr_numbers = int(input('\nHow many numbers do you want in your password: '))
  nr_symbols = int(input('\nHow many symbols do you want in your password: '))

  # The list that will be randomized and made into a password
  password_list = []

  for x in range(0,nr_letters):
    choice = random.choice(letters)
    password_list.append(choice)

  for x in range(0,nr_numbers):
    choice = random.choice(numbers)
    password_list.append(choice)

  for x in range(0,nr_symbols):
    choice = random.choice(symbols)
    password_list.append(choice)

  random.shuffle(password_list)

  password = ''.join(password_list)

  return password