
# Data Types

# String
print("Hello"[0])
print("123" + "345")

# Integer
print(123 + 345)
print(1_200 + 100)

# Float 
print(1.345)

# Boolean
print(True)
print(False)

# Quiz
street_name = "Abbey Road"
print(street_name[4] + street_name[7])

# Typo
print(type("check"))

# Convert num to string
string_length = len(input("Type your name? "))
convert_to_string = str(string_length)
print("Your name has " + convert_to_string + " length!")

# Exercise 1
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# PENDAS
# ()
# **
# *
# /
# +
# -

# Exercise 2
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = int(weight)/(float(height)**2)
print(int(BMI))

# f-Strings
score = 2
isWinning = True
print(f"Your scoure is {score} and your win is {isWinning}")

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
age = int(input("What is your current age? "))
years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
