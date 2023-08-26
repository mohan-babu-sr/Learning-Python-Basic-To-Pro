print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("U r ready to ride!")
else:
  print("U r not allowed to take a ride!")


# Check given number is odd or even
number = int(input("Which number do you want to check? "))

checkNumber = number % 2

if checkNumber == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Leap year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# Bill calculator
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

T = name1.count("t") + name2.count("t")
R = name1.count("r") + name2.count("r")
U = name1.count("u") + name2.count("u")
E = name1.count("e") + name2.count("e")
TRUE = T + R + U + E

L = name1.count("l") + name2.count("l")
O = name1.count("o") + name2.count("o")
V = name1.count("v") + name2.count("v")
E = name1.count("e") + name2.count("e")
LOVE = L + O + V + E 

total = (TRUE*10) + LOVE

if total<10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total>40 and total<50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
