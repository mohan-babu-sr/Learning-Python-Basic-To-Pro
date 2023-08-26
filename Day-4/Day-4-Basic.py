import random

# Random for int
myRandom = random.randint(1, 10)
print(myRandom)

# Random for float
myFloat = random.random()
print(myFloat * 5)

# Randomly tell the user "Heads" or "Tails".
import random
choice = random.randint(0,1)

if choice == 1:
    print("Heads")
else:
    print("Tails")

# Lists 
fruits = ["Apple", "Orange"]
fruits.append("Mango")
fruits.extend(["Grapes", "Banana"])
print(fruits)
print(fruits[0])

# Random person selected will have to pay for everybody's food bill.
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
randomNumber = random.randint(1, len(names) - 1)
randomPerson = names[randomNumber]
# or
randomPerson = random.choice(names)
print(f"{randomPerson} is going to buy the meal today!")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])

# Write your code below this row 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")