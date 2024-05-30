import string

'''
Experimenting with creating these lists of numbers letters and symbols automatically so that I dont have to manually type them out.
May not be more efficient than typing them out, but will revist this later
'''

# Generate letters function
def letters_list():
  letters_string = string.ascii_letters

  letters = []

  for char in letters_string:
    letters.append(char)

  return letters

# Generate numbers function
def numbers_list():
  numbers_string = string.digits

  numbers = []

  for char in numbers_string:
    numbers.append(char)

  return numbers

# Generate symbols function
def symbols_list():
  symbols_string = string.punctuation
  
  symbols = []

  for char in symbols_string:
    symbols.append(char)

  return symbols
