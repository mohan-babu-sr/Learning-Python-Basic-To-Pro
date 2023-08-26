
# for loop
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
  print(fruit)

# Find the Average height 
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
total = 0
for height in student_heights:
    total += height

avg = total/len(student_heights)
print(round(avg))

# Range 
total_number = 0
for number in range(1, 101, 2):
    total_number += number + 1

print(total_number)

# FizzBuzz game
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)