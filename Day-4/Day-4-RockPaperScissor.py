import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# Rock wins against scissors
# Scissors win against paper
# Paper wins against rock

RPS = [rock, paper, scissors]
# 0, 1, 2
machine_input = random.randint(0, 2)
# print(machine_input)
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(RPS[user_input])
print("Computer chose:")
print(RPS[machine_input])

if user_input == machine_input:
  print("Draw")
elif user_input == 0 and machine_input == 2:
  print("You win")
elif user_input == 2 and machine_input == 1:
  print("You win")
elif user_input == 1 and machine_input == 0:
  print("You win")
else:
  print("You lose")
