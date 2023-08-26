#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

word = ''
for count in range(int(nr_letters)):
  word += random.choice(letters)

for count in range(int(nr_symbols)):
  word += random.choice(symbols)

for count in range(int(nr_numbers)):
  word += random.choice(numbers)
print(f"Your password is: {word}")
  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
wordList = []
for count in range(int(nr_letters)):
  wordList += random.choice(letters)

for count in range(int(nr_symbols)):
  wordList += random.choice(symbols)

for count in range(int(nr_numbers)):
  wordList += random.choice(numbers)
  
random.shuffle(wordList)

password = ''
for char in wordList:
  password += char
print(f"Your password is: {password}")