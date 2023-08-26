### Print ###
# Write your code below this line 👇
# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")

# print('Hello ' + input("What is your name? ") + '!')
print( len( input("What is your name? ") ) )


### Variables ###
name = input("What is your name?")
print(name)

# challange
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

temp = a
a = b
b = temp

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

### Brand name generator ###
#1. Create a greeting for your program.
print("Welcome to the brand name!")
#2. Ask the user for the city that they grew up in.
city = input("What's an city you are grown?\n")
#3. Ask the user for the name of a pet.
pet_name = input("Name of your pet?\n")
#4. Combine the name of their city and pet and show them their band name.
brand_name = city + pet_name
print("Your brand name could be " + brand_name)
